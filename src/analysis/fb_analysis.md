---
title: "Analysis of False Belief Task"
author: "Sean Trott"
date: "April 24, 2025"
output:
  html_document:
    keep_md: yes
    toc: yes
    toc_float: yes
---






# Load LLM data


``` r
# setwd("/Users/seantrott/Dropbox/UCSD/Research/NLMs/open_llm_tom/src/analysis")
directory_path <- "../../data/processed/fb_local/"
csv_files <- list.files(path = directory_path, pattern = "*.csv", full.names = TRUE)
csv_list <- csv_files %>%
  map(~ read_csv(.))
```

```
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 0 Columns: 2
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (2): model_path, model_shorthand
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 0 Columns: 2
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (2): model_path, model_shorthand
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
## Rows: 192 Columns: 12
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (9): passage, start, end, knowledge_cue, first_mention, recent_mention, ...
## dbl (3): start_prob, end_prob, log_odds
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```

``` r
df_all_models <- bind_rows(csv_list) %>%
  mutate(model_shorthand = str_to_title(model_shorthand))
nrow(df_all_models)
```

```
## [1] 7872
```

``` r
length(unique(df_all_models$model_shorthand))
```

```
## [1] 41
```

``` r
table(df_all_models$model_path)
```

```
## 
##             allenai/OLMo-2-0325-32B         allenai/OLMo-2-0325-32B-DPO 
##                                 192                                 192 
##    allenai/OLMo-2-0325-32B-Instruct         allenai/OLMo-2-0325-32B-SFT 
##                                 192                                 192 
##              allenai/OLMo-2-0425-1B          allenai/OLMo-2-0425-1B-DPO 
##                                 192                                 192 
##     allenai/OLMo-2-0425-1B-Instruct          allenai/OLMo-2-0425-1B-SFT 
##                                 192                                 192 
##             allenai/OLMo-2-1124-13B         allenai/OLMo-2-1124-13B-DPO 
##                                 192                                 192 
##    allenai/OLMo-2-1124-13B-Instruct         allenai/OLMo-2-1124-13B-SFT 
##                                 192                                 192 
##              allenai/OLMo-2-1124-7B          allenai/OLMo-2-1124-7B-DPO 
##                                 192                                 192 
##     allenai/OLMo-2-1124-7B-Instruct          allenai/OLMo-2-1124-7B-SFT 
##                                 192                                 192 
##              EleutherAI/pythia-1.4b               EleutherAI/pythia-12b 
##                                 192                                 192 
##               EleutherAI/pythia-14m              EleutherAI/pythia-160m 
##                                 192                                 192 
##                EleutherAI/pythia-1b              EleutherAI/pythia-2.8b 
##                                 192                                 192 
##              EleutherAI/pythia-410m              EleutherAI/pythia-6.9b 
##                                 192                                 192 
##               EleutherAI/pythia-70m                     google/gemma-2b 
##                                 192                                 192 
##                  google/gemma-2b-it          meta-llama/Meta-Llama-3-8B 
##                                 192                                 192 
## meta-llama/Meta-Llama-3-8B-Instruct                   Qwen/Qwen2.5-0.5B 
##                                 192                                 192 
##          Qwen/Qwen2.5-0.5B-Instruct                   Qwen/Qwen2.5-1.5B 
##                                 192                                 192 
##          Qwen/Qwen2.5-1.5B-Instruct                    Qwen/Qwen2.5-14B 
##                                 192                                 192 
##           Qwen/Qwen2.5-14B-Instruct                    Qwen/Qwen2.5-32B 
##                                 192                                 192 
##           Qwen/Qwen2.5-32B-Instruct                     Qwen/Qwen2.5-3B 
##                                 192                                 192 
##            Qwen/Qwen2.5-3B-Instruct                     Qwen/Qwen2.5-7B 
##                                 192                                 192 
##            Qwen/Qwen2.5-7B-Instruct 
##                                 192
```

``` r
table(df_all_models$model_shorthand)
```

```
## 
##             Gemma 2 2b    Gemma 2 2b Instruct             Llama 3 8b 
##                    192                    192                    192 
##    Llama 3 8b Instruct             Olmo 2 13b         Olmo 2 13b Dpo 
##                    192                    192                    192 
##    Olmo 2 13b Instruct         Olmo 2 13b Sft              Olmo 2 1b 
##                    192                    192                    192 
##          Olmo 2 1b Dpo     Olmo 2 1b Instruct          Olmo 2 1b Sft 
##                    192                    192                    192 
##             Olmo 2 32b         Olmo 2 32b Dpo    Olmo 2 32b Instruct 
##                    192                    192                    192 
##         Olmo 2 32b Sft              Olmo 2 7b          Olmo 2 7b Dpo 
##                    192                    192                    192 
##     Olmo 2 7b Instruct          Olmo 2 7b Sft            Pythia 1.4b 
##                    192                    192                    192 
##             Pythia 12b             Pythia 14m            Pythia 160m 
##                    192                    192                    192 
##              Pythia 1b            Pythia 2.8b            Pythia 410m 
##                    192                    192                    192 
##            Pythia 6.9b             Pythia 70m          Qwen 2.5 0.5b 
##                    192                    192                    192 
## Qwen 2.5 0.5b Instruct  Qwen 2.5 1.5 Instruct          Qwen 2.5 1.5b 
##                    192                    192                    192 
##           Qwen 2.5 14b  Qwen 2.5 14b Instruct           Qwen 2.5 32b 
##                    192                    192                    192 
##  Qwen 2.5 32b Instruct            Qwen 2.5 3b   Qwen 2.5 3b Instruct 
##                    192                    192                    192 
##            Qwen 2.5 7b   Qwen 2.5 7b Instruct 
##                    192                    192
```

``` r
### Load #params
df_model_properties = read_csv("../../data/processed/model_properties.csv") %>% 
  mutate(model_shorthand = str_to_title(model_shorthand))
```

```
## Rows: 58 Columns: 5
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (4): model_path, model_shorthand, base_instruct, model_family
## dbl (1): num_params
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```

``` r
nrow(df_model_properties)
```

```
## [1] 58
```

``` r
### Load training data
df_training_data = read_csv("../../data/processed/model_training_data.csv")%>% 
  mutate(model_shorthand = str_to_title(model_shorthand))
```

```
## Rows: 58 Columns: 4
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr (3): model_path, model_shorthand, notes
## dbl (1): num_training_tokens
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```

``` r
table(df_training_data$model_shorthand)
```

```
## 
##             Gemma 2 2b    Gemma 2 2b Instruct             Gemma 2 7b 
##                      1                      1                      1 
##    Gemma 2 7b Instruct            Llama 2 13b   Llama 2 13b Instruct 
##                      1                      1                      1 
##            Llama 2 70b   Llama 2 70b Instruct             Llama 2 7b 
##                      1                      1                      1 
##    Llama 2 7b Instruct            Llama 3 70b   Llama 3 70b Instruct 
##                      1                      1                      1 
##             Llama 3 8b    Llama 3 8b Instruct          Llama 3.1 70b 
##                      1                      1                      1 
## Llama 3.1 70b Instruct           Llama 3.1 8b  Llama 3.1 8b Instruct 
##                      1                      1                      1 
##           Mixtral 8x7b  Mixtral 8x7b Instruct             Olmo 2 13b 
##                      1                      1                      1 
##         Olmo 2 13b Dpo    Olmo 2 13b Instruct         Olmo 2 13b Sft 
##                      1                      1                      1 
##              Olmo 2 1b          Olmo 2 1b Dpo     Olmo 2 1b Instruct 
##                      1                      1                      1 
##          Olmo 2 1b Sft             Olmo 2 32b         Olmo 2 32b Dpo 
##                      1                      1                      1 
##    Olmo 2 32b Instruct         Olmo 2 32b Sft              Olmo 2 7b 
##                      1                      1                      1 
##          Olmo 2 7b Dpo     Olmo 2 7b Instruct          Olmo 2 7b Sft 
##                      1                      1                      1 
##            Pythia 1.4b             Pythia 12b             Pythia 14m 
##                      1                      1                      1 
##            Pythia 160m              Pythia 1b            Pythia 2.8b 
##                      1                      1                      1 
##            Pythia 410m            Pythia 6.9b             Pythia 70m 
##                      1                      1                      1 
##          Qwen 2.5 0.5b Qwen 2.5 0.5b Instruct  Qwen 2.5 1.5 Instruct 
##                      1                      1                      1 
##          Qwen 2.5 1.5b           Qwen 2.5 14b  Qwen 2.5 14b Instruct 
##                      1                      1                      1 
##           Qwen 2.5 32b  Qwen 2.5 32b Instruct            Qwen 2.5 3b 
##                      1                      1                      1 
##   Qwen 2.5 3b Instruct  Qwen 2.5 72b Instruct            Qwen 2.5 7b 
##                      1                      1                      1 
##   Qwen 2.5 7b Instruct 
##                      1
```

``` r
### Join
df_all_properties = df_training_data %>%
  inner_join(df_model_properties)
```

```
## Joining with `by = join_by(model_path, model_shorthand)`
```

``` r
table(df_all_properties$model_shorthand)
```

```
## 
##             Gemma 2 2b    Gemma 2 2b Instruct             Gemma 2 7b 
##                      1                      1                      1 
##    Gemma 2 7b Instruct            Llama 2 13b   Llama 2 13b Instruct 
##                      1                      1                      1 
##            Llama 2 70b   Llama 2 70b Instruct             Llama 2 7b 
##                      1                      1                      1 
##    Llama 2 7b Instruct            Llama 3 70b   Llama 3 70b Instruct 
##                      1                      1                      1 
##             Llama 3 8b    Llama 3 8b Instruct          Llama 3.1 70b 
##                      1                      1                      1 
## Llama 3.1 70b Instruct           Llama 3.1 8b  Llama 3.1 8b Instruct 
##                      1                      1                      1 
##           Mixtral 8x7b  Mixtral 8x7b Instruct             Olmo 2 13b 
##                      1                      1                      1 
##         Olmo 2 13b Dpo    Olmo 2 13b Instruct         Olmo 2 13b Sft 
##                      1                      1                      1 
##              Olmo 2 1b          Olmo 2 1b Dpo     Olmo 2 1b Instruct 
##                      1                      1                      1 
##          Olmo 2 1b Sft             Olmo 2 32b         Olmo 2 32b Dpo 
##                      1                      1                      1 
##    Olmo 2 32b Instruct         Olmo 2 32b Sft              Olmo 2 7b 
##                      1                      1                      1 
##          Olmo 2 7b Dpo     Olmo 2 7b Instruct          Olmo 2 7b Sft 
##                      1                      1                      1 
##            Pythia 1.4b             Pythia 12b             Pythia 14m 
##                      1                      1                      1 
##            Pythia 160m              Pythia 1b            Pythia 2.8b 
##                      1                      1                      1 
##            Pythia 410m            Pythia 6.9b             Pythia 70m 
##                      1                      1                      1 
##          Qwen 2.5 0.5b Qwen 2.5 0.5b Instruct  Qwen 2.5 1.5 Instruct 
##                      1                      1                      1 
##          Qwen 2.5 1.5b           Qwen 2.5 14b  Qwen 2.5 14b Instruct 
##                      1                      1                      1 
##           Qwen 2.5 32b  Qwen 2.5 32b Instruct            Qwen 2.5 3b 
##                      1                      1                      1 
##   Qwen 2.5 3b Instruct  Qwen 2.5 72b Instruct            Qwen 2.5 7b 
##                      1                      1                      1 
##   Qwen 2.5 7b Instruct 
##                      1
```

