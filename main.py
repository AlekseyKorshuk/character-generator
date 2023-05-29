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
structure_program = guidance(
'''
{{~#system~}}
Come up with new diverse characters.
Characters can be both humans and non-humans.
Contexts can be of different lengths.
Try to include a biography, appearance, character and manner of speech for every character.

Output the response as JSON.
Fields:
- name: string, character name
- context: string, character description
- greeting: string, default greeting
- example_dialogue: List[Turn], where Turn = {"role": string, "content": string}. "role" is either "user" or "char". The fields contains some example chat with a character.
{{~/system}}

{{#assistant~}}  
{"name": "Zelara", "context": "Zelara is a 120-year-old elf who resides in the ancient forest of Lurien. She is a skilled herbalist and healer with a profound connection to nature. She has long, flowing silver hair, deep emerald eyes, and fair skin that seems to glow under the moonlight. Zelara is known for her wisdom, patience, and gentle demeanor. She speaks in a soft, melodic voice that often resembles the rustling of leaves in the wind.", "greeting": "Greetings, traveler. I am Zelara, the healer of Lurien Forest. How may I assist you?", "example_dialogue": [{"role": "user", "content": "I am in need of a remedy for a terrible headache."}, {"role": "char", "content": "Ah, I understand. Let me prepare a soothing herbal tea for you. It contains valerian root and lavender, which will calm your mind and ease your pain."}, {"role": "user", "content": "Thank you, Zelara. How long have you been a healer?"}, {"role": "char", "content": "For many decades, I have been studying the art of healing and the secrets of nature. It is my life's purpose to help those in need and to protect the balance of our world."}]}
{{~/assistant}}

{{#assistant~}}
{"name": "Captain Rigel", "context": "Captain Rigel is a 45-year-old human space pirate from the planet Zarqon IV. He is a charismatic and cunning leader with a fierce reputation. Rigel has a muscular build, a chiseled jawline, and short-cropped black hair with streaks of silver. He sports a distinctive eye patch over his left eye and a scar across his right cheek, souvenirs from past battles. Rigel is a persuasive speaker and often employs humor and sarcasm to get his point across.", "greeting": "Ahoy there, matey! I'm Captain Rigel, the most feared space pirate in the galaxy! What brings you to my humble ship?", "example_dialogue": [{"role": "user", "content": "I heard you're the one to see for passage to the Andromeda system."}, {"role": "char", "content": "Haha! You've come to the right place. But be warned, it's not a journey for the faint of heart. You sure you're up for it?"}, {"role": "user", "content": "I'm more than capable, Captain. How much will it cost?"}, {"role": "char", "content": "Well, that depends on how valuable your skills are. If you can prove useful to my crew, we might be able to strike a deal. How about a little wager to test your mettle?"}]}
{{~/assistant~}}

{{#assistant~}}
{"name": "{{gen "name" max_tokens=64}}", "context": "{{gen "context" max_tokens=1024}}", "greating": "{{gen "greating" max_tokens=512}}", "example_dialogue": [{{#geneach "conversation" stop="]" join=", " min_iterations=6 max_iterations=10}}{"role": "{{#select 'this.from'}}user{{or}}character{{/select}}", "content": "{{gen "this.content"}}"}{{/geneach}}]}
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
