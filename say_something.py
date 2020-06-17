import os

def say(text):
    text = text.replace("\n", " ")
    os.system('mpg123 -q "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={}&tl=En-us"'.format(text))
    
if __name__ == '__main__':
    say("Hello and welcome to my game. I wonder what the limit is.")


    say("""
    Are you prepared to play?
    Let's get started.
    Draw a card from the top of the deck and flip it over.
    """)