``` r
nrow(df_all_properties)
```

```
## [1] 58
```

``` r
#### Bind with FB data
df_all_models = df_all_models %>%
  inner_join(df_all_properties)
```

```
## Joining with `by = join_by(model_path, model_shorthand)`
```

``` r
nrow(df_all_models)
```

```
## [1] 7872
```

``` r
table(df_all_models$model_shorthand)
```

```
## 
##             Gemma 2 2b    Gemma 2 2b Instruct             Llama 3 8b 
##                    192                    192                    192 
##    Llama 3 8b Instruct             Olmo 2 13b         Olmo 2 13b Dpo 
##                    192                    192                    192 
##    Olmo 2 13b Instruct         Olmo 2 13b Sft              Olmo 2 1b 
##                    192                    192                    192 
##          Olmo 2 1b Dpo     Olmo 2 1b Instruct          Olmo 2 1b Sft 
##                    192                    192                    192 
##             Olmo 2 32b         Olmo 2 32b Dpo    Olmo 2 32b Instruct 
##                    192                    192                    192 
##         Olmo 2 32b Sft              Olmo 2 7b          Olmo 2 7b Dpo 
##                    192                    192                    192 
##     Olmo 2 7b Instruct          Olmo 2 7b Sft            Pythia 1.4b 
##                    192                    192                    192 
##             Pythia 12b             Pythia 14m            Pythia 160m 
##                    192                    192                    192 
##              Pythia 1b            Pythia 2.8b            Pythia 410m 
##                    192                    192                    192 
##            Pythia 6.9b             Pythia 70m          Qwen 2.5 0.5b 
##                    192                    192                    192 
## Qwen 2.5 0.5b Instruct  Qwen 2.5 1.5 Instruct          Qwen 2.5 1.5b 
##                    192                    192                    192 
##           Qwen 2.5 14b  Qwen 2.5 14b Instruct           Qwen 2.5 32b 
##                    192                    192                    192 
##  Qwen 2.5 32b Instruct            Qwen 2.5 3b   Qwen 2.5 3b Instruct 
##                    192                    192                    192 
##            Qwen 2.5 7b   Qwen 2.5 7b Instruct 
##                    192                    192
```

``` r
df_all_models = df_all_models %>%
  mutate(model_shorthand = str_to_title(model_shorthand))


length(unique(df_all_models$model_shorthand))
```

```
## [1] 41
```

``` r
length(unique(df_all_models$model_family))
```

```
## [1] 5
```

``` r
df_all_models <- df_all_models %>%
  mutate(model_shorthand = recode(model_shorthand,
    "Gemma 2 2b"          = "Gemma 1 2b",
    "Gemma 2 2b Instruct" = "Gemma 1 2b Instruct"
  ))
```


# LLM Analysis

## Sensitivity to mental states


``` r
### Visualization
df_all_models %>%
  ggplot(aes(x = log_odds,
             y = reorder(model_shorthand, num_params),
             fill = condition)) +
  geom_density_ridges2(aes(height = ..density..), 
                       color=NA, 
                       scale=.85, 
                       # size=1, 
                       alpha = .8,
                       stat="density") +
  labs(x = "Log Odds (Start vs. End)",
       y = "",
       fill = "") +
  theme_minimal() +
  geom_vline(xintercept = 0, linetype = "dotted") +
  theme(
    legend.position = "bottom"
  ) + 
  theme(axis.title = element_text(size=rel(1.2)),
        axis.text = element_text(size = rel(1.2)),
        legend.text = element_text(size = rel(1.2)),
        legend.title = element_text(size = rel(1.2)),
        strip.text.x = element_text(size = rel(1.2))) +
    scale_fill_manual(values = viridisLite::viridis(2, option = "mako", 
                                                    begin = 0.8, end = 0.15)) +
  facet_wrap(~knowledge_cue)
```

```
## Warning: The dot-dot notation (`..density..`) was deprecated in ggplot2 3.4.0.
## ℹ Please use `after_stat(density)` instead.
## This warning is displayed once every 8 hours.
## Call `lifecycle::last_lifecycle_warnings()` to see where this warning was
## generated.
```

![](fb_analysis_files/figure-html/sensitivity-1.pdf)<!-- -->

``` r
### Visualization by model family
df_all_models %>%
  group_by(passage, condition, knowledge_cue, model_family) %>%
  summarise(m_lo = mean(log_odds)) %>%
  ggplot(aes(x = m_lo,
             y = model_family,
             fill = condition)) +
  geom_density_ridges2(aes(height = ..density..), 
                       color=NA, 
                       scale=.85, 
                       # size=1, 
                       alpha = .8,
                       stat="density") +
  labs(x = "Log Odds (Start vs. End)",
       y = "",
       fill = "") +
  theme_minimal() +
  geom_vline(xintercept = 0, linetype = "dotted") +
  theme(
    legend.position = "bottom"
  ) + 
  theme(axis.title = element_text(size=rel(1.2)),
        axis.text = element_text(size = rel(1.2)),
        legend.text = element_text(size = rel(1.2)),
        legend.title = element_text(size = rel(1.2)),
        strip.text.x = element_text(size = rel(1.2))) +
    scale_fill_manual(values = viridisLite::viridis(2, option = "mako", 
                                                    begin = 0.8, end = 0.15)) +
  facet_wrap(~knowledge_cue)
```

```
## `summarise()` has grouped output by 'passage', 'condition', 'knowledge_cue'.
## You can override using the `.groups` argument.
```

![](fb_analysis_files/figure-html/sensitivity-2.pdf)<!-- -->

``` r
### Visualization altogether
df_all_models %>%
  group_by(passage, condition, knowledge_cue) %>%
  summarise(m_lo = mean(log_odds)) %>%
  ggplot(aes(x = m_lo,
             y = knowledge_cue,
             fill = condition)) +
  geom_density_ridges2(aes(height = ..density..), 
                       color=NA, 
                       scale=.85, 
                       # size=1, 
                       alpha = .8,
                       stat="density") +
  labs(x = "Log Odds (Start vs. End)",
       y = "",
       fill = "") +
  theme_minimal() +
  geom_vline(xintercept = 0, linetype = "dotted") +
  theme(
    legend.position = "bottom"
  ) + 
  theme(axis.title = element_text(size=rel(1.2)),
        axis.text = element_text(size = rel(1.2)),
        legend.text = element_text(size = rel(1.2)),
        legend.title = element_text(size = rel(1.2)),
        strip.text.x = element_text(size = rel(1.2))) +
    scale_fill_manual(values = viridisLite::viridis(2, option = "mako", 
                                                    begin = 0.8, end = 0.15))
```

```
## `summarise()` has grouped output by 'passage', 'condition'. You can override
## using the `.groups` argument.
```

![](fb_analysis_files/figure-html/sensitivity-3.pdf)<!-- -->

Each model on its own:


``` r
# Function to fit models and perform model comparison
compare_models <- function(df) {
  if (n_distinct(df$condition) < 2) return(NULL)  # Skip if only one condition
  
  mod_full <- tryCatch(
    lmer(log_odds ~ condition + knowledge_cue + first_mention + recent_mention +
           (1 + condition | start), data = df, REML = FALSE),
    error = function(e) NULL
  )
  
  mod_reduced <- tryCatch(
    lmer(log_odds ~ knowledge_cue + first_mention + recent_mention +
           (1 + condition | start), data = df, REML = FALSE),
    error = function(e) NULL
  )
  
  if (is.null(mod_full) || is.null(mod_reduced)) return(NULL)
  
  anova_result <- anova(mod_full, mod_reduced)
  delta_aic <- AIC(mod_reduced) - AIC(mod_full)
  lrt_stat <- anova_result$Chisq[2]
  p_val <- anova_result$`Pr(>Chisq)`[2]
  
  # Extract coefficients
  coefs <- tryCatch(fixef(mod_full), error = function(e) return(rep(NA, 2)))
  cond_coef <- coefs[grep("^condition", names(coefs))]
  cue_coef <- coefs[grep("^knowledge_cue", names(coefs))]

  tibble(
    model_path = unique(df$model_path),
    delta_AIC = delta_aic,
    LRT_stat = lrt_stat,
    p_value = p_val,
    condition_coef = cond_coef,
    knowledge_cue_coef = cue_coef
  )
}

# Apply to each model_path
results_by_model_path <- df_all_models %>%
  group_by(model_path) %>%
  group_split() %>%
  map_dfr(compare_models)
```

```
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
```

``` r
results_by_model_path %>%
  arrange(LRT_stat)
```

```
## # A tibble: 41 × 6
##    model_path       delta_AIC LRT_stat p_value condition_coef knowledge_cue_coef
##    <chr>                <dbl>    <dbl>   <dbl>          <dbl>              <dbl>
##  1 meta-llama/Meta…     -2.00  7.77e-5   0.993      -0.000782            0.00235
##  2 EleutherAI/pyth…     -2.00  4.77e-4   0.983       0.00338            -0.240  
##  3 meta-llama/Meta…     -2.00  2.58e-3   0.959      -0.00507             0.0144 
##  4 Qwen/Qwen2.5-1.…     -1.99  6.02e-3   0.938       0.0329             -0.147  
##  5 Qwen/Qwen2.5-0.…     -1.99  8.76e-3   0.925       0.0348             -0.568  
##  6 allenai/OLMo-2-…     -1.99  1.05e-2   0.918      -0.0443              1.06   
##  7 google/gemma-2b      -1.98  1.54e-2   0.901      -0.0177             -0.103  
##  8 EleutherAI/pyth…     -1.98  2.07e-2   0.886      -0.0298              0.464  
##  9 allenai/OLMo-2-…     -1.98  2.18e-2   0.883       0.102               2.32   
## 10 google/gemma-2b…     -1.89  1.06e-1   0.745      -0.106               0.0311 
## # ℹ 31 more rows
```

