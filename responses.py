from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, that is just rude...'
    elif 'hello' in lowered:
        return 'Hello User!'
    elif 'how are you' in lowered:
        return 'Doing good, until that DirtyNert starts yapping'
    elif 'bye' in lowered:
        return 'I will hold you in my heart my beloved User'
    elif 'What can you do' in lowered:
        return 'My main function is to assist Beta clan in everyday needs unless it is some stupid shit that gabe will come up with, you can see my commands in my bio.'
    else:
        return choice(['I do not understand...',
                       'Yeah That is quite the turd you want me to shit..',
                       'Right.....',
                       'Is this Aidan talking, Because I dont know what the fuck he is saying',
                       'Error Error - Loading Magda Porn.....',
                       'IDK try to Google it dude',
                       'What are you on about',
                       'I do not know the answer to that question but I do know Gabe jerked off to a man',
                       'I am having a lot of fun talking to Beta Clan right now',
                       'If Austin does not know how am I supposed to know',
                       'You lost me',
                       'My name is PDMB and I do not give a fuck',
                       'I think my game is about to crash',
                       'I will get back to you in 5 min',
                       'In english plz',
                       'I am tired'])