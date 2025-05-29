"""Run HF models on FB task."""

# import utils
import pandas as pd
import os

from lib.hf_client import HFClient
from tqdm import tqdm


#### MODELS
MODELS = {
    ### HF models
    "meta-llama/Meta-Llama-3-70B": "Llama 3 70b",
    "meta-llama/Meta-Llama-3-8B": "Llama 3 8b",
    "meta-llama/Meta-Llama-3-8B-Instruct": "Llama 3 8b instruct",
    "meta-llama/Meta-Llama-3-70B-Instruct": "Llama 3 70b instruct",
    "meta-llama/Llama-3.1-70B": "Llama 3.1 70b",
    "meta-llama/Llama-3.1-70B-Instruct": "Llama 3.1 70B Instruct",
    "meta-llama/Llama-3.1-8B-Instruct": "Llama 3.1 8B Instruct",
    "meta-llama/Llama-3.1-8B": "Llama 3.1 8B",
    "mistralai/Mixtral-8x7B-v0.1": "Mixtral 8x7b",
    "mistralai/Mixtral-8x7B-Instruct-v0.1": "Mixtral 8x7B Instruct",
    "meta-llama/Llama-2-7b-hf": "Llama 2 7B",
    "meta-llama/Llama-2-13b-hf": "Llama 2 13B",
    "meta-llama/Llama-2-70b-hf": "Llama 2 70B",
    "meta-llama/Llama-2-7b-chat-hf": "Llama 2 7B Instruct",
    "meta-llama/Llama-2-13b-chat-hf": "Llama 2 13B Instruct",
    "meta-llama/Llama-2-70b-chat-hf": "Llama 2 70B Instruct",
    "EleutherAI/pythia-12b": "Pythia 12B",
    "Qwen/Qwen2.5-7B-Instruct": "Qwen 2.5 7B Instruct",
    "Qwen/Qwen2.5-14B-Instruct": "Qwen 2.5 14B Instruct",
    "Qwen/Qwen2.5-72B-Instruct": "Qwen 2.5 72B Instruct",
    "Qwen/Qwen2.5-7B": "Qwen 2.5 7B",

    ### LOCAL MODELS
    ### OLMO
    'allenai/OLMo-2-1124-7B': 'OLMo 2 7B',
    'allenai/OLMo-2-1124-7B-SFT': 'OLMo 2 7B SFT',
    'allenai/OLMo-2-1124-7B-DPO': 'OLMo 2 7B DPO',
    'allenai/OLMo-2-1124-7B-Instruct': 'OLMO 2 7B Instruct', 
    'allenai/OLMo-2-1124-13B': 'OLMO 2 13B',
    'allenai/OLMo-2-1124-13B-SFT': 'OLMO 2 13B SFT', 
    'allenai/OLMo-2-1124-13B-DPO': 'OLMo 2 13B DPO', 
    'allenai/OLMo-2-1124-13B-Instruct': 'OLMO 2 13B Instruct',
    'allenai/OLMo-2-0325-32B': 'OLMO 2 32B',
    'allenai/OLMo-2-0325-32B-SFT': 'OLMO 2 32B SFT', 
    'allenai/OLMo-2-0325-32B-Instruct': 'OLMO 2 32B Instruct',
    'allenai/OLMo-2-0325-32B-DPO': 'OLMO 2 32B DPO',
    'allenai/OLMo-2-0425-1B': 'OLMO 2 1B',
    'allenai/OLMo-2-0425-1B-SFT': 'OLMO 2 1B SFT',
    'allenai/OLMo-2-0425-1B-DPO': 'OLMO 2 1B DPO',
    'allenai/OLMo-2-0425-1B-Instruct': 'OLMO 2 1B Instruct',


    ## Pythia 
    "EleutherAI/pythia-12b": "Pythia 12B", ### TODO
    "EleutherAI/pythia-6.9b": "Pythia 6.9B",
    "EleutherAI/pythia-2.8b": "Pythia 2.8B",
    "EleutherAI/pythia-1.4b": "Pythia 1.4B",
    "EleutherAI/pythia-1b": "Pythia 1B",
    "EleutherAI/pythia-410m": "Pythia 410m",
    "EleutherAI/pythia-160m": "Pythia 160m",
    "EleutherAI/pythia-70m": "Pythia 70m",
    "EleutherAI/pythia-14m": "Pythia 14m",


    ### QWEN
    "Qwen/Qwen2.5-0.5B": "Qwen 2.5 0.5B",
    "Qwen/Qwen2.5-0.5B-Instruct": "Qwen 2.5 0.5B Instruct",
    "Qwen/Qwen2.5-1.5B": "Qwen 2.5 1.5B",
    "Qwen/Qwen2.5-1.5B-Instruct": "Qwen 2.5 1.5 Instruct",
    "Qwen/Qwen2.5-3B": "Qwen 2.5 3B",
    "Qwen/Qwen2.5-3B-Instruct": "Qwen 2.5 3B Instruct",
    "Qwen/Qwen2.5-7B": "Qwen 2.5 7B",
    "Qwen/Qwen2.5-7B-Instruct": "Qwen 2.5 7B Instruct",
    "Qwen/Qwen2.5-14B": "Qwen 2.5 14B",
    "Qwen/Qwen2.5-14B-Instruct": "Qwen 2.5 14B Instruct",
    "Qwen/Qwen2.5-32B": "Qwen 2.5 32B",
    "Qwen/Qwen2.5-32B-Instruct": "Qwen 2.5 32B Instruct",

    ### Gemma
    "google/gemma-2b": "Gemma 2 2B",
    "google/gemma-2b-it": "Gemma 2 2B Instruct",
    "google/gemma-7b": "Gemma 2 7B",
    "google/gemma-7b-it": "Gemma 2 7B Instruct",


    ### LLama 3 (needs authentication)
    "meta-llama/Meta-Llama-3-8B": "LLaMA 3 8B",
    "meta-llama/Meta-Llama-3-8B-Instruct": "LLaMA 3 8B Instruct",

    ### Llama 3.1 (needs authentication)
    # "meta-llama/Meta-Llama-3-8B": "LLaMA 3 8B",
    # "meta-llama/Meta-Llama-3-8B-Instruct": "LLaMA 3 8B Instruct",

}