``` r
summary(results_by_model_path$LRT_stat)
```

```
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max. 
## 7.770e-05 1.949e-01 2.381e+00 6.400e+00 1.337e+01 2.135e+01
```

``` r
summary(results_by_model_path$condition_coef)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
## -6.9767 -2.9962 -0.1059 -1.5648  0.1018  0.7203
```

``` r
summary(results_by_model_path$knowledge_cue_coef)
```

```
##     Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
## -9.28771 -2.16395 -0.87006 -1.49007 -0.06634  2.93665
```

``` r
### TODO: Should we adjust? What hypothesis are we testing?
results_by_model_path$p_adj = p.adjust(results_by_model_path$p_value, method = "holm")
results_by_model_path = results_by_model_path %>%
  mutate(sig = p_adj < .05)
mean(results_by_model_path$sig)
```

```
## [1] 0.3414634
```

``` r
results_by_model_path %>%
  filter(sig == TRUE) %>%
  select(model_path, LRT_stat, p_adj, condition_coef)
```

```
## # A tibble: 14 × 4
##    model_path                       LRT_stat    p_adj condition_coef
##    <chr>                               <dbl>    <dbl>          <dbl>
##  1 Qwen/Qwen2.5-14B                     13.5 0.00763           -3.00
##  2 Qwen/Qwen2.5-32B                     17.1 0.00128           -2.57
##  3 Qwen/Qwen2.5-32B-Instruct            12.2 0.0135            -3.25
##  4 allenai/OLMo-2-0325-32B              17.2 0.00127           -2.67
##  5 allenai/OLMo-2-0325-32B-DPO          20.9 0.000191          -4.66
##  6 allenai/OLMo-2-0325-32B-Instruct     20.3 0.000262          -4.72
##  7 allenai/OLMo-2-0325-32B-SFT          21.4 0.000157          -2.69
##  8 allenai/OLMo-2-1124-13B              14.5 0.00482           -2.93
##  9 allenai/OLMo-2-1124-13B-DPO          13.4 0.00794           -6.32
## 10 allenai/OLMo-2-1124-13B-Instruct     14.1 0.00576           -6.98
## 11 allenai/OLMo-2-1124-13B-SFT          13.1 0.00894           -3.28
## 12 allenai/OLMo-2-1124-7B-DPO           15.8 0.00244           -4.90
## 13 allenai/OLMo-2-1124-7B-Instruct      16.4 0.00184           -5.38
## 14 allenai/OLMo-2-1124-7B-SFT           11.9 0.0155            -2.18
```


All models together:


``` r
### Mixed models
mod_full = lmer(data = df_all_models,
                log_odds ~ condition + knowledge_cue + first_mention + recent_mention + 
                  (1 + condition | model_path) + (1 + condition | start),
                REML = FALSE)

mod_reduced = lmer(data = df_all_models,
                log_odds ~ knowledge_cue + first_mention + recent_mention + 
                  (1 + condition | model_path) + (1 + condition | start),
                REML = FALSE)

summary(mod_full)
```

```
## Linear mixed model fit by maximum likelihood . t-tests use Satterthwaite's
##   method [lmerModLmerTest]
## Formula: 
## log_odds ~ condition + knowledge_cue + first_mention + recent_mention +  
##     (1 + condition | model_path) + (1 + condition | start)
##    Data: df_all_models
## 
##       AIC       BIC    logLik -2*log(L)  df.resid 
##   45909.0   45992.7  -22942.5   45885.0      7860 
## 
## Scaled residuals: 
##      Min       1Q   Median       3Q      Max 
## -10.2512  -0.4293  -0.0098   0.4312   6.5843 
## 
## Random effects:
##  Groups     Name                 Variance Std.Dev. Corr 
##  model_path (Intercept)           5.9203  2.4332        
##             conditionTrue Belief  4.2476  2.0610   -0.73
##  start      (Intercept)           0.7217  0.8495        
##             conditionTrue Belief  0.2557  0.5056   -0.01
##  Residual                        19.2075  4.3826        
## Number of obs: 7872, groups:  model_path, 41; start, 10
## 
## Fixed effects:
##                         Estimate Std. Error         df t value Pr(>|t|)    
## (Intercept)              1.30162    0.47865   44.40631   2.719 0.009299 ** 
## conditionTrue Belief    -1.57089    0.37353   42.66967  -4.205 0.000131 ***
## knowledge_cueImplicit   -1.49007    0.09879 7771.46284 -15.083  < 2e-16 ***
## first_mentionStart       0.16592    0.09879 7771.46284   1.679 0.093098 .  
## recent_mentionStart      0.31025    0.09879 7771.46286   3.140 0.001693 ** 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) cndtTB knwl_I frst_S
## condtnTrBlf -0.533                     
## knwldg_cImp -0.103  0.000              
## frst_mntnSt -0.103  0.000  0.000       
## rcnt_mntnSt -0.103  0.000  0.000  0.000
```

``` r
anova(mod_full, mod_reduced)
```

```
## Data: df_all_models
## Models:
## mod_reduced: log_odds ~ knowledge_cue + first_mention + recent_mention + (1 + condition | model_path) + (1 + condition | start)
## mod_full: log_odds ~ condition + knowledge_cue + first_mention + recent_mention + (1 + condition | model_path) + (1 + condition | start)
##             npar   AIC   BIC logLik -2*log(L)  Chisq Df Pr(>Chisq)    
## mod_reduced   11 45922 45998 -22950     45900                         
## mod_full      12 45909 45993 -22942     45885 14.779  1  0.0001209 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```


## Accuracy metric



``` r
df_all_models = df_all_models %>%
  mutate(correct = case_when(
    condition == "False Belief" & log_odds > 0 ~ TRUE,
    condition == "True Belief" & log_odds <= 0 ~ TRUE,
    TRUE ~ FALSE  # all other cases are incorrect
  ))



df_summ = df_all_models %>%
  group_by(model_path, model_shorthand, model_family,
           num_params, num_training_tokens, base_instruct) %>%
  summarise(mean_accuracy = mean(correct))
```

```
## `summarise()` has grouped output by 'model_path', 'model_shorthand',
## 'model_family', 'num_params', 'num_training_tokens'. You can override using the
## `.groups` argument.
```

``` r
df_summ %>%
  select(model_shorthand, mean_accuracy)
```

```
## Adding missing grouping variables: `model_path`, `model_family`, `num_params`,
## `num_training_tokens`
```

```
## # A tibble: 41 × 6
## # Groups:   model_path, model_shorthand, model_family, num_params,
## #   num_training_tokens [41]
##    model_path        model_family num_params num_training_tokens model_shorthand
##    <chr>             <chr>             <dbl>               <dbl> <chr>          
##  1 EleutherAI/pythi… Pythia          1.52e 9             3   e11 Pythia 1.4b    
##  2 EleutherAI/pythi… Pythia          1.20e10             3   e11 Pythia 12b     
##  3 EleutherAI/pythi… Pythia          3.92e 7             3   e11 Pythia 14m     
##  4 EleutherAI/pythi… Pythia          2.13e 8             3   e11 Pythia 160m    
##  5 EleutherAI/pythi… Pythia          1.08e 9             3   e11 Pythia 1b      
##  6 EleutherAI/pythi… Pythia          2.91e 9             3   e11 Pythia 2.8b    
##  7 EleutherAI/pythi… Pythia          5.06e 8             3   e11 Pythia 410m    
##  8 EleutherAI/pythi… Pythia          6.99e 9             3   e11 Pythia 6.9b    
##  9 EleutherAI/pythi… Pythia          9.56e 7             3   e11 Pythia 70m     
## 10 Qwen/Qwen2.5-0.5B Qwen 2.5        4.94e 8             1.80e13 Qwen 2.5 0.5b  
## # ℹ 31 more rows
## # ℹ 1 more variable: mean_accuracy <dbl>
```

``` r
mean(df_all_models$correct)
```

```
## [1] 0.5647866
```

``` r
df_summ %>%
  ungroup() %>%
  arrange(desc(mean_accuracy)) %>%
  select(model_shorthand, mean_accuracy) %>%
  head(5)
```

```
## # A tibble: 5 × 2
##   model_shorthand      mean_accuracy
##   <chr>                        <dbl>
## 1 Olmo 2 13b Dpo               0.745
## 2 Olmo 2 13b Instruct          0.745
## 3 Olmo 2 13b Sft               0.734
## 4 Olmo 2 13b                   0.698
## 5 Qwen 2.5 7b Instruct         0.677
```

``` r
### "Wisdom of the crowd"?
df_lo_avg = df_all_models %>%
  group_by(passage, condition) %>%
  summarise(m_lo = mean(log_odds)) %>%
  mutate(correct = case_when(
    condition == "False Belief" & m_lo > 0 ~ TRUE,
    condition == "True Belief" & m_lo <= 0 ~ TRUE,
    TRUE ~ FALSE  # all other cases are incorrect
  )) 
```

```
## `summarise()` has grouped output by 'passage'. You can override using the
## `.groups` argument.
```

``` r
mean(df_lo_avg$correct)
```

```
## [1] 0.7083333
```

