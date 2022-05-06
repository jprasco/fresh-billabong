# 
# iCountTs.py
# enter a url and I will count and return all of the letter t's on the page.
#

import os
import sys
import subprocess
from collections import Counter
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests
import time

def is_good_length(letIn):
    if len(letIn) == 1:
        return(True)
    else:
        return(False)

os.system('cls')
print(' ')
# url = 'https://jprasco.com/'
# ^^ should have 58 I think
url = input("Paste your url: ")
time.sleep(1)
searchLetter = input("Which letter would you like to count? ")
while not is_good_length(searchLetter):
    os.system('cls')
    print('I can only count 1 letter at a time!')
    searchLetter = input("Which letter would you like to count? ")

searchLetter.lower()

print(' ')
print('Counting...')
print(' ')
#htmlContent = requests.get(url).text
#soup = BeautifulSoup(htmlContent, 'lxml')
#print(soup.prettify())

#___________________________________________________________________
# got this bit from stack overflow. I have yet to completely understand it but it works great 
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen(url).read()
#___________________________________________________________________
clean = text_from_html(html)
clean = clean.lower()
letterCount = Counter(clean)

print('Done!')
time.sleep(1.5)
os.system('cls')
print(' ')
print(f'Your webpage has {letterCount[searchLetter]} {searchLetter}\'s on it!')
print(' ')
print(' ')
playAgain = input('Count Again? (y/n) ')

if playAgain == 'y':
    os.system('CLS')
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
elif playAgain == 'n':
    os.system('CLS')
else:
    print('Oops! Something went wrong.')
    print('Let\'s start from the beginning!')
    time.sleep(3)
    os.system('CLS')
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])


