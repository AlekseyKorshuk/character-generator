import json

import torch
from datasets import load_dataset, Dataset
import guidance
import transformers
import tqdm

from converter.config import chat_prompt
from converter.utils import construct_guidance, prepare_sample, get_sub_dict, prepare_examples, prepare_query
from converter.settings import settings

ds = load_dataset("AlekseyKorshuk/roleplay-characters", split="train")

guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo")

configs = []
for sample in tqdm.tqdm(ds):

    bot_config = dict()
    for setting in settings:
        guidance.llms.Transformers.cache.clear()
        guidance.llms.OpenAI.cache.clear()

        description = "{{#system~}}\n" + setting["description"] + "\n{{~/system}}"
        prompt = guidance(description + chat_prompt)

        sample = prepare_sample(sample)
        inputs = get_sub_dict(sample, setting["input_keys"])
        if inputs == {}:
            inputs = sample
        out = prompt(
            examples=prepare_examples(setting["examples"]),
            query=prepare_query(inputs),
        )
        # print(out)
        result = json.loads(out["result"])
        print(result)
        bot_config.update(result)

    print(bot_config)
    configs.append(bot_config)

ds_config = Dataset.from_list(configs)
ds_config.push_to_hub("AlekseyKorshuk/character-prepared")
import pdb;

pdb.set_trace()
