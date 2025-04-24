"""Run HF models on FB task."""

# import utils
import pandas as pd
import os

from lib.hf_client import HFClient
from tqdm import tqdm


#### MODELS
MODELS = {
    "meta-llama/Meta-Llama-3-70B": "Llama 3 70b",
    "meta-llama/Meta-Llama-3-8B": "Llama 3 8b",
    "meta-llama/Meta-Llama-3-8B-Instruct": "Llama 3 8b instruct",
    "meta-llama/Llama-3.1-70B": "Llama 3.1 70b",
    "mistralai/Mixtral-8x7B-v0.1": "Mixtral 8x7b",
    "mistralai/Mixtral-8x22B-v0.1": "Mixtral 8x22b",
    "EleutherAI/pythia-6.9b": "Pythia 6.9B",
    "EleutherAI/pythia-12b": "Pythia 12B"
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
                'lp_end': lp_start,
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
    selected_model = "meta-llama/Meta-Llama-3-8B"
    if selected_model not in MODELS:
        selected_model = None
        raise ValueError(f"Model {selected_model} not found in MODELS")

    ### Wait for model    
    hf_client = setup_hf()
    hf_client.wait_for_model(selected_model)

    ### Load dataframe
    df_fb = pd.read_csv("data/raw/fb.csv")

    main(df_fb, selected_model)
