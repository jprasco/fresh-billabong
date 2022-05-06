'''
madlibs.py
idea is we have 3-5 madlibs that we can cycle through
    maybe famous monologues? or dialogue scenes?
each one has different adjectives, nouns, verbs, etc. Hopefully in 
different orders or something.

- prompt user to make selection of madlib (give # of words needed for each)
- prompt user to fill out each word
- update how many have been filled in "#filled/#unfilled" format
- Congratulate user as we "craft your unique story"
- print out madlib
- prompt to play again

Build this into an app or something later?

'''
# Source Scripts for adlibs
import time


deadPoets = \
'''
    We don't read and write poetry because it's cute. We read and write poetry because we 
are members of the human race. And the human race is filled with passion. And medicine, 
law, business, engineering, these are noble pursuits and necessary to sustain life. But 
poetry, beauty, romance, love, these are what we stay alive for. Boys, you must strive 
to find your own voice because the longer you wait to begin, the less likely you are to 
find it at all.
'''
theSocial = \
'''
    I think if your clients want to sit on my shoulders and call themselves tall, they have the
right to give it a try—but there's no requirement that I enjoy sitting here listening to people 
lie. You have part of my attention—you have the minimum amount. The rest of my attention is back
 at the offices of Facebook, where my colleagues and I are doing things that no one in this room,
including and especially your clients, are intellectually or creatively capable of doing.
'''
commaGets = \
'''
    Sarah Perry was a veterinary nurse who had been working daily at an old zoo in a deserted 
district of the territory, so she was very happy to start a new job at a superb private practice 
in North Square near the Duke Street Tower. That area was much nearer for her and more to her 
liking. Even so, on her first morning, she felt stressed. She ate a bowl of porridge, checked 
herself in the mirror and washed her face in a hurry. Then she put on a plain yellow dress and a 
fleece jacket, picked up her kit and headed for work. 
'''
romeoPro = \
'''
Two households, both alike in dignity
(In fair Verona, where we lay our scene),
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-crossed lovers take their life;
Whose misadventured piteous overthrows
Doth with their death bury their parents’ strife.
The fearful passage of their death-marked love
And the continuance of their parents’ rage,
Which, but their children’s end, naught could remove,
Is now the two hours’ traffic of our stage;
The which, if you with patient ears attend,
What here shall miss, our toil shall strive to mend.
'''
eisenhower = \
'''
In the councils of government, we must guard against the acquisition of unwarranted influence, 
whether sought or unsought, by the military-industrial complex. The potential for the disastrous 
rise of misplaced power exists and will persist. We must never let the weight of this combination 
endanger our liberties or democratic processes. We should take nothing for granted. Only an alert 
and knowledgeable citizenry can compel the proper meshing of the huge industrial and military 
machinery of defense with our peaceful methods and goals, so that security and liberty may prosper 
together.
'''

# _______________________________________________________________________________________
# Put it all together
# prompt to choose piece
import os
import sys
import subprocess
from gettext import dpgettext
import time

print('''
Welcome to the AdLib Addinator!
Which piece would you like to adlib?

#       Original Piece
1.      Dead Poets' Society
2.      The Social Network
3.      Comma Gets a Cure
4.      Romeo and Juliet
'''
)

choice = input("Type the number of your choice here: ", )
choice = choice.strip()
time.sleep(0.6)

