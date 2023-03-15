# A function to test each completion
import evals.api

@evals.api.register_test
def test_incorrect_answer(prompt, completion):
  # Your logic here
  return True or False
