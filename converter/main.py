import torch
from datasets import load_dataset
import guidance
import transformers
import tqdm

from converter.utils import construct_guidance, prepare_sample, get_sub_dict, prepare_examples, prepare_query
from converter.settings import settings

ds = load_dataset("AlekseyKorshuk/roleplay-characters", split="train")

sample = ds[256]

# model = transformers.AutoModelForCausalLM.from_pretrained(
#     "huggyllama/llama-7b",
#     torch_dtype=torch.float16,
#     device_map="auto"
# ).eval()
# tokenizer = transformers.AutoTokenizer.from_pretrained(
#     "huggyllama/llama-7b"
# )
# guidance.llm = guidance.llms.Transformers(model=model, tokenizer=tokenizer)
guidance.llm = guidance.llms.Transformers("huggyllama/llama-7b", device=0)
import pdb;

pdb.set_trace()

bot_config = {}
for setting in tqdm.tqdm(settings):
    guidance.llms.Transformers.cache.clear()
    guidance.llms.OpenAI.cache.clear()

    prompt = construct_guidance(
        description=setting["description"],
        request_format=setting["request"],
    )

    sample = prepare_sample(sample)
    inputs = get_sub_dict(sample, setting["input_keys"])
    out = prompt(
        examples=prepare_examples(setting["examples"]),
        query=prepare_query(inputs),
    )
    expected_keys = setting["examples"][0]["outputs"].keys()
    print(out)
    for expected_key in expected_keys:
        bot_config[expected_key] = out[expected_key]

print(bot_config)
import pdb;

pdb.set_trace()
