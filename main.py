import os
import random

def readfile():
    with open('words.txt' , 'r') as file:
        words = file.readlines()
        currword = random.choice(words)
        return currword

def takeip(L):
    global tries
    t = True
    while (t):
        os.system("cls")
        print(currentword, "(hidden from user)")
        print("==========================")
        print("\nTrials left: ", tries)
        print("\nWord So Far: ", hidingListToStr)
        letter = input("\nenter a letter: ")
        if len(letter) > 1:
            letter = letter[0]
        if letter == '':
            print("invalid ip")
            input()
            continue
        if letter.lower() in L:
            print("\nyou've entered this letter before")
            input()
        else:
            history_list.append(letter)
            t = False
            return letter


checkletter = lambda checkl, checkw: True if checkl in checkw else False


def hide(w, crctlist, lttr):
    global hidingListToStr, hidingList

    indices = [i for i, char in enumerate(wordAsList) if char == lttr]  # Using enumerate
    hidingList = [lttr if idx in indices else hidingList[idx] for idx in range(len(wordAsList))]
    hidingListToStr = ''.join([c if c in crctlist else "_" for c in w])
    print("\nWord is: ", hidingListToStr)

    input()
    if '_' not in hidingList:
        print("\nYou Guessed Correctly")
        input()
        global flag
        flag = False

tries = 6
currentword = readfile()
history_list = []  # to stop re0
correct_list = []
wordAsList = list(currentword.strip())
hidingList = ['_'] * len(wordAsList)
hidingListToStr = ''.join([str(item) for item in hidingList])

flag = True
while(flag):
    os.system("cls")
    ltr = takeip(history_list)
    checkresult = checkletter(ltr, currentword)
    if checkresult == True:
        print("\nCorrect guess")
        correct_list.append(ltr)
        hide(currentword, correct_list,ltr)
    else:
        print("\nWrong guess")
        tries-=1
        input()
        if tries==0:
            print("\nGame over, you couldn't guess")
            input()
            flag = False
