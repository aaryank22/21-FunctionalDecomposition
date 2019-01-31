"""
Hangman.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random
def main():
   words = wordstolist()
   selectedword = selectrandomword(words)
   answer = minlength(words)
   print(answer)
   guess(words)
   # stage5()
   # stage6()
   # stage7()
   # stage8()



def wordstolist():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
    words = string.split()
    # print(words)
    return words


def selectrandomword(words):
    r = random.randrange(0, len(words))
    item = words[r]
    print(item)
    return item

def minlength(words):
    print('what is the minimum length you want for the word')
    y = int(input('Enter an Integer'))
    while True:
        selectedword = selectrandomword(words)

        if len(selectedword) > y:
            return selectedword

def guess(selectedword):
    z =input('Enter a String')
    while True:
        if z in selectedword:
            return



main()

