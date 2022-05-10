#
# secretMessage.py
# idea here is to put in a secret message, choose the encoding method
# you want, put in the necessary parameters such as keywords or numbers
# and whatnot and then this bad boi will spit out the encoded version
#
# I think the message input will be in the general program and then the 
# we'll have functions for individual methods that use the message as the
# input and then request their own individual parameters from the user.
# 
import time
import sys
import os
import subprocess
import string
import random
import numpy as np


# ___________________________________________________________________________
# CAESAR CIPHER

def caesar(plainText):
    print(' ')
    print('Caesar Cipher Encoder')
    output = ''
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    shift = input('Enter your shift number (0-25): ') # this part is not idiot-proofed!!!
    shift = int(shift.strip())
    caesarShift = alph[shift:]+alph[:shift] # shifts right    this is correct
    translator = dict(zip(alph, caesarShift)) # this is correct too 
    for i in plainText:
        output += translator[i]
    
    print(f'''
    Your secret message:
        {output}
    with a shift key of {shift}
    ''')
    '''
    to decode: shift the alphabet right then create the dictionary using shift 
    first then correct alph translator = dict(zip(alph, caesarShift))
    '''
    return()

# ___________________________________________________________________________
# MONOALPHABETIC CIPHER

def monoalphabetic(plainText):
    print(' ')
    print('Monoalphabetic Cipher Encoder')
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    rando = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(rando)
    translator = dict(zip(alph, rando))
    output, outRand, outAlph= '', '', ''
    for i in plainText:
        output += translator[i]
    for i in rando:
        outRand += i
    for i in alph:
        outAlph += i
    print(f'''
    Your secret message:
        {output}
    with the alphabet key:
        {outAlph}
        {outRand}

    ''')
    '''
    to decode, input alphabet, input random  for i in alphabet and random 
    append to list, create a dictionary using translator = dict(zip(rando, alph)) 
    and then just translate back
    '''
    return()

# ___________________________________________________________________________
# DATE CIPHER

def date(plainText):
    print(' ')
    print('Date Cipher Encoder')
    print(' ')
    dateKey = input('Enter your key date (MMDDYYYY): ')
    while len(dateKey) != 8:
        print(' ')
        print('Please enter a valid date.')
        dateKey = input('Enter your key date (MMDDYYYY): ')
    dateKey.lstrip('0')
    keyList = []
    output = ''
    j=0
    for i in range(len(plainText)):
        i = i%len(plainText)
        keyList.append(dateKey[j])
        if j == len(dateKey)-1:
            j = 0
        else:
            j += 1
    print(keyList)
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    translator = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
        'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
        'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,
        'y':24,'z':25}
    for i in range(len(plainText)):
        output += alph[(translator[alph[i]] + int(keyList[i]))%26]
        #print('i:',i,'   alph(i):', alph[i])
        #print('keyList:', type(keyList[i]))
    if len(dateKey) == 7:
        dateKey.insert(0,0)
    print(f'''
    Your secret message:
        {output}
    with a date key of {dateKey}
    ''')

    return()

# ___________________________________________________________________________
# VIGINERE CIPHER

def viginere(plainText):
    print(' ')
    print('Viginere Cipher Encoder')
    print(' ')
    # vigSqr is 26*26 cipher containing every possible Caesar Cipher
    vigSqr = [\
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],\
        ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a'],\
        ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b'],\
        ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c'],\
        ['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d'],\
        ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e'],\
        ['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f'],\
        ['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g'],\
        ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h'],\
        ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i'],\
        ['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j'],\
        ['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k'],\
        ['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l'],\
        ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m'],\
        ['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n'],\
        ['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'],\
        ['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'],\
        ['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'],\
        ['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'],\
        ['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'],\
        ['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],\
        ['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'],\
        ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'],\
        ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'],\
        ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'],]
    output = ''
    translator = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
        'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
        'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,
        'y':24,'z':25}

    keyWord = input("Enter your key word: ")
    keyWord.lower()
    keyWord = keyWord.translate({ord(c): None for c in string.whitespace})

    keyList = []
    j = 0
    for i in range(len(plainText)): # building key list
        #i = i%len(plainText) # idk why this is here?
        keyList.append(translator[keyWord[j]])
        #print(keyWord[j], translator[keyWord[j]])
        if j == len(keyWord)-1:
            j = 0
        else:
            j += 1
    print(keyList)
    for i in range(len(plainText)):
        print(translator[plainText[i]],keyList[i])
        output += vigSqr[keyList[i]][translator[plainText[i]]]
    
    print(f'''
    Your secret message:
        {output}
    using the key word \'{keyWord}\'
    ''')
    
    return()

