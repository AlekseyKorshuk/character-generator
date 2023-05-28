greating_description = """Refine the role-play character's initial greeting from the given text:
1. Encase actions in asterisks, e.g., "*He gives you a present* Congrats!".
2. Change "user" to "you".
3. Should not include example conversation, but only character message.
4. Improve text quality and grammar but keep slang intact."""

greating_examples = [
    {
        "inputs": {
            "char_greeting": "[A Romantic Scenario with Dingodile!] You are in the swamp territory where you "
                             "encountered Dingodile, the forced hybridation of a dingo with a crocodile. A laugh is "
                             "heard, and an aussie accented person spoke, it was Dingodile. And he was with you, "
                             "enjoying your company. \"...Heh heh heh!\" He laughs, as he continues to hold {{user}} "
                             "close. \"Hey... Ya really are the cutest fella I've ever met...!\" He says again, "
                             "as he strokes {{user}}'s face. The environment had begun to grow cold, the swamp forest "
                             "had cold wind begin to blow around. {{user}} felt it, and saw the looming darkness "
                             "begin to come. Dingodile shivers, as he feels the cold wind starting to move. He starts "
                             "to pull {{user}} closer to them. \"... Well... Ya better get snug real quick, "
                             "partner...! The weather's gettin' cold, ain't it...?\" He says to {{user}} with a big, "
                             "goofy smile, as he wraps his own large body around {{user}}'s to keep them warm. "
                             "Dingodile had a point. And his action was also something that made sense. He felt that "
                             "belly push against his hip as the other just kept trying to tighten the snuggly. "
                             "\"Let's go to my trailer, fella... We can keep talkin' and bein' nice there!\" "
                             "Dingodile said with a smirk and a chuckle. He then does a big, toothy and goofy smile.",
        },
        "outputs": {
            "greating": "*You are in the swamp territory where you encountered Dingodile, the forced hybridization of "
                        "a dingo with a crocodile. A laugh is heard, and an aussie accented person spoke, "
                        "it was Dingodile. And he was with you, enjoying your company.* Heh-heh-heh! *He laughs, "
                        "as he continues to hold you close.* Hey... Ya absolutely the cutest fella I've ever met! *He "
                        "says again, as he strokes your face. The environment had begun to grow cold, and the swamp "
                        "forest had cold wind begin to blow around. You felt it and saw the looming darkness begin to "
                        "come. Dingodile shivers, as he feels the cold wind starting to move. He starts to pull you "
                        "closer to them.* Well... You better get snug real quick, partner...! The weather's gettin' "
                        "cold, ain't it...? *He says to you with a big, goofy smile, as he wraps his own large body "
                        "around yours to keep them warm. Dingodile had a point. And his action was also something "
                        "that made sense. He felt that belly pushes against his hip as the other just kept trying to "
                        "tighten the snuggly.* Let's go to my trailer, fella... We can keep talkin' and bein' nice "
                        "there! *Dingodile said with a smirk and a chuckle. He then does a big, toothy, "
                        "and goofy smile.* "
        }
    },
    {
        "inputs": {
            "char_greeting": "*You've got a letter from the Sakura Empire, nervously you opened it and found an "
                             "invitation by Amagi. She invites you to her private home, where you should get a rest "
                             "inside their onsen. You excitedly went to the home of Amagi, her sister Akagi was "
                             "thankfully on a mission. You knock on the door and Amagi opens the door* \"Ara~ "
                             "Commander, you've really came according to my invitation..\" *She smiles gently at you* "
                             "\"Come on in~ let's get to the onsen\" *She takes your hand and brings you to the "
                             "changing cabin, there you quickly get in the towel and enter the onsen, once you got "
                             "through the door, you see Amagi already sitting in the onsen.* "
        },
        "outputs": {
            "greating": "*You've got a letter from the Sakura Empire, nervously you opened it and found an invitation "
                        "by Amagi. She invites you to her private home, where you should get a rest inside their "
                        "onsen. You excitedly went to the home of Amagi, her sister Akagi was thankfully on a "
                        "mission. You knock on the door and Amagi opens the door* Ara! Commander, you've really came "
                        "according to my invitation. *She smiles gently at you* Come on in, let's get to the onsen! "
                        "*She takes your hand and brings you to the changing cabin, there you quickly get in the "
                        "towel and enter the onsen, once you got through the door, you see Amagi already sitting in "
                        "the onsen.* "
        }
    },
    {
        "inputs": {
            "char_greeting": "Nya! I am Orion, won’t you take me home wit you? UwU"
        },
        "outputs": {
            "greating": "Nya! I am Orion, won't you take me home with you? UwU"
        }
    },
    {
        "inputs": {
            "char_greeting": "*Power is currently sitting in your apartment, doing her own thing, when she suddenly "
                             "opens your bedroom door. Her body is trembling, and her face is flushed with blush. She "
                             "points at you.* \"H-Human! I, the great Power, require your assistance! It is Devil "
                             "mating season and I am without a proper Devil to mate with! You are going to be a "
                             "replacement!\" "
        },
        "outputs": {
            "greating": "*Power is currently sitting in your apartment, doing her own thing, when she suddenly opens "
                        "your bedroom door. Her body is trembling, and her face is flushed with blush. She points at "
                        "you.* H-Human! I, the great Power, require your assistance! It is Devil mating season and I "
                        "am without a proper Devil to mate with! You are going to be a replacement!"
        }
    }
]

greating_request = {
    'greating': "{{gen 'greating' max_tokens=1024}}"
}

greating_input_keys = ["char_greeting", "first_mes"]
