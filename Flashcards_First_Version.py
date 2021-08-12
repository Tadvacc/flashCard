#Flashcards_First_Version.py
"""This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks a entry from all glossary entries.
It shows the entry.
After the user presses return, the program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also has the option to quit the program."""

from random import *

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(glossary))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(glossary[random_key])

# Set up the glossary

glossary = {'Bless':'Verb, pronounce words in a religious rite in order to confer or invoke divine favour upon; ask God to look favourably on.',
            'Love':'Noun, an intense feeling of deep affection.',
            'Peace':'Noun, freedom from disturbance; tranquillity.'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
