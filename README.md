# MINE Evaluation
Evaluates a given LLM's performance with kg-gen using MINE. 

Usage:
- Set your OPENAI_API_KEY environment variable (`export OPENAI_API_KEY="<your key here>"`)
- Run `generate_data.py`
- Run `kg-gen-repo/MINE/evaluation.py`
- Run `read_results.py`

Or simply run `run_all.sh` to do all of that for you (except for the api key part). 

## Results 
The kg-gen paper uses GPT-4o for its results. 
We can test any model supported by DSPy. 

<!-- 
This takes a long time to run! 
I have not included a time column becuase it froze my computer part-way through
but cached some results, which threw off the timing. 
Expect to wait for 14*105/60=24.5 minutes to generate results. 
And then 10*105/60=17.5 minutes for evaluation.
The rest is fast though!

With a larger dataset it may be better to save graphs immediately rather than 
holding them in memory until saving them in bulk. 
It could also be worth investigating using parallel llm requests. 
This would probably help with openAI models but may be unwise when using local 
models.
-->

| Model | Mean Accuracy (%) |
| - | - |
| openai/gpt-4o-mini | 36.38 | 
| openai/gpt-4o | 46.86\* |

\*
The kg-gen package as written throws errors when working with essays 61 and 78. 
This evaluation uses fixes found in https://github.com/stair-lab/kg-gen/pull/8. 

<!-- 
The paper result is 66.07% for GPT-4o. 
I am not sure why this is so much lower! 
-->
