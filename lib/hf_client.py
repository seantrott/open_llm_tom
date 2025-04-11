import requests, atexit

import time
from tqdm import tqdm

class HFClient:
    HF_URL = "https://api.endpoints.huggingface.cloud/v2/endpoint"

    def __init__(self, 
                 api_key, 
                 organization = "language-and-cognition-ucsd", 
                 use_tqdm = False, 
                 kill_endpoint_on_exit = True):
        self.api_key = api_key
        self.organization = organization

        self.use_tqdm = use_tqdm

        self.model_repo = None
        self.model_name = None
        self.endpoint = None

        self.BASE_URL = f"{HFClient.HF_URL}/{organization}"
        self.HEADERS = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
            "Content-Type": "application/json"
        }

        self.DASHBOARD_URL = f"https://ui.endpoints.huggingface.co/{organization}/endpoints"

        if kill_endpoint_on_exit:
            atexit.register(self.teardown_endpoint)

    def _get_model_name(self, 
                        model_repo_name):
        models = requests.get(self.BASE_URL, headers = self.HEADERS)

        list_models = models.json()['items']

        for model in list_models:
            if model['model']['repository'] == model_repo_name:
                return model["name"]
            
        return None
    
    def _is_model_ready(self, 
                        model_name):
        url = f'{self.BASE_URL}/{model_name}'
        model_info = requests.get(url, headers = self.HEADERS)

        return model_info.json()['status']['state'] == 'running'
    
    def _get_endpoint_url(self, model_name):
        url = f'{self.BASE_URL}/{model_name}'
        model_info = requests.get(url, headers = self.HEADERS)

        return model_info.json()['status']['url']
    
    def wait_for_model(self, 
                       model_repo_name): 
        model_name = self._get_model_name(model_repo_name)
    
        if model_name is None:
            raise Exception(f"Model {model_repo_name} not found in the list of available models on HF API. \n Start on dashboard ({self.DASHBOARD_URL}) first, or launch programmatically.")
            
        TIME_WAIT = 10
        while not self._is_model_ready(model_name):
            for _ in tqdm(range(TIME_WAIT), desc=f"{model_name} initializing, waiting {TIME_WAIT}s", disable=not self.use_tqdm, leave=False):
                time.sleep(1)

        model_url = self._get_endpoint_url(model_name)

        self.endpoint = model_url
        self.model_repo = model_repo_name
        self.model_name = model_name

    def _send_request(self, 
                      payload, 
                      timeout = None):
        if self.endpoint is None:
            raise Exception("Model is not initialized. Run `wait_for_model` first.")

        return requests.post(self.endpoint, headers = self.HEADERS, json = payload, timeout=timeout).json()
    
    def send_prompt(self, 
                    prompt, 
                    max_new_tokens = 100, 
                    temperature = 0.0, 
                    details = True, 
                    max_retries = 5, 
                    timeout = 30.0, backoff_delay = 3.0):
        
        if temperature == 0.0:
            temperature = 1.0
            do_sample = False
        else:
            do_sample = True

        payload = {
            "inputs": prompt,
            "parameters": {
                "details": details,
                "max_new_tokens": max_new_tokens,
                "temperature": temperature,
                "decoder_input_details": details,
                "do_sample": do_sample
            }
        }

        for attempt in range(max_retries):
            try:
                response = self._send_request(payload, timeout = timeout)

                break
            except requests.exceptions.Timeout:
                response = None
                print(f"Timeout from HF API on attempt {attempt + 1}, waiting before next attempt...")

                for _ in tqdm(range(backoff_delay ** attempt), desc=f"Timeout occured, waiting {backoff_delay ** attempt}s", disable=not self.use_tqdm, leave=False):
                    time.sleep(1)

        if response is None:
            raise Exception(f'No responses from HF API after {max_retries} attempts')

        response_data = response
        
        return response_data
    
    def teardown_endpoint(self):
        if self.endpoint is not None:
            url = f"{self.BASE_URL}/{self.organization}/{self.model_name}/scale-to-zero"
            requests.post(url, headers = self.HEADERS)

            print(f"scaled down the {self.model_name} endpoint for {self.model_repo}, but double check on the dashboard ({self.DASHBOARD_URL}).")