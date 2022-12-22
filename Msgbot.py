##simple msgbot to write on screen Hello in different languages

import pyautogui as py
import time

time.sleep(2)
text = 'How to say hello in: '
languages = open('languages.txt', 'r')

for language in languages:
    py.write(text+ ' ' + language)
    py.press('Enter')