#### SETUP HF
def setup_hf():
    ### Requires API key and ORG to be saved as environmental variables
    api_key = os.getenv("HF_API_KEY")
    org = os.getenv("HF_ORG")
    hf_client = HFClient(api_key, org, use_tqdm=True, kill_endpoint_on_exit=False)
    return hf_client


def get_logprob(passage, location):

    final_passage = passage + location
    response = hf_client.send_prompt(final_passage, max_new_tokens=1)

    return response[0]['details']['prefill'][-1]


def main(df_fb, model_path):


    # Set up save path, filename, etc.
    savepath = f"data/processed/fb/"
    if not os.path.exists(savepath): 
        os.makedirs(savepath)

    if "/" in model_path:
        filename = "fb-" + model_path.split("/")[1] + ".csv"
    else:
        filename = "fb-" + model_path + ".csv"

    print(filename)
    print(savepath)

    results = []
    with tqdm(total=df_fb.shape[0]) as pbar:    
        for index, row in df_fb.iterrows():
            
            ### Replace MASK with space
            passage = row['passage'].replace("[MASK].", "")

            ### If necessary, buffer and end location
            start_location = row['start'] if passage.endswith(" ") else " " + row['start']
            end_location = row['end'] if passage.endswith(" ") else " " + row['end']
            
            ### Get lp for both start and end location
            lp_start_response = get_logprob(passage, start_location)
            lp_end_response = get_logprob(passage, end_location)
            lp_start = lp_start_response['logprob']
            lp_end = lp_end_response['logprob']
        
            results.append({
                'lp_start': lp_start,
                'lp_end': lp_end,
                'passage': row['passage'],
                'start': row['start'],
                'end': row['end'],
                'knowledge_cue': row['knowledge_cue'],
                'first_mention': row['first_mention'],
                'recent_mention': row['recent_mention'],
                'log_odds': lp_start - lp_end,
                'condition': row['condition']
            })
        


            pbar.update(1)

    df_results = pd.DataFrame(results)
    df_results['model_path'] = model_path
    df_results['model_shorthand'] = MODELS[model_path]

    df_results.to_csv(os.path.join(savepath,filename), index=False)


if __name__ == "__main__":

    ### Select model
    selected_model = "Qwen/Qwen2.5-7B"
    if selected_model not in MODELS:
        selected_model = None
        raise ValueError(f"Model {selected_model} not found in MODELS")

    ### Wait for model    
    hf_client = setup_hf()
    hf_client.wait_for_model(selected_model)

    ### Load dataframe
    df_fb = pd.read_csv("data/raw/fb.csv")

    main(df_fb, selected_model)
