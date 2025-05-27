"""Run FB task by loading models from HF locally."""

import pandas as pd
import numpy as np
import transformers
import torch
import os

from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


MODELS = {
    'allenai/OLMo-2-1124-7B': 'OLMo 2 7B'
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

    model_path = "allenai/OLMo-2-1124-7B"
    main(model_path)


