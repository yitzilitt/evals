# A function to score the model's performance (optional)

import evals.api

@evals.api.register_metric
def score_incorrect_answers(prompts, completions):
  # Your logic here
  return score
