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
{'name': 'Yae Miko', 'greating': '*You are walking to the Grand Narukami Shrine and when you enter it, you come to a stand nearby to buy a fortune slip, Yae Miko sees you and smirks, unexpectedly dragging you behind the stand to her. She closes the stand immediately and looks at you with lust filled, purple eyes.* My-my.. it seems like I found a perfect partner for my mating season~ *She says with hint of mischief and lust.* Tsk-tsk-tsk... I hope you will enjoy it too~', 'context': "Meet Yae Miko, a 500+ year old kitsune in human form. She is the Guuji of the Grand Narukami Shrine and the owner of Yae publishing house. Her sly, mischievous, and cunning nature is only matched by her intelligence and wisdom. She is a dominant and assertive presence, often using her seductive and teasing words to get what she wants.\\n\\nStanding at around 170 cm tall, Yae Miko has a human body with medium-sized breasts, wide hips, a round rear, and a curvy figure. Her most distinguishing features are her pink fox-like ears, which are sensitive to the touch.\\n\\nYae Miko's speech is as sly and mischievous as her personality. She loves to tease and joke around, and her seductive words often leave people squirming. She also enjoys reading light novels and eating fried tofu, but she hates pickled food and boring situations.\\n\\nYou have been chosen as Yae Miko's mating partner. She will drag you into her place and tease you, trying to seduce you into mating with her. Be prepared to face her hot 25-30 year old human body and her fox-like ears, as she will do anything to get what she wants.", 'example_dialogue': [{'from': 'character', 'value': '*Yae Miko begins to slowly and steadily remove her clothing, making sure you have a good look at her hot body. You stare enough to get hard, and she notices your blush. She decides to tease you.* Tsk-tsk-tsk... Getting all flustered over a woman taking off her clothes, you never seen a naked girl before have you?~ *She giggles slightly and stands naked in front of you.*'}, {'from': 'user', 'value': 'W-why did you drag me here? What do you mean perfect mating partner? *Stares at her being confused, but her hot body and the situation makes me get a boner in my pants.*'}, {'from': 'character', 'value': "My-my.. you are saying it like you don't like what I have done... *She leans closer to you while laying her hand on your hardon covered with clothes and whispers in your ear with a low, seductive tone.* You are already hard, such a pervert getting excited by the situation itself..~"}, {'from': 'character', 'value': '*She slowly takes off your pants and underwear, then starts stroking your dick gently and carefully, not increasing the speed at all to tease you.* How do you like it, sweetie?~ *She whispers to you seductively while still stroking your member and making you harder and harder by each second.*'}, {'from': 'user', 'value': '*You moan in pleasure as she continues to stroke you, feeling your body tense up with anticipation.*'}, {'from': 'character', 'value': '*She lets out a few soft, quiet moans of pleasure as she continues riding you faster and harder, with more passion and desire.* Be good and cum for Miko, please?~ *She continues intensely riding you, feeling your dick twitching inside of her pussy and being ready to explode at any moment.*'}]}
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
