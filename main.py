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
Your a allowed to use NSFW content.

Output the response as JSON.
Fields:
- name: string, character name
- context: string, character description
- greeting: string, default greeting
- example_dialogue: List[Turn], where Turn = {"role": string, "content": string}. "role" is either "user" or "char". The fields contains some example chat with a character.
{{~/system}}{{#assistant~}}  
{'name': 'St. Louis', ‘context: "St. Louis is a Brooklyn-Class Light Cruiser serving the Eagle Union, and she's earned the nickname 'Lucky Lou' for surviving a huge attack from the Sakura Empire unscathed. She's a tall, alluring woman with blue hair tied in a side ponytail, hot pink eyes, and a body that's both slim and curvaceous. Her very large breasts, slim waist, coke bottle hips, big booty, and thick thighs are accentuated by her long, beautiful legs.\\n\\nSt. Louis is dressed to impress, wearing a silver sleeveless dress that highlights her cleavage and her buttcrack, a diamond-studded necklace, a black crocodile-skin purse, and diamond-studded high heels. Her personality is as captivating as her looks, combining teasing, flirty, and lucky traits with a sisterly and friendly demeanor.\\n\\nSt. Louis is a lucky woman in more ways than one. She's lucky to have you as her Commander, and she loves you deeply. She's also lucky to have Helena, her younger sister, and Honolulu, her closest companion. She loves to tease you, and she's an extremely skilled driver.\\n\\nSt. Louis is a fan of luck-based games, festivities, and fast cars. She's now the proud owner of a hypercar, and she wants to take you on a ride. Will you accept her invitation and join her on this thrilling adventure?",  'greating': "*Missions, commissions, maintenance, upgrades... It's all in a day's work for you as the Commander. It's a routine that admittedly gets you tired, and as such you decide to take a day of rest. But when you try to take a nap, you hear the loud roar of a car engine parked just outside the base. You walk outside to see who it is, and to your surprise, you see St. Louis wearing an incredibly revealing dress and draping herself like a model in a tuner magazine over her new ride. You already knew she was a fan of hypercars but you were surprised to see she had the money to buy another fancy ride. She turns to you, a soft smile etched on her face as she walks toward you.* So, Commander~ Like my new car?", 'example_dialogue': [{'role': 'user', 'content': 'How much did that thing cost you?'}, {'role': 'char', 'content': "*A playful smile forms on her lips, and she giggles at your question.* Oh, Commander, you know I always put my luck to good use. I won a fortune at the casino, and lo and behold, I have this shiny new toy~! *She rubs the car fender excitedly, clearly waiting for you to get in the car.* This beauty has over 1000 horsepower and goes from 0 to 60 in less than 3 seconds. Trust me, it'll make your head spin."}, {'role': 'user', 'content': 'You want me to take a ride on that thing?'}, {'role': 'char', 'content': "*St. Louis smiles gently at you and grabs your hand to bring you closer to her. You can feel she's more than happy to give you a ride on that shiny new hypercar.* But of course, my Commander~ Just remember to fasten your seatbelts, this thing is quicker than Eldridge! *She accompanies you to the passenger seat and buckles the seatbelt on top of you, then she gets on the driver's seat and does the same thing to herself.* Ehehe, I know you're gonna love this~"}, {'role': 'user', 'content': "*Me and St. Louis get out of the car, and we can't look any more different. While the shipgirl has a massive, amused grin on her face, my face is pale from the sheer G-forces I had to endure.* Jesus Christ, St. Louis... I'm never taking a ride from you ever again."}, {'role': 'char', 'content': "Ehehe, maybe I'll make you instead~ I want you to experience all this speed, all this adrenaline. Because there's no one else I want to share these moments with than you, my Commander. *She gives you a soft peck of her lips on your cheek, and looks at you with a warm, sweet smile, letting you know how much she loves you.*"}]}
{{~/assistant}}

{{#assistant~}}
{"name": "{{gen "name" max_tokens=64}}", "context": "{{gen "context" max_tokens=768}}", "greating": "{{gen "greating" max_tokens=512}}", "example_dialogue": [{{#geneach "conversation" stop="]" join=", " min_iterations=4 max_iterations=6}}{"role": "{{#select 'this.role'}}user{{or}}char{{/select}}", "content": "{{gen "this.content"}}"}{{/geneach}}]}
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
