import json

import guidance
import openai

from config import base_prompt


def remove_duplicates(sample):
    temp = []
    res = dict()
    for key, val in sample.items():
        if val not in temp and val is not None and val != "":
            temp.append(val)
            res[key] = val
    return res


def prepare_examples(examples):
    new_examples = []
    for sample in examples:
        example = {}
        for key, value in sample.items():
            example[key] = json.dumps(value, indent=2)
        new_examples.append(example)
    return new_examples


def prepare_query(query):
    if isinstance(query, str):
        return query
    return json.dumps(query, indent=2)


def construct_guidance(description, request_format):
    return guidance(description + base_prompt + prepare_query(request_format))


def prepare_sample(sample):
    sample = remove_duplicates(sample)
    return sample


def get_sub_dict(sample, wanted_keys):
    return dict((k, sample[k]) for k in wanted_keys if k in sample)


def check_moderation(text):
    response = openai.Moderation.create(
        input=text
    )
    flagged = response["results"][0]["flagged"]
    return flagged