if choice == '1':

    dpV1 = input("Verb: ")
    dpV2 = input("Verb: ")
    dpGroup = input("Social Organization: ")
    dpAdj1 = input("Adjective: ")
    dpN1 = input("Abstract Noun: ")
    dpN2 = input("Abstract Noun: ")
    dpN3 = input("Abstract Noun: ")
    dpN4 = input("Abstract Noun: ")
    dpPluralAddress = input("Plural Noun: ")
    dpN5 = input("Noun: ")
    dpV3 = input("Verb: ")

    print('Constructing your story!')
    time.sleep(2)
    os.system('CLS')
    print(f'''
    We don't {dpV1} and {dpV2} poetry because it's cute. We {dpV1} and {dpV2} poetry because we 
are members of the {dpGroup}. And the {dpGroup} is filled with passion. And medicine, 
law, business, engineering, these are {dpAdj1} pursuits and necessary to sustain life. But 
{dpN1}, {dpN2}, {dpN3}, {dpN4}, these are what we stay alive for. {dpPluralAddress}, you must strive 
to find your own {dpN5} because the longer you wait to begin, the less likely you are to 
{dpV3} it at all.
''')
elif choice == '2':
    snPluralNoun1 = input("Plural Noun: ")
    snBodyPart = input("Body Part: ")
    snAdj1 = input("Adjective: ")
    snV1 = input("Present Progressive Verb: ")
    snQuant = input("Quantifier: ")
    snLocation = input("Location: ")
    snV2 = input("Present Progressive Verb: ")
    snPluralNoun2 = input("Plural Noun: ")

    print('Constructing your story!')
    time.sleep(2)
    os.system('CLS')
    print(f'''
    I think if your {snPluralNoun1} want to sit on my {snBodyPart} and call themselves {snAdj1}, they have the
right to give it a try—but there's no requirement that I enjoy {snV1} here listening to people 
lie. You have {snQuant} of my attention—you have the minimum amount. The rest of my attention is back
in {snLocation}, where my colleagues and I are {snV2} things that no one in this room,
including and especially your {snPluralNoun2}, are intellectually or creatively capable of {snV2}.
''')
elif choice == '3':
    comOccu = input("Occupation starting with a consonant: ") # Occupation starting with a consonant
    comAdj1 = input("Adjective starting with a vowel: ") # Ajective starting with a vowel
    comAdj2 = input("Adjective: ")
    comLoc = input("Location: ")
    comCompare = input("Comparative (word ending in \'-er\'): ") # Comparative (word that ends in 'er'
    comAdj3 = input("Adjective: ")
    comFood = input("Food: ")
    comV1 = input("Past Tense Verb: ") # Past tense Verb
    comColor = input("Color: ")
    comCloth = input("Article of Clothing: ") # Article of clothing
    
    print('Constructing your story!')
    time.sleep(2)
    os.system('CLS')
    print(f'''
    Sarah Perry was a {comOccu} who had been working daily at an {comAdj1} zoo in a deserted 
district of the territory, so she was very {comAdj2} to start a new job at a superb private practice 
in {comLoc} near the Duke Street Tower. That area was much {comCompare} for her and more to her 
liking. Even so, on her first morning, she felt {comAdj3}. She ate a bowl of {comFood}, {comV1} 
herself in the mirror and washed her face in a hurry. Then she put on a plain {comColor} dress and a 
{comCloth}, picked up her kit and headed for work. 
''')
elif choice == '4':
    rjPluralN =input("Plural Noun: ")
    rjCity = input("City: ")
    rjAdj1 = input("Adjective: ")
    rjN1 = input("Noun: ")
    rjBodyPart1 = input("Body Part: ")
    rjPluralNoun = input("Plural Noun: ")
    rjActiv = input("Plural Activity: ") # plural activity
    rjAdj2 = input("Adjective: ")
    rjNoun2 = input("Noun: ")
    rjTime = input("Plural Unit of Time: ") # Plural unit of time
    rjBodyPart2 = input("Body Part: ")

    print('Constructing your story!')
    time.sleep(2)
    os.system('CLS')
    print(f'''
Two {rjN1}, both alike in dignity
In fair {rjCity}, where we lay our scene,
From {rjAdj1} grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal {rjBodyPart1} of these two foes
A pair of star-crossed {rjNoun2} take their life;
Whose misadventured piteous {rjActiv}
Doth with their death bury their parents’ strife.
The {rjAdj2} passage of their death-marked love
And the continuance of their parents’ rage,
Which, but their children’s {rjNoun2}, naught could remove,
Is now the two {rjTime}’ traffic of our stage;
The which, if you with patient {rjBodyPart2} attend,
What here shall miss, our toil shall strive to mend.
''')

else:
    print('Oops! Something went wrong.')
    print('Let\'s try that again!')
    time.sleep(3)
    os.system('CLS')
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

print('''



'''
)
playAgain = input('Play Again? (y/n) ')

if playAgain == 'y':
    os.system('CLS')
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
elif playAgain == 'n':
    os.system('CLS')
else:
    print('Oops! Something went wrong.')
    print('Let\'s try that again!')
    time.sleep(3)
    os.system('CLS')
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

