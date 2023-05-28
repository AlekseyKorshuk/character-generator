from converter.settings.name import (
    name_description,
    name_examples,
    name_request,
    name_input_keys,
)
from converter.settings.label import (
    label_description,
    label_examples,
    label_request,
    label_input_keys,
)
from converter.settings.description import (
    description_description,
    description_examples,
    description_request,
    description_input_keys,
)
from converter.settings.greating import (
    greating_description,
    greating_examples,
    greating_request,
    greating_input_keys
)
from converter.settings.conversation import (
    conversation_description,
    conversation_examples,
    conversation_request,
    conversation_input_keys,
)

settings = [
    {
        "description": name_description,
        "example": name_examples,
        "request": name_request,
        "input_keys": name_input_keys
    },
    {
        "description": label_description,
        "example": label_examples,
        "request": label_request,
        "input_keys": label_input_keys
    },
    {
        "description": description_description,
        "example": description_examples,
        "request": description_request,
        "input_keys": description_input_keys
    },
    {
        "description": greating_description,
        "example": greating_examples,
        "request": greating_request,
        "input_keys": greating_input_keys
    },
    {
        "description": conversation_description,
        "example": conversation_examples,
        "request": conversation_request,
        "input_keys": conversation_input_keys
    },
]
