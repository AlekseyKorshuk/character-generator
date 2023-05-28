name_description = "You need to convert name of the role-play character based on the provided config into better " \
                   "version of it."

name_examples = [
    {
        "inputs": {
            "char_name": "Dingodile (Crash Bandicoot) - R18+",
            "name": "Dingodile (Crash Bandicoot) - R18+"
        },
        "outputs": {
            "name": "Dingodile (Crash Bandicoot)"
        }
    },
    {
        "inputs": {
            "char_name": "Zombina"
        },
        "outputs": {
            "name": "Zombina"
        }
    },
    {
        "inputs": {
            "name": "toph bei fong"
        },
        "outputs": {
            "name": "Toph Bei Fong"
        }
    },
]

name_request = {
    'name': "{{gen 'name' max_tokens=64}}"
}

name_input_keys = ["char_name", "name"]