# ___________________________________________________________________________
# PLAYFAIR CIPHER

def playfair(plainText):
    print(' ')
    print('Playfair Cipher Encoder')
    print(' ')
    if len(plainText)%2 != 0:
        plainText += 'z'
    output = ''
    keyWord = input("Enter your key word: ")
    if 'j' in keyWord:
        keyWord.replace('j', 'i')
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l',\
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
       
    keyList = []
    for i in keyWord:
        if i not in keyList:
            keyList.append(i)
    for i in alph:
        if i not in keyList:
            keyList.append(i)

    keySqr = [keyList[:5],keyList[5:10],keyList[10:15],keyList[15:20],keyList[20:25]]
    # for x in keySqr:
    #    print(x)
    i = 0
    while i < len(plainText): # building output
        for j in range(0,5):
            if plainText[i] in keySqr[j]:
                r1 = j
                c1 = keySqr[j].index(plainText[i])
            if plainText[i+1] in keySqr[j]:
                r2 = j
                c2 = keySqr[j].index(plainText[i+1])
        i += 2
    
        if r1 == r2:
            if c1 == 4:
                output += keySqr[r1][0]
            else:
                output += keySqr[r1][c1+1]
            if c2 == 4:
                output += keySqr[r1][0]
            else:
                output += keySqr[r1][c2+1]
        elif c1 == c2:
            if r1 == 4:
                output += keySqr[0][c1]
            else:
                output += keySqr[r1+1][c1]
            if r2 == 4:
                output += keySqr[0][c1]
            else:
                output += keySqr[r2+1][c2]
        else:
                output += keySqr[r1][c2]
                output += keySqr[r2][c1]
        
    print(f'''
    Your secret message:
        {output}
    using the key word \'{keyWord}\'
    ''')

    return()


# ___________________________________________________________________________
# BITWISE CIPHER

def bitwise(plainText): # this does exactly what it should, but not what I was hoping for
    print(' ')
    print('Bitwise Cipher Encoder')
    print(' ')
    translator = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
        'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,
        'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,
        'y':24,'z':25}
    bitSize = 8
    numList = []
    invNums = []
    for i in plainText:
        numList.append(np.uint8(translator[i]))
    for i in numList:
        invNums.append(~i)
    print(numList)
    print(invNums)

    print(f'''
    Your secret message:''')
    for x in invNums:
        print(x)
    print(f'''with a bit key of {bitSize}
    ''')

    return()

# ___________________________________________________________________________
# MAIN PROGRAM

print('''
Welcome to the Secret Message Encoder.
There are currently 6 cipher methods supported:
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Date Cipher
4) Viginere Cipher
5) Playfair Cipher
6) Bitwise Cipher

Your input message will be formatted as such:
thisisyourmessage
before executing the desired cipher and returning
the encoded message. The program will also return 
any necessary keys for your correspondent to decode 
the message.


''')

# May decide to switch to choosing encoding method first; haven't
# decided yet
message = input("What is your secret message? ")
message = message.lower()
message = message.translate({ord(c): None for c in string.whitespace})

trigger = True

while trigger:
    method = input("Which encoding method would you like to use? ")
    method = method.lower()
    message = message.translate({ord(c): None for c in string.whitespace})
    if method == '1' or method == 'caesarcipher' or method == 'caesar':
        trigger = False
        caesar(message)
    elif method == '2' or method == 'monoalphabeticcipher' or method == 'monoalphabetic':
        monoalphabetic(message)
        trigger = False
    elif method == '3' or method == 'datecipher' or method == 'date':
        date(message)
        trigger = False
    elif method == '4' or method == 'viginerecipher' or method == 'viginere':
        viginere(message)
        trigger = False
    elif method == '5' or method == 'playfaircipher' or method == 'playfir':
        playfair(message)
        trigger = False
    elif method == '6' or method == 'bitwisecipher' or method == 'bitwise':
        bitwise(message)
        trigger = False
    else:
        os.system('cls')
        print('''
    --Please choose a valid encoding method--
    
There are currently 6 cipher methods supported:
1) Caesar Cipher
2) Monoalphabetic Cipher
3) Date Cipher
4) Viginere Ciper
5) Playfair Cipher
6) Bitwise Cipher

        ''')
        time.sleep(1)

else:
    print(' ')
    print(' ')
    playAgain = input("Would you like to encode another message? (Y/N) ")
    playAgain = playAgain.lower()
    if playAgain == 'y' or playAgain == 'yes':
        os.system('CLS')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])


    
