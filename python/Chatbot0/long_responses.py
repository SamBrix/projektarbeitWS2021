import  random

R_EATING = "Since I am a bot, me eating does not make any sense!"

def unknown():
    res = ['Could you rephrase that?',
           '...',
           'Sounds about right',
           'What does that mean?'][random.randrange(4)]
    return res