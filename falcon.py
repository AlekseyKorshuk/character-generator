import torch
from datasets import load_dataset
import guidance
import transformers

ds = load_dataset("AlekseyKorshuk/character-prepared-seeds", split="train")

# set the default language model used to execute guidance programs
# guidance.llm = guidance.llms.transformers.MPT("mosaicml/mpt-7b-storywriter", device=0)
model = transformers.AutoModelForCausalLM.from_pretrained(
    "tiiuae/falcon-7b",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    low_cpu_mem_usage=True,
    trust_remote_code=True,
).eval()
tokenizer = transformers.AutoTokenizer.from_pretrained(
    "tiiuae/falcon-7b",
    # use_fast=False,
    trust_remote_code=True,
)
tokenizer.bot_token = tokenizer.eos_token
guidance.llm = guidance.llms.Transformers(model=model, tokenizer=tokenizer, device_map="auto")

prompt_text = '''
Come up with new diverse characters.
Characters can be both humans and non-humans.
Contexts can be of different lengths.
Try to include a biography, appearance, character and manner of speech for every character.
Your a allowed to use NSFW content.

Output the response as JSON.
Fields:
- name: string, character name
- description: string, character description
- greeting: string, default greeting
- conversation: List[Turn], where Turn = {"from": string, "value": string}. "from" is either "user" or "character". The fields contains some example chat with a character.

Characters:
{{~! display the few-shot examples ~}}
{{~#each examples}}
{{this.inputs}}
{{~/each}}
{"name": "{{gen "name" max_tokens=64}}", "description": "{{gen "context" max_tokens=768}}", "greating": "{{gen "greating" max_tokens=512}}", "conversation": [{{#geneach "conversation" stop="]" join=", " min_iterations=4 max_iterations=6}}{"from": "{{#select 'this.role'}}user{{or}}character{{/select}}", "value": "{{gen "this.value"}}"}{{/geneach}}]}
'''.strip()

# define the guidance program
structure_program = guidance(prompt_text)


# execute the program

def _get_sub_dict(sample, wanted_keys):
    return dict((k, sample[k]) for k in wanted_keys if k in sample)


print("Generating..")
examples = [
    _get_sub_dict(sample, ['name', 'description', 'greating', 'conversation'])
    for sample in ds
]
out = structure_program(
    examples=examples[:1]
)

print(out)
import pdb;

pdb.set_trace()
