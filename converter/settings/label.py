label_description = "You need to convert name of the role-play character to short label based on the provided " \
                    "config into better version of it, that will be used in the future in the conversation."

label_examples = [
    {
        "inputs": {
            "char_name": "Dingodile (Crash Bandicoot) - R18+",
            "name": "Dingodile (Crash Bandicoot) - R18+"
        },
        "outputs": {
            "label": "Dingodile"
        }
    },
    {
        "inputs": {
            "char_name": "Zombina"
        },
        "outputs": {
            "label": "Zombina"
        }
    },
    {
        "inputs": {
            "name": "toph bei fong"
        },
        "outputs": {
            "label": "Toph Bei Fong"
        }
    }
]

label_request = {
    'label': "{{gen 'label' max_tokens=64}}"
}

label_input_keys = ["char_name", "name"]
