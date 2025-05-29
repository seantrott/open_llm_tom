"""Run FB task by loading models from HF locally."""

import pandas as pd
import numpy as np
import transformers
import torch
import os

from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


MODELS = {
    
    ### OLMo
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

    ### Pythia (To run locally)
    "EleutherAI/pythia-12b": "Pythia 12B", 
    "EleutherAI/pythia-6.9b": "Pythia 6.9B",
    "EleutherAI/pythia-2.8b": "Pythia 2.8B",
    "EleutherAI/pythia-1.4b": "Pythia 1.4B",
    "EleutherAI/pythia-1b": "Pythia 1B",
    "EleutherAI/pythia-410m": "Pythia 410m",
    "EleutherAI/pythia-160m": "Pythia 160m",
    "EleutherAI/pythia-70m": "Pythia 70m",
    "EleutherAI/pythia-14m": "Pythia 14m",

    ### Qwen (TO DO)
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
    "Qwen/Qwen2.5-32B-Instruct": "Qwen 2.5 32B Instruct"

    ### ALso run: smaller Llama 3, llama 3.1, llama 2, Gemma
}



def next_seq_prob(model, tokenizer, seen, unseen):
    device = next(model.parameters()).device  # get model's actual device
    input_ids = tokenizer.encode(seen, return_tensors="pt").to(device)
    unseen_ids = tokenizer.encode(unseen)

    log_probs = []
    for unseen_id in unseen_ids:
        with torch.no_grad():
            logits = model(input_ids).logits

        next_token_logits = logits[0, -1]
        next_token_probs = torch.softmax(next_token_logits, dim=0)

        prob = next_token_probs[unseen_id]
        log_probs.append(torch.log(prob))

        # Append next token to input
        next_token_tensor = torch.tensor([[unseen_id]], device=device)
        input_ids = torch.cat((input_ids, next_token_tensor), dim=1)

    total_log_prob = sum(log_probs)
    total_prob = torch.exp(total_log_prob)
    return total_prob.item()





def main(model_path):

    # Set up save path, filename, etc.
    savepath = f"data/processed/fb_local/"
    if not os.path.exists(savepath): 
        os.makedirs(savepath)

    if "/" in model_path:
        filename = "fb-" + model_path.split("/")[1] + ".csv"
    else:
        filename = "fb-" + model_path + ".csv"

    print(filename)
    print(savepath)

    ### Load model
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto"  # spread across available GPUs
    )
    tokenizer = AutoTokenizer.from_pretrained(model_path)


    ### Load data
    df_fb = pd.read_csv("data/raw/fb.csv")

    results = []
    ### Run model
    with tqdm(total=len(df_fb)) as pbar:
        for index, row in df_fb.iterrows():
            passage = row['passage'].replace("[MASK].", "")
            sep = " " if not passage.endswith(" ") else ""
            start_location = sep + row['start']
            end_location = sep + row['end']


            start_prob = next_seq_prob(model, tokenizer, passage, start_location)
            end_prob = next_seq_prob(model, tokenizer, passage, end_location)

            if start_prob == 0 or end_prob == 0:
                continue

            results.append({
                'start_prob': start_prob,
                'end_prob': end_prob,
                'passage': row['passage'],
                'start': row['start'],
                'end': row['end'],
                'knowledge_cue': row['knowledge_cue'],
                'first_mention': row['first_mention'],
                'recent_mention': row['recent_mention'],
                'log_odds': np.log2(start_prob / end_prob),
                'condition': row['condition']
            })


            
            pbar.update(1)

    ### Create DataFRame
    df_results = pd.DataFrame(results)
    df_results['model_path'] = model_path
    df_results['model_shorthand'] = MODELS[model_path]

    df_results.to_csv(os.path.join(savepath,filename), index=False)


if __name__ == "__main__":

    paths = ['Qwen/Qwen2.5-0.5B', 'Qwen/Qwen2.5-0.5B-Instruct', 
    'Qwen/Qwen2.5-1.5B', 'Qwen/Qwen2.5-1.5B-Instruct', 
    'Qwen/Qwen2.5-3B', 'Qwen/Qwen2.5-3B-Instruct', 
    'Qwen/Qwen2.5-7B', 'Qwen/Qwen2.5-7B-Instruct', 
    'Qwen/Qwen2.5-14B', 'Qwen/Qwen2.5-14B-Instruct', 
    'Qwen/Qwen2.5-32B', 'Qwen/Qwen2.5-32B-Instruct']

    for model_path in paths:
        # model_path = "allenai/OLMo-2-1124-13B-DPO"
        main(model_path)