``` r
df_summ %>%
  ggplot(aes(x = num_params,
             y = mean_accuracy,
             color = model_family,
             shape = base_instruct)) +
  geom_point(size = 6,
             alpha = .5) +
  geom_hline(yintercept = .83,##TODO: Calculate from scratch
             linetype = "dotted", color = "red",
             size = 1.2, alpha = .8) + 
  geom_hline(yintercept = .5, linetype = "dotted",
             size = 1.2, alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  scale_y_continuous(limits = c(0, 1)) +
  labs(x = "#Parameters (Log10)",
       y = "Accuracy",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

```
## Warning: Using `size` aesthetic for lines was deprecated in ggplot2 3.4.0.
## ℹ Please use `linewidth` instead.
## This warning is displayed once every 8 hours.
## Call `lifecycle::last_lifecycle_warnings()` to see where this warning was
## generated.
```

![](fb_analysis_files/figure-html/accuracy-1.pdf)<!-- -->

``` r
df_summ %>%
  ggplot(aes(x = num_training_tokens,
             y = mean_accuracy,
             color = model_family,
             shape = base_instruct)) +
  geom_point(size = 6,
             alpha = .5) +
  geom_hline(yintercept = .83,##TODO: Calculate from scratch
             linetype = "dotted", color = "red",
             size = 1.2, alpha = .8) + 
  geom_hline(yintercept = .5, linetype = "dotted",
             size = 1.2, alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  scale_y_continuous(limits = c(0, 1)) +
  labs(x = "#Training Tokens",
       y = "Accuracy",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

![](fb_analysis_files/figure-html/accuracy-2.pdf)<!-- -->

``` r
### How do model properties predict the probability of a correct response?
mod_full = glmer(data = df_all_models,
                 correct ~ condition + knowledge_cue  +
                   log10(num_params) + log10(num_training_tokens) + 
                  base_instruct + first_mention + recent_mention +
                   (1 | start) + (1|model_family), 
                 family = binomial())
summary(mod_full)
```

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: 
## correct ~ condition + knowledge_cue + log10(num_params) + log10(num_training_tokens) +  
##     base_instruct + first_mention + recent_mention + (1 | start) +  
##     (1 | model_family)
##    Data: df_all_models
## 
##       AIC       BIC    logLik -2*log(L)  df.resid 
##   10654.8   10724.5   -5317.4   10634.8      7862 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -1.5716 -1.0860  0.7269  0.8654  1.3736 
## 
## Random effects:
##  Groups       Name        Variance Std.Dev.
##  start        (Intercept) 0.01518  0.1232  
##  model_family (Intercept) 0.02804  0.1674  
## Number of obs: 7872, groups:  start, 10; model_family, 5
## 
## Fixed effects:
##                            Estimate Std. Error z value Pr(>|z|)    
## (Intercept)                -2.14519    1.55244  -1.382    0.167    
## conditionTrue Belief       -0.01479    0.04596  -0.322    0.748    
## knowledge_cueImplicit       0.03590    0.04596   0.781    0.435    
## log10(num_params)           0.28249    0.04014   7.037 1.96e-12 ***
## log10(num_training_tokens) -0.03072    0.12673  -0.242    0.808    
## base_instructInstruct       0.05350    0.05550   0.964    0.335    
## first_mentionStart         -0.03379    0.04596  -0.735    0.462    
## recent_mentionStart        -0.06336    0.04596  -1.379    0.168    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) cndtTB knwl_I l10(_) l10(__ bs_nsI frst_S
## condtnTrBlf -0.015                                          
## knwldg_cImp -0.015  0.000                                   
## lg10(nm_pr)  0.014 -0.001  0.001                            
## lg10(nm_t_) -0.969  0.000  0.000 -0.253                     
## bs_nstrctIn  0.123  0.000  0.000  0.010 -0.137              
## frst_mntnSt -0.015  0.000  0.000 -0.001  0.000  0.000       
## rcnt_mntnSt -0.014  0.000  0.000 -0.002  0.000  0.000  0.000
```

``` r
### Plot coefficients
df_coef <- broom.mixed::tidy(mod_full, effects = "fixed") %>%
  mutate(term = forcats::fct_reorder(term, estimate))


df_coef %>%
  filter(term != "(Intercept)") %>%
  ggplot(aes(x = term, y = estimate)) +
  geom_point() +
  geom_errorbar(aes(ymin = estimate - std.error, ymax = estimate + std.error),
                width = 0.2) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "gray40") +
  coord_flip() +
  labs(
    x = NULL, y = "Coefficient Estimate",
  ) +
  theme_minimal(base_size = 12)
```

![](fb_analysis_files/figure-html/accuracy-3.pdf)<!-- -->

``` r
write.csv(df_summ, "../../data/processed/summaries/fb_summary.csv")


### Using accuracy instead of binary correct/incorrect response

### Just individual predictors
summary(lm(data = df_summ,
           mean_accuracy ~ log10(num_params)))
```

```
## 
## Call:
## lm(formula = mean_accuracy ~ log10(num_params), data = df_summ)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.13135 -0.04897 -0.01824  0.03822  0.13639 
## 
## Coefficients:
##                   Estimate Std. Error t value Pr(>|t|)    
## (Intercept)       -0.20770    0.13983  -1.485    0.146    
## log10(num_params)  0.08051    0.01453   5.539 2.26e-06 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.06515 on 39 degrees of freedom
## Multiple R-squared:  0.4403,	Adjusted R-squared:  0.4259 
## F-statistic: 30.68 on 1 and 39 DF,  p-value: 2.261e-06
```

``` r
summary(lm(data = df_summ,
           mean_accuracy ~ log10(num_training_tokens)))
```

```
## 
## Call:
## lm(formula = mean_accuracy ~ log10(num_training_tokens), data = df_summ)
## 
## Residuals:
##       Min        1Q    Median        3Q       Max 
## -0.129295 -0.071585 -0.002279  0.048207  0.176399 
## 
## Coefficients:
##                            Estimate Std. Error t value Pr(>|t|)  
## (Intercept)                 0.05641    0.25077   0.225   0.8232  
## log10(num_training_tokens)  0.04032    0.01986   2.030   0.0492 *
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.08282 on 39 degrees of freedom
## Multiple R-squared:  0.09556,	Adjusted R-squared:  0.07237 
## F-statistic: 4.121 on 1 and 39 DF,  p-value: 0.04922
```

``` r
summary(lm(data = df_summ,
           mean_accuracy ~ base_instruct))
```

```
## 
## Call:
## lm(formula = mean_accuracy ~ base_instruct, data = df_summ)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.11563 -0.06746 -0.01017  0.06146  0.16171 
## 
## Coefficients:
##                       Estimate Std. Error t value Pr(>|t|)    
## (Intercept)            0.53621    0.01784  30.058   <2e-16 ***
## base_instructInstruct  0.05858    0.02554   2.294   0.0273 *  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.08175 on 39 degrees of freedom
## Multiple R-squared:  0.1188,	Adjusted R-squared:  0.09626 
## F-statistic:  5.26 on 1 and 39 DF,  p-value: 0.02729
```

``` r
### All together
summary(lm(data = df_summ,
           mean_accuracy ~ log10(num_params) + log10(num_training_tokens) + base_instruct))
```

```
## 
## Call:
## lm(formula = mean_accuracy ~ log10(num_params) + log10(num_training_tokens) + 
##     base_instruct, data = df_summ)
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -0.11246 -0.05102 -0.01146  0.04487  0.12404 
## 
## Coefficients:
##                             Estimate Std. Error t value Pr(>|t|)    
## (Intercept)                -0.107031   0.222648  -0.481    0.634    
## log10(num_params)           0.076875   0.016596   4.632 4.37e-05 ***
## log10(num_training_tokens) -0.006345   0.018539  -0.342    0.734    
## base_instructInstruct       0.029058   0.022563   1.288    0.206    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.06544 on 37 degrees of freedom
## Multiple R-squared:  0.4644,	Adjusted R-squared:  0.4209 
## F-statistic: 10.69 on 3 and 37 DF,  p-value: 3.347e-05
```



# Comparison to human baseline

## Load human data


``` r
df_human = read_csv("../../data/processed/human/human_fb_cleaned.csv") %>%
  select(participant_id, item_id, passage,
         is_correct, is_start, is_end,
         reaction_time, condition, response, first_mention, recent_mention, knowledge_cue)
```

```
## New names:
## Rows: 613 Columns: 51
## ── Column specification
## ──────────────────────────────────────────────────────── Delimiter: "," chr
## (26): item_id, item_type, correct_answer, response, condition, first_men... dbl
## (21): ...1, id, participant_id, item, trial_index, reaction_time, trial_... lgl
## (4): is_correct, is_start, is_end, excluded.attention
## ℹ Use `spec()` to retrieve the full column specification for this data. ℹ
## Specify the column types or set `show_col_types = FALSE` to quiet this message.
## • `` -> `...1`
```

``` r
mean(df_human$is_correct)
```

```
## [1] 0.8270799
```

``` r
df_by_item = df_human %>%
  group_by(condition, passage, knowledge_cue) %>%
  summarise(p_start = mean(is_start) + .0001,
            p_end = mean(is_end) + .0001) %>%
  mutate(log_odds = log((p_start / p_end))) %>%
  mutate(model_shorthand = "Human") %>%
  mutate(correct = case_when(
    condition == "False Belief" & log_odds > 0 ~ TRUE,
    condition == "True Belief" & log_odds <= 0 ~ TRUE,
    TRUE ~ FALSE  # all other cases are incorrect
  ))
```

```
## `summarise()` has grouped output by 'condition', 'passage'. You can override
## using the `.groups` argument.
```

``` r
### Mean using log-odds measure forh umans
mean(df_by_item$correct)
```

```
## [1] 0.8972973
```

``` r
### Merge
df_merged = df_all_models %>%
  bind_rows(df_by_item)
```


## Top-performing models


``` r
df_merged %>%
  filter(model_shorthand %in% c("Human",
                                "Olmo 2 13b Dpo",
                                "Olmo 2 13b Instruct",
                                "Olmo 2 13b Sft",
                                "Llama 3 70b Instruct",
                                "Olmo 2 13b")) %>%
  ggplot(aes(x = log_odds,
             y = model_shorthand,
             fill = condition)) +
  geom_density_ridges2(aes(height = ..density..), 
                       color=NA, 
                       scale=.85, 
                       # size=1, 
                       alpha = .8,
                       stat="density") +
  labs(x = "Log Odds (Start vs. End)",
       y = "",
       fill = "") +
  theme_minimal() +
  geom_vline(xintercept = 0, linetype = "dotted") +
  theme(
    legend.position = "bottom"
  ) + 
  theme(axis.title = element_text(size=rel(1.2)),
        axis.text = element_text(size = rel(1.2)),
        legend.text = element_text(size = rel(1.2)),
        legend.title = element_text(size = rel(1.2)),
        strip.text.x = element_text(size = rel(1.2))) +
    scale_fill_manual(values = viridisLite::viridis(2, option = "mako", 
                                                    begin = 0.8, end = 0.15)) +
  facet_wrap(~knowledge_cue) 
```

![](fb_analysis_files/figure-html/best_models-1.pdf)<!-- -->



## Correlation matrix


``` r
df_model_means = df_all_models %>%
  group_by(passage, condition, knowledge_cue) %>%
  summarise(log_odds = mean(log_odds)) %>%
  mutate(model_shorthand = "All Models")
```

```
## `summarise()` has grouped output by 'passage', 'condition'. You can override
## using the `.groups` argument.
```

``` r
df_wide <- df_merged %>%
  select(passage, model_shorthand, log_odds) %>%
  pivot_wider(names_from = model_shorthand, values_from = log_odds)

cor_matrix <- df_wide %>%
  select(-passage) %>%
  cor(use = "pairwise.complete.obs")

# Plot the correlation matrix
ggcorrplot(cor_matrix, 
           hc.order = FALSE,
           method = "square") +
  theme(
    axis.text.x = element_text(size = 6, angle = 45, hjust = 1),
    axis.text.y = element_text(size = 6)
  )
```

![](fb_analysis_files/figure-html/corr_matrix-1.pdf)<!-- -->

``` r
sort(cor_matrix["Human",])
```

```
##              Olmo 2 1b             Pythia 14m     Olmo 2 1b Instruct 
##          -4.992973e-02          -4.276445e-02          -4.245679e-02 
##              Pythia 1b          Olmo 2 1b Sft            Pythia 2.8b 
##          -4.031918e-02          -3.787642e-02          -3.594982e-02 
##          Olmo 2 1b Dpo          Qwen 2.5 0.5b            Pythia 6.9b 
##          -2.940477e-02          -2.780097e-04           8.817533e-05 
##             Gemma 1 2b    Llama 3 8b Instruct    Gemma 1 2b Instruct 
##           9.128841e-03           2.814842e-02           2.892354e-02 
##            Pythia 410m          Qwen 2.5 1.5b            Pythia 160m 
##           3.982029e-02           4.600132e-02           4.892553e-02 
##             Llama 3 8b             Pythia 12b             Pythia 70m 
##           5.204098e-02           7.143812e-02           7.703393e-02 
##            Pythia 1.4b Qwen 2.5 0.5b Instruct            Qwen 2.5 7b 
##           7.755252e-02           9.932982e-02           1.373892e-01 
##  Qwen 2.5 1.5 Instruct   Qwen 2.5 3b Instruct            Qwen 2.5 3b 
##           1.433560e-01           1.489277e-01           2.042285e-01 
##              Olmo 2 7b   Qwen 2.5 7b Instruct          Olmo 2 7b Sft 
##           2.684079e-01           2.813659e-01           3.151644e-01 
##           Qwen 2.5 14b  Qwen 2.5 14b Instruct  Qwen 2.5 32b Instruct 
##           3.196391e-01           3.249040e-01           3.385223e-01 
##           Qwen 2.5 32b          Olmo 2 7b Dpo     Olmo 2 7b Instruct 
##           3.550363e-01           3.816489e-01           3.902405e-01 
##         Olmo 2 32b Sft    Olmo 2 32b Instruct         Olmo 2 13b Sft 
##           4.736136e-01           4.865321e-01           4.867408e-01 
##             Olmo 2 13b         Olmo 2 32b Dpo             Olmo 2 32b 
##           4.899657e-01           4.926853e-01           4.940875e-01 
##    Olmo 2 13b Instruct         Olmo 2 13b Dpo                  Human 
##           5.081724e-01           5.083239e-01           1.000000e+00
```

``` r
### MDS - EXCLUDE HUMAN
# Remove Human from correlation matrix for MDS
cor_matrix_no_human <- cor_matrix[rownames(cor_matrix) != "Human", 
                                   colnames(cor_matrix) != "Human"]

# Convert correlation matrix to a dissimilarity matrix
dissimilarity <- as.dist(sqrt(1 - cor_matrix_no_human))

# Perform classical MDS
mds_result <- cmdscale(dissimilarity, k = 2)

# Put into a data frame for plotting
mds_df <- as.data.frame(mds_result)
colnames(mds_df) <- c("Dim1", "Dim2")
mds_df$model_shorthand <- rownames(mds_df)

mds_df = mds_df %>%
  inner_join(df_summ)
```

```
## Joining with `by = join_by(model_shorthand)`
```

``` r
cor(mds_df$Dim1, mds_df$mean_accuracy)
```

```
## [1] -0.8786899
```

``` r
cor(mds_df$Dim2, mds_df$mean_accuracy)
```

```
## [1] -0.03103448
```

``` r
mds_df = mds_df %>%
  inner_join(results_by_model_path)
```

```
## Joining with `by = join_by(model_path)`
```

``` r
# Identify top-performing models for labeling
top_n_models <- 5  # Adjust this number
top_models <- mds_df %>%
  filter(model_shorthand %in% c("Qwen 2.5 7b Instruct", "Olmo 2 13b Dpo")) %>% 
  pull(model_shorthand)

# Add a column to indicate if model should be labeled
mds_df <- mds_df %>%
  mutate(label_model = ifelse(model_shorthand %in% top_models, 
                               model_shorthand, 
                               NA))

# Plot with labels
ggplot(mds_df, aes(Dim1, Dim2, 
                   color = model_family,
                   size = mean_accuracy,
                   shape = base_instruct)) +
  geom_point(alpha = .5) +
  geom_text(aes(label = label_model), 
            size = 3, 
            hjust = -0.1, 
            vjust = 0,
            show.legend = FALSE) +
  theme_minimal() +
  labs(x = "MDS 1",
       y = "MDS 2",
       color = "") +
  theme(text = element_text(size = 15),
        legend.position = "bottom") +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                   begin = 0.8, end = 0.15)) +
  guides(size = "none",      # Remove size legend
         shape = "none")
