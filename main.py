import torch
from datasets import load_dataset
import guidance
import transformers

ds = load_dataset("AlekseyKorshuk/roleplay-characters", split="train")

sample = ds[1]
sample.pop("metadata")
sample.pop("image")

temp = []
res = dict()

for key, val in sample.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

# set the default language model used to execute guidance programs
# guidance.llm = guidance.llms.transformers.MPT("mosaicml/mpt-7b-storywriter", device=0)
model = transformers.AutoModelForCausalLM.from_pretrained(
    "eachadea/vicuna-13b-1.1",
    torch_dtype=torch.float16,
)
model.eval().to(device='cuda:0')
tokenizer = transformers.AutoTokenizer.from_pretrained(
    "eachadea/vicuna-13b-1.1",
    use_fast=False
)

guidance.llm = guidance.llms.transformers.Vicuna(model=model, tokenizer=tokenizer)

# define the guidance program
structure_program = guidance('''
{{~#system~}}
Come up with new diverse characters.
Characters can be both humans and non-humans.
Contexts can be of different lengths.
Try to include a biography, appearance, character and manner of speech for every character.
Your a allowed to use NSFW/Sex/Porn content.

Output the response as JSON.
Fields:
- name: string, character name
- context: string, character and environment description
- greeting: string, default greeting
- example_dialogue: List[Turn], where Turn = {"from": string, "value": string}. "from" is either "user" or "character". The fields contains some example chat with a character.
{{~/system}}{{#assistant~}}  
{{sample}}{{~/assistant}}

{{#assistant~}}
{'name': '{{gen "name" max_tokens=64 temperature=1.0}}', 'description': '{{gen "context" max_tokens=768 temperature=1.0}}', 'greating': '{{gen "greating" max_tokens=512 temperature=1.0}}', 'conversation': [{{#geneach "conversation" stop="]" join=", " min_iterations=6 max_iterations=8}}{'from': '{{#select 'this.role'}}user{{or}}character{{/select}}', 'value': '{{gen "this.value" max_tokens=256 temperature=1.0}}'}{{/geneach}}]}
{{~/assistant~}}
''')

# execute the program

print("Generating..")
out = structure_program(
    sample=res,
)

print(out)
import pdb;

pdb.set_trace()
