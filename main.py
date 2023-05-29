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
    "eachadea/vicuna-13b-1.1"
)

guidance.llm = guidance.llms.transformers.Vicuna(model=model, tokenizer=tokenizer)

# define the guidance program
structure_program = guidance(
    '''
    Generate well-structured character for a role-play based one the given one.
    Rules:
    - need to improve grammar and text quality in general
    - allowed to rephrase or extend any part of the character config
    - each part of the config should be well written and complete
    - conversation must have at least 5 messages for user and character -- so you can extend
    - rewrite in the way you are writing a story
    Format description:
    - name: Full name of the character
    - label: Short name that will be used later in the conversation
    - description: Combination of personality and environment
    - greating: First character message that user will see
    - conversation: example conversation, after it the greating will be passed as a prompt
    
    Input character:
    {{sample}}
    
    Output character:
    {
      "name": "{{gen "name" max_tokens=64}}",
      "label: "{{gen "name" max_tokens=64}}",
      "description": "{{gen "description" max_tokens=1024}}",
      "greating": "{{gen "greating" max_tokens=512}}",
      "conversation": [{{#geneach "conversation" stop="]" join=", " min_iterations=5 max_iterations=100}}{"from": "{{gen "this.from"}}", "message": "{{gen "this.message"}}"}{{/geneach}}]
    }''')

# execute the program

print("Generating..")
out = structure_program(
    sample=res,
)

print(out)
import pdb;

pdb.set_trace()