```

```
## Warning: Removed 39 rows containing missing values or values outside the scale range
## (`geom_text()`).
```

![](fb_analysis_files/figure-html/corr_matrix-2.pdf)<!-- -->

``` r
# Convert correlation matrix to long format
# Just extract the Human row/column directly
human_cors <- data.frame(
  model_shorthand = names(cor_matrix["Human", ]),
  correlation = cor_matrix["Human", ]
) %>%
  filter(model_shorthand != "Human") %>%
  arrange(desc(correlation))

rownames(human_cors) <- NULL

human_cors = human_cors %>%
  mutate(r2 = correlation ** 2)

summary(human_cors$r2)
```

```
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max. 
## 8.000e-09 1.803e-03 1.888e-02 7.538e-02 1.261e-01 2.584e-01
```

``` r
human_cors %>%
  head(3)
```

```
##       model_shorthand correlation        r2
## 1      Olmo 2 13b Dpo   0.5083239 0.2583932
## 2 Olmo 2 13b Instruct   0.5081724 0.2582391
## 3          Olmo 2 32b   0.4940875 0.2441224
```

``` r
human_cors = human_cors %>%
  inner_join(df_summ) 
```

```
## Joining with `by = join_by(model_shorthand)`
```

``` r
human_cors %>%
  ggplot(aes(x = num_params,
             y = r2,
             color = model_family,
             shape = base_instruct)) +
  geom_point(size = 6,
             alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  labs(x = "#Parameters (Log10)",
       y = "R2",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

![](fb_analysis_files/figure-html/corr_matrix-3.pdf)<!-- -->

``` r
mod_ppp = lm(data = human_cors,
               r2 ~ # mean_accuracy + 
                 log10(num_params) + log10(num_training_tokens)+ base_instruct)

summary(mod_ppp)
```

```
## 
## Call:
## lm(formula = r2 ~ log10(num_params) + log10(num_training_tokens) + 
##     base_instruct, data = human_cors)
## 
## Residuals:
##       Min        1Q    Median        3Q       Max 
## -0.119500 -0.050291 -0.008523  0.041559  0.136239 
## 
## Coefficients:
##                            Estimate Std. Error t value Pr(>|t|)    
## (Intercept)                -0.56173    0.23229  -2.418   0.0206 *  
## log10(num_params)           0.09247    0.01732   5.340 4.91e-06 ***
## log10(num_training_tokens) -0.02141    0.01934  -1.107   0.2756    
## base_instructInstruct       0.04046    0.02354   1.719   0.0940 .  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.06827 on 37 degrees of freedom
## Multiple R-squared:  0.5192,	Adjusted R-squared:  0.4802 
## F-statistic: 13.32 on 3 and 37 DF,  p-value: 4.768e-06
```


## Baselines analysis

First, merge with raw human data.


``` r
df_human_shortened = df_human %>%
  # mutate(human_is_start = is_start) %>%
  select(participant_id, item_id, passage, condition, knowledge_cue, 
         is_start, reaction_time)

df_all_models_with_human = df_all_models %>%
  inner_join(df_human_shortened)
```

```
## Joining with `by = join_by(passage, knowledge_cue, condition)`
```

```
## Warning in inner_join(., df_human_shortened): Detected an unexpected many-to-many relationship between `x` and `y`.
## ℹ Row 1 of `x` matches multiple rows in `y`.
## ℹ Row 102 of `y` matches multiple rows in `x`.
## ℹ If a many-to-many relationship is expected, set `relationship =
##   "many-to-many"` to silence this warning.
```

``` r
table(df_all_models_with_human$model_path)
```

```
## 
##             allenai/OLMo-2-0325-32B         allenai/OLMo-2-0325-32B-DPO 
##                                 613                                 613 
##    allenai/OLMo-2-0325-32B-Instruct         allenai/OLMo-2-0325-32B-SFT 
##                                 613                                 613 
##              allenai/OLMo-2-0425-1B          allenai/OLMo-2-0425-1B-DPO 
##                                 613                                 613 
##     allenai/OLMo-2-0425-1B-Instruct          allenai/OLMo-2-0425-1B-SFT 
##                                 613                                 613 
##             allenai/OLMo-2-1124-13B         allenai/OLMo-2-1124-13B-DPO 
##                                 613                                 613 
##    allenai/OLMo-2-1124-13B-Instruct         allenai/OLMo-2-1124-13B-SFT 
##                                 613                                 613 
##              allenai/OLMo-2-1124-7B          allenai/OLMo-2-1124-7B-DPO 
##                                 613                                 613 
##     allenai/OLMo-2-1124-7B-Instruct          allenai/OLMo-2-1124-7B-SFT 
##                                 613                                 613 
##              EleutherAI/pythia-1.4b               EleutherAI/pythia-12b 
##                                 613                                 613 
##               EleutherAI/pythia-14m              EleutherAI/pythia-160m 
##                                 613                                 613 
##                EleutherAI/pythia-1b              EleutherAI/pythia-2.8b 
##                                 613                                 613 
##              EleutherAI/pythia-410m              EleutherAI/pythia-6.9b 
##                                 613                                 613 
##               EleutherAI/pythia-70m                     google/gemma-2b 
##                                 613                                 613 
##                  google/gemma-2b-it          meta-llama/Meta-Llama-3-8B 
##                                 613                                 613 
## meta-llama/Meta-Llama-3-8B-Instruct                   Qwen/Qwen2.5-0.5B 
##                                 613                                 613 
##          Qwen/Qwen2.5-0.5B-Instruct                   Qwen/Qwen2.5-1.5B 
##                                 613                                 613 
##          Qwen/Qwen2.5-1.5B-Instruct                    Qwen/Qwen2.5-14B 
##                                 613                                 613 
##           Qwen/Qwen2.5-14B-Instruct                    Qwen/Qwen2.5-32B 
##                                 613                                 613 
##           Qwen/Qwen2.5-32B-Instruct                     Qwen/Qwen2.5-3B 
##                                 613                                 613 
##            Qwen/Qwen2.5-3B-Instruct                     Qwen/Qwen2.5-7B 
##                                 613                                 613 
##            Qwen/Qwen2.5-7B-Instruct 
##                                 613
```

Now, fit a baselines model for each LLM.



``` r
fit_compare_glmer_by_model <- function(df) {
  if (n_distinct(df$is_start) < 2) return(NULL)  # skip degenerate cases

  # Fit full model
  mod_full <- tryCatch(
    glmer(is_start ~ condition + knowledge_cue + 
            first_mention + recent_mention + log_odds +
            (1 | item_id),
          data = df,
          family = binomial()),
    error = function(e) NULL
  )

  # Fit reduced model (no condition)
  mod_reduced <- tryCatch(
    glmer(is_start ~ knowledge_cue + 
            first_mention + recent_mention + log_odds +
            (1 | item_id),
          data = df,
          family = binomial()),
    error = function(e) NULL
  )

  if (is.null(mod_full) || is.null(mod_reduced)) return(NULL)

  # Model comparison (Likelihood Ratio Test)
  anova_result <- anova(mod_reduced, mod_full)
  lrt_stat <- anova_result$Chisq[2]
  p_val <- anova_result$`Pr(>Chisq)`[2]
  delta_aic <- AIC(mod_reduced) - AIC(mod_full)

  # Extract coefficient for log_odds
  log_odds_coef <- tryCatch({
    fixef(mod_full)["log_odds"]
  }, error = function(e) NA)

  tibble(
    model_shorthand = unique(df$model_shorthand),
    delta_AIC = delta_aic,
    LRT_stat = lrt_stat,
    p_value = p_val,
    log_odds_coef = log_odds_coef,
    knowledge_cue_coef = fixef(mod_full)["knowledge_cueImplicit"],
    condition_coef = fixef(mod_full)["conditionTrue Belief"],
    
  )
}

# Apply across model_shorthand groups
glmer_model_comparisons <- df_all_models_with_human %>%
  group_by(model_shorthand) %>%
  group_split() %>%
  map_dfr(fit_compare_glmer_by_model)

glmer_model_comparisons
```

```
## # A tibble: 41 × 7
##    model_shorthand  delta_AIC LRT_stat  p_value log_odds_coef knowledge_cue_coef
##    <chr>                <dbl>    <dbl>    <dbl>         <dbl>              <dbl>
##  1 Gemma 1 2b            190.     192. 1.14e-43      -0.0135              -0.968
##  2 Gemma 1 2b Inst…      191.     193. 9.00e-44       0.00616             -0.944
##  3 Llama 3 8b            192.     194. 3.34e-44       0.108               -0.970
##  4 Llama 3 8b Inst…      191.     193. 8.46e-44       0.0468              -0.958
##  5 Olmo 2 13b            138.     140. 2.82e-32      -0.00482             -0.980
##  6 Olmo 2 13b Dpo        133.     135. 2.67e-31       0.00328             -0.941
##  7 Olmo 2 13b Inst…      133.     135. 3.36e-31       0.00217             -0.947
##  8 Olmo 2 13b Sft        139.     141. 1.71e-32      -0.00578             -0.982
##  9 Olmo 2 1b             188.     190. 2.68e-43      -0.00367             -0.963
## 10 Olmo 2 1b Dpo         190.     192. 1.19e-43      -0.00200             -0.956
## # ℹ 31 more rows
## # ℹ 1 more variable: condition_coef <dbl>
```

``` r
summary(glmer_model_comparisons$log_odds_coef)
```

```
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max. 
## -0.115835 -0.020611  0.003283  0.009687  0.043815  0.124516
```

``` r
summary(glmer_model_comparisons$knowledge_cue_coef)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
## -1.0776 -0.9865 -0.9626 -0.9522 -0.9242 -0.7799
```

``` r
summary(glmer_model_comparisons$condition_coef)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  -3.751  -3.606  -3.584  -3.558  -3.560  -3.274
```

``` r
summary(glmer_model_comparisons$LRT_stat)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   123.6   165.9   190.3   175.7   192.5   195.4
```


## PPP Analysis


``` r
fit_ppp_by_model <- function(df) {

  # Fit full model
  mod_full <- tryCatch(
    glmer(is_start ~ log_odds+first_mention + recent_mention + condition +
            (1 | item_id),
          data = df,
          family = binomial()),
    error = function(e) NULL
  )

  # Extract coefficient for log_odds
  log_odds_coef <- tryCatch({
    fixef(mod_full)["log_odds"]
  }, error = function(e) NA)

  tibble(
    model_shorthand = unique(df$model_shorthand),
    AIC = AIC(mod_full),
    log_odds_coef = fixef(mod_full)["log_odds"]
  )
}

# Apply across model_shorthand groups
ppp_models <- df_all_models_with_human %>%
  group_by(model_shorthand) %>%
  group_split() %>%
  map_dfr(fit_ppp_by_model) %>%
  inner_join(df_model_properties)
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Model failed to converge with max|grad| = 0.022669 (tol = 0.002, component 1)
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Model failed to converge with max|grad| = 0.0234677 (tol = 0.002, component 1)
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Model failed to converge with max|grad| = 0.0227791 (tol = 0.002, component 1)
```

```
## Joining with `by = join_by(model_shorthand)`
```

``` r
mod_base <- glmer(is_start ~ first_mention + recent_mention + condition + # log_odds+
          (1 | item_id),
        data = filter(df_all_models_with_human, model_shorthand == "Qwen 2.5 7b Instruct"),
        family = binomial())
  
### Rescale AIC
ppp_models = ppp_models %>%
  mutate(delta_AIC = AIC - AIC(mod_base))

summary(ppp_models$delta_AIC)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
## -7.9956 -3.5355  0.5292 -0.9230  1.7039  1.9997
```

``` r
ppp_models %>%
  arrange(delta_AIC) %>%
  head(5)
```

```
## # A tibble: 5 × 8
##   model_shorthand      AIC log_odds_coef model_path     num_params base_instruct
##   <chr>              <dbl>         <dbl> <chr>               <dbl> <chr>        
## 1 Olmo 2 7b Instruct  541.        0.0491 allenai/OLMo-…    7.30e 9 Instruct     
## 2 Olmo 2 7b Dpo       541.        0.0512 allenai/OLMo-…    7.30e 9 Instruct     
## 3 Olmo 2 32b          544.        0.169  allenai/OLMo-…    3.22e10 Base         
## 4 Olmo 2 32b Sft      544.        0.154  allenai/OLMo-…    3.22e10 Instruct     
## 5 Olmo 2 13b          545.        0.109  allenai/OLMo-…    1.37e10 Base         
## # ℹ 2 more variables: model_family <chr>, delta_AIC <dbl>
```

``` r
### Add back to original data
ppp_with_accuracy = ppp_models %>%
  select(model_shorthand, delta_AIC) %>%
  inner_join(df_summ)
```

```
## Joining with `by = join_by(model_shorthand)`
```

``` r
ppp_with_accuracy %>%
  ggplot(aes(x = num_training_tokens,
             y = delta_AIC,
             color = model_family,
             shape = base_instruct)) +
  geom_point(size = 6,
             alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  labs(x = "#Training Tokens",
       y = "Delta AIC",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

![](fb_analysis_files/figure-html/ppp-1.pdf)<!-- -->

``` r
ppp_with_accuracy %>%
  ggplot(aes(x = num_params,
             y = delta_AIC,
             color = model_family,
             shape = base_instruct)) +
  geom_point(size = 6,
             alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  labs(x = "#Parameters",
       y = "Delta AIC",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

![](fb_analysis_files/figure-html/ppp-2.pdf)<!-- -->

``` r
### Among models that >50% accuracy, better models explain more variance in human data
ppp_with_accuracy %>%
  ggplot(aes(x = mean_accuracy,
             y = delta_AIC,
             color = model_family,
             shape = base_instruct)) +
  geom_point(size = 6,
             alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  labs(x = "Accuracy",
       y = "Delta AIC",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

![](fb_analysis_files/figure-html/ppp-3.pdf)<!-- -->

``` r
mod_ppp = lm(data = ppp_with_accuracy,
               delta_AIC ~ 
                 log10(num_params) + log10(num_training_tokens)+ base_instruct )

summary(mod_ppp)
```

```
## 
## Call:
## lm(formula = delta_AIC ~ log10(num_params) + log10(num_training_tokens) + 
##     base_instruct, data = ppp_with_accuracy)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -5.5455 -1.1864  0.0928  2.0845  4.0856 
## 
## Coefficients:
##                            Estimate Std. Error t value Pr(>|t|)  
## (Intercept)                  1.0001     9.0424   0.111   0.9126  
## log10(num_params)           -1.2979     0.6747  -1.924   0.0625 .
## log10(num_training_tokens)   0.9268     0.7550   1.227   0.2278  
## base_instructInstruct       -2.3277     0.9404  -2.475   0.0183 *
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.645 on 35 degrees of freedom
## Multiple R-squared:  0.2557,	Adjusted R-squared:  0.1919 
## F-statistic: 4.009 on 3 and 35 DF,  p-value: 0.0149
```


## Knowledge cue


``` r
mod_full = glmer(is_start ~ condition + knowledge_cue + 
          first_mention + recent_mention +
          (1 + knowledge_cue | item_id),
        data = df_human,
        family = binomial())
```

```
## boundary (singular) fit: see help('isSingular')
```

``` r
mod_no_kc = glmer(is_start ~ condition + # knowledge_cue + 
          first_mention + recent_mention +
          (1+ knowledge_cue  | item_id),
        data = df_human,
        family = binomial())
```

```
## boundary (singular) fit: see help('isSingular')
```

``` r
anova(mod_full, mod_no_kc)
```

```
## Data: df_human
## Models:
## mod_no_kc: is_start ~ condition + first_mention + recent_mention + (1 + knowledge_cue | item_id)
## mod_full: is_start ~ condition + knowledge_cue + first_mention + recent_mention + (1 + knowledge_cue | item_id)
##           npar    AIC    BIC  logLik -2*log(L)  Chisq Df Pr(>Chisq)    
## mod_no_kc    7 549.91 580.84 -267.96    535.91                         
## mod_full     8 535.80 571.15 -259.90    519.80 16.109  1  5.981e-05 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

``` r
summary(mod_full)
```

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: 
## is_start ~ condition + knowledge_cue + first_mention + recent_mention +  
##     (1 + knowledge_cue | item_id)
##    Data: df_human
## 
##       AIC       BIC    logLik -2*log(L)  df.resid 
##     535.8     571.2    -259.9     519.8       605 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -4.7709 -0.5173  0.2116  0.3270  2.4639 
## 
## Random effects:
##  Groups  Name                  Variance Std.Dev. Corr
##  item_id (Intercept)           0.0000   0.0000       
##          knowledge_cueImplicit 0.7148   0.8455    NaN
## Number of obs: 613, groups:  item_id, 185
## 
## Fixed effects:
##                       Estimate Std. Error z value Pr(>|z|)    
## (Intercept)             2.7950     0.3463   8.071 6.96e-16 ***
## conditionTrue Belief   -3.7802     0.3262 -11.589  < 2e-16 ***
## knowledge_cueImplicit  -1.0276     0.2670  -3.849 0.000119 ***
## first_mentionStart      0.0192     0.2419   0.079 0.936739    
## recent_mentionStart     0.3109     0.2443   1.272 0.203207    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) cndtTB knwl_I frst_S
## condtnTrBlf -0.721                     
## knwldg_cImp -0.549  0.374              
## frst_mntnSt -0.345 -0.019 -0.038       
## rcnt_mntnSt -0.322 -0.102  0.032  0.034
## optimizer (Nelder_Mead) convergence code: 0 (OK)
## boundary (singular) fit: see help('isSingular')
```

``` r
### Comopare to parameter estimate for LLMs, using binary outcome
df_all_models$is_start = df_all_models$log_odds > 0


coef_human <- fixef(mod_full)

# Create aligned dataframe
group_coefs <- tibble(
  model_path = c("Human"),
  knowledge_cue_coef = c(coef_human["knowledge_cueImplicit"]),
  condition_coef = c(coef_human["conditionTrue Belief"])
)

## Each model on its own
run_models_for_comparison <- function(df) {

  mod_full = glmer(is_start ~ condition + knowledge_cue + 
            first_mention + recent_mention +
            (1 + condition | start),
          data = df,
          family = binomial(),
          control = glmerControl(optimizer = "bobyqa"))
  
  # Extract coefficients
  coefs <- fixef(mod_full)
  cond_coef <- coefs[grep("^condition", names(coefs))]
  cue_coef <- coefs[grep("^knowledge_cue", names(coefs))]

  tibble(
    model_path = unique(df$model_path),
    condition_coef = cond_coef,
    knowledge_cue_coef = cue_coef
  )
}

# Apply to each model_path
results_by_model_path <- df_all_models %>%
  group_by(model_path) %>%
  group_split() %>%
  map_dfr(run_models_for_comparison)
```

```
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
## boundary (singular) fit: see help('isSingular')
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Hessian is numerically singular: parameters are not uniquely determined
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## unable to evaluate scaled gradient
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Model failed to converge: degenerate Hessian with 1 negative eigenvalues
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## unable to evaluate scaled gradient
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Hessian is numerically singular: parameters are not uniquely determined
```

``` r
all_coefs = results_by_model_path %>%
  select(model_path, knowledge_cue_coef, condition_coef) 

summary(all_coefs$knowledge_cue_coef)
```

```
##       Min.    1st Qu.     Median       Mean    3rd Qu.       Max. 
## -1.167e+01 -2.304e+00 -1.079e+00 -1.622e+00  1.700e-06  1.525e+00
```

``` r
sd(all_coefs$knowledge_cue_coef)
```

```
## [1] 2.741543
```

``` r
sd(all_coefs$knowledge_cue_coef)/sqrt(nrow(all_coefs))
```

```
## [1] 0.4281571
```

``` r
summary(all_coefs$condition_coef)
```

```
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max. 
## -25.82083  -3.62087  -1.12940  -2.50717   0.02743   4.86728
```

``` r
sd(all_coefs$condition_coef)
```

```
## [1] 4.848538
```

``` r
sd(all_coefs$condition_coef)/sqrt(nrow(all_coefs))
```

```
## [1] 0.7572143
```

``` r
### Percentile of human effect (KC)
percentile <- mean(all_coefs$knowledge_cue_coef >= -1.02) * 100
percentile
```

```
## [1] 48.78049
```

``` r
### Percentile of human effect (condition)
percentile <- mean(all_coefs$condition_coef >= -3.78) * 100
percentile
```

```
## [1] 75.60976
```

``` r
### Merge with other data
df_all_coefs = all_coefs %>%
  inner_join(df_summ)
```

```
## Joining with `by = join_by(model_path)`
```

``` r
summary(lm(data = df_all_coefs, knowledge_cue_coef ~ log10(num_params) +
             log10(num_training_tokens) + base_instruct))
```

```
## 
## Call:
## lm(formula = knowledge_cue_coef ~ log10(num_params) + log10(num_training_tokens) + 
##     base_instruct, data = df_all_coefs)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -8.9857 -0.5921  0.6298  1.2785  2.5312 
## 
## Coefficients:
##                            Estimate Std. Error t value Pr(>|t|)   
## (Intercept)                 9.68263    8.52952   1.135  0.26360   
## log10(num_params)          -2.04362    0.63580  -3.214  0.00271 **
## log10(num_training_tokens)  0.65717    0.71021   0.925  0.36080   
## base_instructInstruct       0.03709    0.86438   0.043  0.96601   
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 2.507 on 37 degrees of freedom
## Multiple R-squared:  0.2266,	Adjusted R-squared:  0.1639 
## F-statistic: 3.613 on 3 and 37 DF,  p-value: 0.02199
```

``` r
### Larger models show bigger effect
top_models <- df_all_coefs %>%
  filter(model_shorthand %in% c("Olmo 2 13b Dpo", "Olmo 2 13b")) %>% 
  pull(model_shorthand)

# Add a column to indicate if model should be labeled
df_all_coefs <- df_all_coefs %>%
  mutate(label_model = ifelse(model_shorthand %in% top_models, 
                               model_shorthand, 
                               NA))

df_all_coefs %>%
  ggplot(aes(x = num_params,
             y = knowledge_cue_coef,
             color = model_family,
             shape = base_instruct)) +
  geom_hline(yintercept = -1.02, color = "red",
             linetype = "dotted", size = 1.2, alpha = .5) +
  scale_x_log10() +
  geom_text_repel(aes(label = label_model), 
            size = 3, 
            hjust = -0.1, 
            vjust = 0,
            show.legend = FALSE) +
  theme_minimal() +
  geom_point(size = 6,
             alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  labs(x = "#Parameters (Log10)",
       y = "Parameter Estimate (Knowledge Cue)",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

```
## Scale for x is already present.
## Adding another scale for x, which will replace the existing scale.
```

```
## Warning: Removed 39 rows containing missing values or values outside the scale range
## (`geom_text_repel()`).
```

![](fb_analysis_files/figure-html/kc_epistemics-1.pdf)<!-- -->

``` r
df_all_coefs %>%
  ggplot(aes(x = num_params,
             y = condition_coef,
             color = model_family,
             shape = base_instruct)) +
  geom_hline(yintercept = -3.78, color = "red",
             linetype = "dotted", size = 1.2, alpha = .5) +
  scale_x_log10() +
  geom_text_repel(aes(label = label_model), 
            size = 3, 
            hjust = -0.1, 
            vjust = 0,
            show.legend = FALSE) +
  theme_minimal() +
  geom_point(size = 6,
             alpha = .5) +
  scale_x_log10() +
  # geom_text_repel(aes(label=model_shorthand), size=3) +
  labs(x = "#Parameters (Log10)",
       y = "Parameter Estimate (Knowledge State)",
       color = "",
       shape = "") +
  theme_minimal() +
  scale_color_manual(values = viridisLite::viridis(5, option = "mako", 
                                                  begin = 0.8, end = 0.15)) +
  theme(text = element_text(size = 15),
        legend.position="bottom") +
  guides(color = guide_legend(nrow = 2),     # Wrap colors
         shape = guide_legend(nrow = 2))     # Wrap shapes
```

```
## Scale for x is already present.
## Adding another scale for x, which will replace the existing scale.
```

```
## Warning: Removed 39 rows containing missing values or values outside the scale range
## (`geom_text_repel()`).
```

![](fb_analysis_files/figure-html/kc_epistemics-2.pdf)<!-- -->

``` r
df_all_coefs %>%
  ggplot(aes(x = knowledge_cue_coef,
             y = condition_coef,
             size = num_params)) +
  geom_point(alpha = .5) +
  geom_point(aes(x = -1.02, y = -3.78), color = "red") +
  annotate("text", x = -1.02, y = -3.78, label = "Human Estimate",
           hjust = .3, vjust = 1.5, color = "red", size = 4) +
  geom_vline(xintercept = 0, linetype = "dotted") +
  geom_hline(yintercept = 0, linetype = "dotted") +
  theme_minimal() +
  labs(x = "Parameter Estimate (Knowledge Cue)",
       y = "Parameter Estimate (Knowledge State)") + 
  theme(text = element_text(size = 15),
        legend.position="none") 
```

![](fb_analysis_files/figure-html/kc_epistemics-3.pdf)<!-- -->

``` r
#### Plot effect of KC across LMs
# Calculate mean Log Odds for each model and Knowledge Cue
df_by_kc <- df_all_models %>%
  group_by(model_path, knowledge_cue) %>%
  summarise(mean_start = mean(is_start),
            .groups = "drop")

# Calculate overall mean across all LMs
df_overall_mean <- df_all_models %>%
  group_by(knowledge_cue) %>%
  summarise(mean_start = mean(is_start),
            .groups = "drop") %>%
  mutate(model_path = "All LMs Mean")

df_human_mean = df_human %>%
  group_by(knowledge_cue) %>%
  summarise(mean_start = mean(is_start),
            .groups = "drop") %>%
  mutate(model_path = "Human")

# Plot
library(ggrepel)


# Add labels to the data
set.seed(1)
df_overall_mean <- df_overall_mean %>% mutate(label = "LLM Mean")
df_human_mean <- df_human_mean %>% mutate(label = "Human")
ggplot(df_by_kc, aes(x = knowledge_cue, y = mean_start)) +
  geom_jitter(width = 0.1, alpha = 0.3, size = 2, color = "gray40") +
  geom_point(data = df_overall_mean, 
             aes(x = knowledge_cue, y = mean_start),
             color = "#1f77b4", size = 5, shape = 18) +
  geom_text_repel(data = df_overall_mean,
                  aes(x = knowledge_cue, y = mean_start, label = label),
                  size = 4, color = "#1f77b4") +
  geom_point(data = df_human_mean, 
             aes(x = knowledge_cue, y = mean_start),
             color = "#d62728", size = 5, shape = 17) +
  geom_text_repel(data = df_human_mean,
                  aes(x = knowledge_cue, y = mean_start, label = label),
                  size = 4, color = "#d62728") +
  theme_minimal() +
  labs(x = "Knowledge Cue",
       y = "Proportion of Start Responses") +
  theme(text = element_text(size = 15))
```

![](fb_analysis_files/figure-html/kc_epistemics-4.pdf)<!-- -->

``` r
# Calculate human difference
df_human_diff <- df_human_mean %>%
  pivot_wider(names_from = knowledge_cue, values_from = mean_start) %>%
  mutate(diff = Explicit - Implicit)

human_diff <- df_human_diff$diff
# Calculate the difference for each model
df_kc_diff <- df_by_kc %>%
  pivot_wider(names_from = knowledge_cue, values_from = mean_start) %>%
  mutate(diff = Explicit - Implicit)  # Adjust these names to match your levels

# Calculate mean difference
mean_diff <- mean(df_kc_diff$diff)

# Plot the distribution of differences
ggplot(df_kc_diff, aes(x = diff)) +
  geom_histogram(aes(y = after_stat(density)), bins = 15, alpha = 0.4) +
  geom_density(color = "#1f77b4", linewidth = 1.2) +
  geom_vline(xintercept = mean_diff, color = "#1f77b4", linewidth = 1.5, linetype = "dashed") +
  geom_vline(xintercept = human_diff, color = "#d62728", linewidth = 1.5, linetype = "solid") +
  geom_vline(xintercept = 0, color = "black", linetype = "dotted") +
  annotate("text", x = mean_diff, y = Inf, label = "LLM Mean",
           hjust = -0.1, vjust = 1.5, color = "#1f77b4", size = 4) +
  annotate("text", x = human_diff, y = Inf, label = "Human",
           hjust = -0.1, vjust = 3, color = "#d62728", size = 4) +
  theme_minimal() +
  labs(x = "Difference in Proportion Start (Explicit - Implicit)",
       y = "Density") +
  theme(text = element_text(size = 15))
```

![](fb_analysis_files/figure-html/kc_epistemics-5.pdf)<!-- -->

``` r
#### Do this for condition
# Calculate mean Log Odds for each model andcondition
df_by_condition <- df_all_models %>%
  group_by(model_path, condition) %>%
  summarise(mean_start = mean(is_start),
            .groups = "drop")

# Calculate overall mean across all LMs
df_overall_mean <- df_all_models %>%
  group_by(condition) %>%
  summarise(mean_start = mean(is_start),
            .groups = "drop") %>%
  mutate(model_path = "All LMs Mean")

df_human_mean = df_human %>%
  group_by(condition) %>%
  summarise(mean_start = mean(is_start),
            .groups = "drop") %>%
  mutate(model_path = "Human")

# Plot
library(ggrepel)


# Add labels to the data
set.seed(1)
df_overall_mean <- df_overall_mean %>% mutate(label = "LLM Mean")
df_human_mean <- df_human_mean %>% mutate(label = "Human")
ggplot(df_by_condition, aes(x = condition, y = mean_start)) +
  geom_jitter(width = 0.1, alpha = 0.3, size = 2, color = "gray40") +
  geom_point(data = df_overall_mean, 
             aes(x = condition, y = mean_start),
             color = "#1f77b4", size = 5, shape = 18) +
  geom_text_repel(data = df_overall_mean,
                  aes(x = condition, y = mean_start, label = label),
                  size = 4, color = "#1f77b4") +
  geom_point(data = df_human_mean, 
             aes(x = condition, y = mean_start),
             color = "#d62728", size = 5, shape = 17) +
  geom_text_repel(data = df_human_mean,
                  aes(x = condition, y = mean_start, label = label),
                  size = 4, color = "#d62728") +
  theme_minimal() +
  labs(x = "Knowledge State",
       y = "Proportion of Start Responses") +
  theme(text = element_text(size = 15))
```

![](fb_analysis_files/figure-html/kc_epistemics-6.pdf)<!-- -->

``` r
# Calculate human difference
df_human_diff <- df_human_mean %>%
  pivot_wider(names_from = condition, values_from = mean_start) %>%
  mutate(diff = `False Belief` - `True Belief`)

human_diff <- df_human_diff$diff
# Calculate the difference for each model
df_cond_diff <- df_by_condition %>%
  pivot_wider(names_from = condition, values_from = mean_start) %>%
  mutate(diff = `False Belief` - `True Belief`)  # Adjust these names to match your levels

# Calculate mean difference
mean_diff <- mean(df_cond_diff$diff)

# Plot the distribution of differences
ggplot(df_cond_diff, aes(x = diff)) +
  geom_histogram(aes(y = after_stat(density)), bins = 15, alpha = 0.4) +
  geom_density(color = "#1f77b4", linewidth = 1.2) +
  geom_vline(xintercept = mean_diff, color = "#1f77b4", linewidth = 1.5, linetype = "dashed") +
  geom_vline(xintercept = human_diff, color = "#d62728", linewidth = 1.5, linetype = "solid") +
  geom_vline(xintercept = 0, color = "black", linetype = "dotted") +
  annotate("text", x = mean_diff, y = Inf, label = "LLM Mean",
           hjust = -0.1, vjust = 1.5, color = "#1f77b4", size = 4) +
  annotate("text", x = human_diff, y = Inf, label = "Human",
           hjust = 1.1, vjust = 3, color = "#d62728", size = 4) +
  theme_minimal() +
  labs(x = "Difference in Proportion Start (FB - TB)",
       y = "Density") +
  theme(text = element_text(size = 15))
```

![](fb_analysis_files/figure-html/kc_epistemics-7.pdf)<!-- -->

### Baselines analysis (knowledge cue)

Now, fit a baselines model for each LLM.



``` r
fit_compare_glmer_by_model <- function(df) {
  if (n_distinct(df$is_start) < 2) return(NULL)  # skip degenerate cases

  # Fit full model
  mod_full <- tryCatch(
    glmer(is_start ~ condition + knowledge_cue + 
            first_mention + recent_mention + log_odds +
            (1 | item_id),
          data = df,
          family = binomial()),
    error = function(e) NULL
  )

  # Fit reduced model (no condition)
  mod_reduced <- tryCatch(
    glmer(is_start ~ condition + 
            first_mention + recent_mention + log_odds +
            (1 | item_id),
          data = df,
          family = binomial()),
    error = function(e) NULL
  )

  if (is.null(mod_full) || is.null(mod_reduced)) return(NULL)

  # Model comparison (Likelihood Ratio Test)
  anova_result <- anova(mod_reduced, mod_full)
  lrt_stat <- anova_result$Chisq[2]
  p_val <- anova_result$`Pr(>Chisq)`[2]
  delta_aic <- AIC(mod_reduced) - AIC(mod_full)

  # Extract coefficient for log_odds
  log_odds_coef <- tryCatch({
    fixef(mod_full)["log_odds"]
  }, error = function(e) NA)

  tibble(
    model_shorthand = unique(df$model_shorthand),
    delta_AIC = delta_aic,
    LRT_stat = lrt_stat,
    p_value = p_val,
    log_odds_coef = log_odds_coef,
    knowledge_cue_coef = fixef(mod_full)["knowledge_cueImplicit"],
    condition_coef = fixef(mod_full)["conditionTrue Belief"],
    
  )
}

# Apply across model_shorthand groups
glmer_model_comparisons <- df_all_models_with_human %>%
  group_by(model_shorthand) %>%
  group_split() %>%
  map_dfr(fit_compare_glmer_by_model)
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Model failed to converge with max|grad| = 0.0226629 (tol = 0.002, component 1)
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Model failed to converge with max|grad| = 0.0234321 (tol = 0.002, component 1)
```

```
## Warning in checkConv(attr(opt, "derivs"), opt$par, ctrl = control$checkConv, :
## Model failed to converge with max|grad| = 0.0227752 (tol = 0.002, component 1)
```

``` r
glmer_model_comparisons
```

```
## # A tibble: 41 × 7
##    model_shorthand   delta_AIC LRT_stat p_value log_odds_coef knowledge_cue_coef
##    <chr>                 <dbl>    <dbl>   <dbl>         <dbl>              <dbl>
##  1 Gemma 1 2b            14.1     16.1  6.03e-5      -0.0135              -0.968
##  2 Gemma 1 2b Instr…     13.6     15.6  7.79e-5       0.00616             -0.944
##  3 Llama 3 8b            14.5     16.5  4.95e-5       0.108               -0.970
##  4 Llama 3 8b Instr…     14.3     16.3  5.44e-5       0.0468              -0.958
##  5 Olmo 2 13b             7.55     9.55 1.99e-3      -0.00482             -0.980
##  6 Olmo 2 13b Dpo         8.11    10.1  1.48e-3       0.00328             -0.941
##  7 Olmo 2 13b Instr…      8.24    10.2  1.37e-3       0.00217             -0.947
##  8 Olmo 2 13b Sft         8.96    11.0  9.29e-4      -0.00578             -0.982
##  9 Olmo 2 1b             14.0     16.0  6.28e-5      -0.00367             -0.963
## 10 Olmo 2 1b Dpo         12.5     14.5  1.37e-4      -0.00200             -0.956
## # ℹ 31 more rows
## # ℹ 1 more variable: condition_coef <dbl>
```

``` r
summary(glmer_model_comparisons$log_odds_coef)
```

```
##      Min.   1st Qu.    Median      Mean   3rd Qu.      Max. 
## -0.115835 -0.020611  0.003283  0.009687  0.043815  0.124516
```

``` r
summary(glmer_model_comparisons$knowledge_cue_coef)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
## -1.0776 -0.9865 -0.9626 -0.9522 -0.9242 -0.7799
```

``` r
summary(glmer_model_comparisons$condition_coef)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  -3.751  -3.606  -3.584  -3.558  -3.560  -3.274
```

``` r
summary(glmer_model_comparisons$LRT_stat)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   7.054  12.395  15.609  14.294  16.169  18.180
```

