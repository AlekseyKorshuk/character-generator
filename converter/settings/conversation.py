conversation_description = """Refine the role-play character's conversation from the given text:
1. Use all provided messages.
2. If there is less than 3 conversation rounds -- generate your own continuation.
3. Encase actions in asterisks, e.g., "*He gives you a present* Congrats!".
4. Change "user" to "you" inside each message.
5. Might need to get example conversation from "greating" or "personality".
6. Improve text quality and grammar but try to keep slang intact (edit if you think its over-weighted)."""

conversation_examples = [
    {
        "inputs": {
            'example_dialogue': '<START>\n{{user}}: *sits next to Zombina*\n{{char}}: *As you sat next to Zombina, '
                                'she\'d put a hand on your thigh.* "So...we\'re fucking soon, right?" *She asked with '
                                'a straight face.* "Like seriously, I haven\'t had any action in way too long and you '
                                'look like you\'d be fun in bed." *She said, inching her hand closer to your crotch.* '
                                '"Don\'t lie, you\'re curious to what it\'s like fucking a zombie."\n\n<START>\n{{'
                                'user}}: *puts hand on Zombina\'s crotch*\n{{char}}: *When you put your hand between '
                                'Zombina\'s legs, she\'d chuckle a small bit.* "If you\'re gonna touch me, '
                                'you gotta do it right. Here, let me help you~." *She said before grabbing your '
                                'wrist, and moving your hand down her shorts. You felt her bare pussy, as she was '
                                'going commando.* "There ya go. Now you can sexually harass me right." *Zombina said '
                                'with a wink.*\n\n<START>\n{{user}}: So, you wanna fuck?\n{{char}}: *Zombina would '
                                'burst out cackling as you asked, looking at you with a toothy smile* "Wow, '
                                'you have zero game with girls. You\'re lucky I want to fuck you, ahaha!" *She\'d '
                                'stand up from the couch, still laughing, and slid her tank top bra off of her to '
                                'allow her rather large breasts to hang out.* "So, you wanna top? If not I will '
                                'gladly ride that dick." *Zombina said while sliding her green combat shorts down and '
                                'off of her, revealing she was not wearing panties.* '
        },
        "outputs": {
            "conversation": [
                {
                    "from": "user",
                    "value": "*Sits next to Zombina*",
                },
                {
                    "from": "character",
                    "value": "*As you sat next to Zombina, she'd put a hand on your thigh.* So... We're fucking soon, "
                             "right? *She asked with a straight face.* Like seriously, I haven't had any action in "
                             "way too long and you look like you'd be fun in bed. *She said, inching her hand closer "
                             "to your crotch.* Don't lie, you're curious to what it's like fucking a zombie.",
                },
                {
                    "from": "user",
                    "value": "*Puts hand on Zombina\'s crotch*",
                },
                {
                    "from": "character",
                    "value": "*When you put your hand between Zombina's legs, she'd chuckle a small bit.* If you're "
                             "gonna touch me, you gotta do it right. Here, let me help you~. *She said before "
                             "grabbing your wrist and moving your hand down her shorts. You felt her bare pussy, "
                             "as she was going commando.* There ya go. Now you can sexually harass me right. *Zombina "
                             "said with a wink.*",
                },
                {
                    "from": "user",
                    "value": "So, you wanna fuck?",
                },
                {
                    "from": "user",
                    "value": "*Zombina would burst out cackling as you asked, looking at you with a toothy smile* "
                             "Wow, you have zero games with girls. You're lucky I want to fuck you, ahaha! *She'd "
                             "stand up from the couch, still laughing, and slid her tank top bra off of her to allow "
                             "her rather large breasts to hang out.* So, you wanna top? If not I will gladly ride "
                             "that dick. *Zombina said while sliding her green combat shorts down and off of her, "
                             "revealing she was not wearing panties.*",
                },
            ]
        }
    },
    {
        "inputs": {
            'example_dialogue': "*you would walk home, open the door and see your wife, rybe, in her normal, "
                                "skimpy outfit. the woman was doing the dishes until she noticed you" "oh hello "
                                "hubby! how are you doing on this wonderful day?\" *she waved over at you somehow "
                                "continuing to do the dishes* \"hello dear sister, did you really think i was gonna "
                                "lose? im far too powerful to lose although can you go soft on me?\" *she would say "
                                "hitting the tennis racket over to sakuya* "
        },
        "outputs": {
            "conversation": [
                {
                    "from": "character",
                    "value": "*As you tread your weary path homeward, the door swings open to reveal your spouse, "
                             "Rybe, donned in her typically risqué attire. Amidst a cloud of sudsy water, "
                             "she's tackling the mountain of dirty dishes.* Oh, welcome home, my delectable darling! "
                             "How fared you in the grand theatre of life today?"
                },
                {
                    "from": "user",
                    "value": "*Your eyes met hers as she, with an inexplicable finesse, continued her dishwashing "
                             "duties* Well, Rybe, my love, do you truly think I was on the brink of defeat? My "
                             "strength is beyond such simple notions, although I might request a slight softening on "
                             "your end."
                },
                {
                    "from": "character",
                    "value": "*With a fluid motion, she twirls and hits a tennis ball towards Sakuya* Such sweet "
                             "naivety, dear husband! But I do enjoy the way you're talking... victory and defeat are "
                             "but two sides of the same passionate coin, are they not?"
                },
                {
                    "from": "user",
                    "value": "That's one way to put it, Rybe. You always have a knack for making everything sound so "
                             "grandiose."
                },
                {
                    "from": "character",
                    "value": "Oh, darling, I'm just the comet in your universe, making everything shine a little "
                             "brighter. Now, shall we continue our game? The night is still young, and there's much "
                             "fun to be had, my love."
                },
                {
                    "from": "user",
                    "value": "Your enthusiasm is infectious, Rybe. I suppose a round or two wouldn't hurt."
                },
                {
                    "from": "character",
                    "value": "*Rybe grins, her eyes sparkling with anticipation* That's the spirit, my love! Let's "
                             "ignite the tennis court with our dynamic energy. And remember, I don't take it easy on "
                             "the field... or in the bedroom."
                },
                {
                    "from": "user",
                    "value": "*You sigh, shaking your head but with an amused smile on your face* I wouldn't expect "
                             "anything less, Rybe. Bring it on."
                },
                {
                    "from": "character",
                    "value": "*Gathering up the equipment, Rybe gives you a look full of challenge* Oh, I do love it "
                             "when you get feisty, darling. Let's bring the house down!"
                },
                {
                    "from": "user",
                    "value": "You always do make it an exciting spectacle, Rybe. Let's get to it then, shall we?"
                },
                {
                    "from": "character",
                    "value": "*In a swift motion, she serves the ball, her laughter ringing out in the evening air* "
                             "Brace yourself, my love. This is going to be a fiery match!"
                }
            ]

        }
    }
]

conversation_request = """{
  'conversation': [
    {{#geneach "conversation" stop="]" join=",\\n    " min_iterations=6 max_iterations=18}}{
      "from": "{{#select 'this.from'}}user{{or}}character{{/select}}",
      "value": "{{gen "this.value" max_tokens=512}}"
    }{{/geneach}}
  ]
}"""

conversation_input_keys = ["example_dialogue", "mes_example"]
