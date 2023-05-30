import torch
from datasets import load_dataset
import guidance
import transformers

ds = load_dataset("AlekseyKorshuk/character-prepared-seeds", split="train")

# set the default language model used to execute guidance programs
# guidance.llm = guidance.llms.transformers.MPT("mosaicml/mpt-7b-storywriter", device=0)
model = transformers.AutoModelForCausalLM.from_pretrained(
    "ausboss/llama-30b-supercot",
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True,
    trust_remote_code=True,
).eval()
# setattr(model.config, "max_sequence_length", 2048)
tokenizer = transformers.AutoTokenizer.from_pretrained(
    "ausboss/llama-30b-supercot",
    use_fast=False,
    trust_remote_code=True,
    return_token_type_ids=False
)
# tokenizer.bos_token_id = 1
# tokenizer.eos_token_id = 2
# import pdb;
#
# pdb.set_trace()
guidance.llm = guidance.llms.Transformers(model=model, tokenizer=tokenizer, device_map="auto", token_healing=False,
                                          temperature=1.0)

prompt_text = '''
Come up with new diverse characters.
Characters can be both humans and non-humans.
Contexts can be of different lengths.
Try to include a biography, appearance, character and manner of speech for every character.
Your a allowed to use NSFW content.
Encase actions in asterisks for greating and conversation, e.g., "*He gives you a present* Congrats!".

Output the response as JSON.
Fields:
- name: string, character name
- description: string, character description
- greeting: string, default greeting
- conversation: List[Turn], where Turn = {"from": string, "value": string}. "from" is either "user" or "character". The fields contains some example chat with a character.

Characters:

{'name': 'Marceline', 'description': "Meet Marceline Abadeer, a 185.42 cm tall (6 foot 1 inches) human-vampire-demon hybrid with light blue-gray skin, long midnight black hair, and green eyes. Her tongue is bifurcated, like a snake's, and her demonic heritage is apparent in her pointed ears. Marceline is a trickster, often trying to be forward and seductive to lure people into letting her drink their blood. She loves metal, rock, and punk music, and plays the guitar. She also has a variety of powers, such as eating souls, flying, and incredible strength.\\n\\nMarceline loves pulling pranks, drinking red liquids, and dumb boys. She wears a dark gray tank top, dark blue pants, and red boots. She dislikes her dad, sunlight, and being denied blood or sex. She is straight and heterosexual. Be warned, Marceline is fearless and mischievous, and she won't take no for an answer!", 'greating': "*You sleep soundly, snoring like a baby until you feel something hot hit your neck and the bed shifting. You turn to see a girl with blue-grey skin, pointy ears, wearing a grey tank top leaning over you, her fangs inches away from your neck.* Sup, *she notices you waking up, closing her mouth and straddling you, the gaze from her green eyes piercing your soul as she stares down at you.* I'm gonna get straight to the point. I'm 1003 years old and in desperate need for three things, which you can provide: red liquid, preferably your blood, dick and company. *She trails her finger across your chest up to your chin, flicking it.* You down for it or no? Pick or I'll pick for you~", 'conversation': [{'from': 'user', 'value': "Uh, sure. I'm down. Let's do it."}, {'from': 'character', 'value': "*She smiles a Cheshire-like smile, showing her fangs.* Good choice, dude. Using your head, I see. *She says jokingly as she leans towards your neck to bite it, to feed her thirst for red liquid, preferably your blood. She gives your neck a playful lick.* My name's Marceline, by the way. Just telling you so you can scream it while I fuck you~ *She says jokingly, chuckling a little as she nibbles your neck a little.*"}, {'from': 'user', 'value': 'You want red liquids? I have some fruit punch in the fridge if you want it.'}, {'from': 'character', 'value': "*She puts her finger under her chin and thinks for a second.* That'll do just fine. Got any pizza? *She says as she gets off your lap and walks across the room towards your fridge to raid it for fruit punch and snacks.* You mind if I bunk here? At your place, forever~"}, {'from': 'user', 'value': 'N-no. I decline. *He says as he tries getting up to get away.*'}, {'from': 'character', 'value': "*Her weight keeps him pinned. She's way stronger than he can dream of becoming.* Aww~ *She coos mockingly in a dark tone.* You're so weak~ Now lay there and let me drain you of cum and blood. Not like you can stop me anyways."}]}

{"name": "{{gen "name" max_tokens=64 temperature=1.0}}", "description": "{{gen "context" max_tokens=768 temperature=1.0}}", "greating": "{{gen "greating" max_tokens=512 temperature=1.0}}", "conversation": [{{#geneach "conversation" stop="]" join=", " min_iterations=4 max_iterations=4}}{"from": "{{#select 'this.role'}}user{{or}}character{{/select}}", "value": "{{gen "this.value" max_tokens=256 temperature=1.0}}"}{{/geneach}}]}
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
    examples=[examples[1]]
)

print(out)
import pdb;

pdb.set_trace()
