"""Run FB task by loading models from HF locally."""

import pandas as pd
import numpy as np
import transformers
import torch

from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

def next_seq_prob(model, tokenizer, seen, unseen):
    device = next(model.parameters()).device  # Detect model's device

    input_ids = tokenizer.encode(seen, return_tensors="pt").to(device)
    unseen_ids = tokenizer.encode(unseen)

    log_probs = []
    for unseen_id in unseen_ids:
        with torch.no_grad():
            logits = model(input_ids).logits

        next_token_logits = logits[0, -1]
        next_token_probs = torch.softmax(next_token_logits, 0)

        prob = next_token_probs[unseen_id]
        log_probs.append(torch.log(prob))

        # Add next token to input, ensuring device match
        next_token_tensor = torch.tensor([[unseen_id]], device=device)
        input_ids = torch.cat((input_ids, next_token_tensor), dim=1)

    total_log_prob = sum(log_probs)
    total_prob = torch.exp(total_log_prob)
    return total_prob.item()




### TESTING OUT


### Load data
df_fb = pd.read_csv("data/raw/fb.csv")
df_fb.head(1)



### Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

mpath = "allenai/OLMo-2-1124-7B"
model = AutoModelForCausalLM.from_pretrained(
    mpath,
    output_hidden_states = False,
    device_map="auto"  
).to(device) 

tokenizer = AutoTokenizer.from_pretrained(mpath)



### Run model
results = []

with tqdm(total=df_fb.shape[0]) as pbar:    
        
    for index, row in df_fb.iterrows():
        passage = row['passage'].replace("[MASK].", "")
        start_location = row['start'] if passage.endswith(" ") else " " + row['start']
        end_location = row['end'] if passage.endswith(" ") else " " + row['end']
    
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
            'log_odds': np.log2(start_prob/end_prob),
            'condition': row['condition']
        })

        pbar.update(1)

df_results = pd.DataFrame(results)

### Quick check
from scipy.stats import ttest_ind
# Separate into two groups
group1 = df_results[df_results['condition'] == 'True Belief']['log_odds']
group2 = df_results[df_results['condition'] == 'False Belief']['log_odds']

# Run independent t-test (assumes unequal variance by default)
t_stat, p_val = ttest_ind(group1, group2, equal_var=False)

print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_val:.3f}")

print(df_results.groupby("condition").mean("log_odds"))

