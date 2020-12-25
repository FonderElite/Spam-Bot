import pyautogui
import os
import time
print(
    '''
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████──────────██████────────────────██████████████───██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██────────────────██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██────────────────██░░██████░░██───██░░██████░░██─██████░░██████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██████░░██████░░██────────────────██░░██──██░░██───██░░██──██░░██─────██░░██─────
─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██──██░░██──██░░██─██████████████─██░░██████░░████─██░░██──██░░██─────██░░██─────
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─────██░░██─────
─██████████░░██─██░░██████████─██░░██████░░██─██░░██──██████──██░░██─██████████████─██░░████████░░██─██░░██──██░░██─────██░░██─────
─────────██░░██─██░░██─────────██░░██──██░░██─██░░██──────────██░░██────────────────██░░██────██░░██─██░░██──██░░██─────██░░██─────
─██████████░░██─██░░██─────────██░░██──██░░██─██░░██──────────██░░██────────────────██░░████████░░██─██░░██████░░██─────██░░██─────
─██░░░░░░░░░░██─██░░██─────────██░░██──██░░██─██░░██──────────██░░██────────────────██░░░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────
─██████████████─██████─────────██████──██████─██████──────────██████────────────────████████████████─██████████████─────██████─────
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────   '''
)
print("Made By Droid || FonderElite")
print("Visit My GitHub: https://github.com/fonderelite")
cool = os.getcwd()
print("Your current working directory is: " + cool)
time.sleep(2)
help = '''
|-------------------------------------|
|[+]Commands:                         |
|[+]-h help                           |
|[+]-f file                           |
|[+]-o open file                      |
|[+]-v verbose                        |
|[+]-s start                          |
|ex. python3 spambot.py -f file.txt -s|
|-------------------------------------|
'''
print('''
|-------------------------------------|
|[+]Commands:                         |
|[+]-h help                           |
|[+]-f file                           |
|[+]-o open file                      |
|[+]-v verbose                        |
|[+]-s start                          |
|ex. python3 spambot.py -f  -s        |
|-------------------------------------|
''')

first = input("Enter a command: ")
if first == "python3 spambot.py -h ":
    print(help)
elif first == "python3 spambot.py -f":
    print("Input a file location to open:")
    print(open(input(), 'r'))
    print("File opened but not executed")
    print("Try again")
    first = input("Enter a command:")
elif first == "python3 spambot.py -o":
    print("Input a file location to open:")
    print(open(input(), 'r'))
    print("File opened but not executed")
    print("Try again")
    first = input("Enter a command:")

elif first == "python3 spambot.py -f -v -s":
    print("Input a file location to open:")
    c = open(input(), 'r')
    for word in c:
        pyautogui.typewrite(word)
        time.sleep(5)
        pyautogui.press("enter")

elif first == "python3 spambot.py -o -v -s":
        print("Input a file location to open:")
        g = open(input(), 'r')
        p = open(input(), 'r')
        for worde in g:
            pyautogui.typewrite(worde)
            time.sleep(5)
            pyautogui.press("enter")
            for wordo in p:
                pyautogui.typewrite(wordo)
                time.sleep(5)
                pyautogui.press("enter")


elif first == "python3 spambot.py ":
    print(help)
elif first == "python3 spambot.py -f -s":

    print("Input a file location to open:")
    k = open(input(), 'r')

    for word in k:
        pyautogui.typewrite(word)
        time.sleep(5)
        pyautogui.press("enter")

elif first == "python3 spambot.py -v":
    print("Entering verbose mode..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    print("Your in verbose mode but not executed.")
    print("Try again")
    first = input("Enter a command:")
else:
    print('''
    
░█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ █ 
░█▀▀▀ █▄▄▀ █▄▄▀ █──█ █▄▄▀ ▀ 
░█▄▄▄ ▀─▀▀ ▀─▀▀ ▀▀▀▀ ▀─▀▀ ▄
    ''')
