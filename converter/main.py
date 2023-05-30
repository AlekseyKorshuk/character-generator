import json

import torch
from datasets import load_dataset, Dataset
import guidance
import transformers
import tqdm

from converter.utils import construct_guidance, prepare_sample, get_sub_dict, prepare_examples, prepare_query, \
    check_moderation
from converter.settings import settings

ds = load_dataset("AlekseyKorshuk/roleplay-characters", split="train")

prepared_dataset = None
try:
    prepared_dataset = load_dataset("AlekseyKorshuk/character-prepared-seeds", split="train")
    configs = list(prepared_dataset)
except:
    configs = []
# model = transformers.AutoModelForCausalLM.from_pretrained(
#     "eachadea/vicuna-13b-1.1",
#     torch_dtype=torch.float16,
#     device_map="auto"
# ).eval()
# tokenizer = transformers.AutoTokenizer.from_pretrained(
#     "eachadea/vicuna-13b-1.1",
#     use_fast=False
# )
# guidance.llm = guidance.llms.Transformers(model=model, tokenizer=tokenizer)
guidance.llm = guidance.llms.OpenAI("text-davinci-003")

for sample in tqdm.tqdm(ds):
    name = sample["char_name"] or sample["name"]
    if prepared_dataset is not None and name in list(prepared_dataset["original_name"]):
        print("Skip, already in the dataset")
        continue

    prepared_sample = prepare_sample(sample)
    prepared_sample.pop("image", None)
    prepared_sample.pop("metadata", None)
    text = json.dumps(prepared_sample)
    if not check_moderation(text):
        continue

    try:
        bot_config = {}
        for setting in settings:
            # guidance.llms.Transformers.cache.clear()
            # guidance.llms.OpenAI.cache.clear()

            prompt = construct_guidance(
                description=setting["description"],
                request_format=setting["request"],
            )

            prepared_sample = prepare_sample(sample)
            inputs = get_sub_dict(prepared_sample, setting["input_keys"])
            if inputs == {}:
                inputs = prepared_sample
            out = prompt(
                examples=prepare_examples(setting["examples"]),
                query=prepare_query(inputs),
            )
            expected_keys = setting["examples"][0]["outputs"].keys()
            for expected_key in expected_keys:
                bot_config[expected_key] = out[expected_key]
        bot_config["image"] = sample["image"]
        bot_config["original_name"] = sample["char_name"] or sample["name"]
        print(bot_config)
        configs.append(bot_config)
        ds_config = Dataset.from_list(configs)
        ds_config.push_to_hub("AlekseyKorshuk/character-prepared-seeds")
    except Exception as ex:
        print(ex)

import pdb;

pdb.set_trace()
