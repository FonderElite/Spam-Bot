import pyautogui
import os
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
print(
    Fore.BLUE +
    '''

  █████████                                                 ███████████            █████   
 ███░░░░░███                                               ░░███░░░░░███          ░░███    
░███    ░░░  ████████   ██████   █████████████              ░███    ░███  ██████  ███████  
░░█████████ ░░███░░███ ░░░░░███ ░░███░░███░░███  ██████████ ░██████████  ███░░███░░░███░   
 ░░░░░░░░███ ░███ ░███  ███████  ░███ ░███ ░███ ░░░░░░░░░░  ░███░░░░░███░███ ░███  ░███    
 ███    ░███ ░███ ░███ ███░░███  ░███ ░███ ░███             ░███    ░███░███ ░███  ░███ ███
░░█████████  ░███████ ░░████████ █████░███ █████            ███████████ ░░██████   ░░█████ 
 ░░░░░░░░░   ░███░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░            ░░░░░░░░░░░   ░░░░░░     ░░░░░  
             ░███                                                                          
             █████                                                                         
            ░░░░░             
 '''
)
print(Fore.GREEN + "Made By Droid || FonderElite")
print(Fore.GREEN + "Visit My GitHub: https://github.com/fonderelite")
cool = os.getcwd()
print("Your current working directory is: " + cool)
time.sleep(2)
help = Fore.YELLOW + '''
|-------------------------------------|
|[+]Commands:                         |
|[+]-h help                           |
|[+]-f file                           |
|[+]-o open file                      |
|[+]-v verbose                        |
|[+]-s start                          |
|ex. ./spambot -f file.txt -s      |
|-------------------------------------|
'''
print(Fore.YELLOW + '''
|-------------------------------------|
|[+]Commands:                         |
|[+]-h help                           |
|[+]-f file                           |
|[+]-o open file                      |
|[+]-v verbose                        |
|[+]-s start                          |
|ex. ./spambot -f  -s              |
|-------------------------------------|
''')
while True:
 first = input("Enter a command: ")
 if first == "./spambot -h":
    print(help)
 elif first == "./spambot -f":
    print("Input a file location to open:")
    print(open(input(), 'r'))
    print(Fore.RED + "File opened but not executed")
    print(Fore.RED + "Try again")

    first = input("Enter a command:")
 elif first == "./spambot -o":
    print("Input a file location to open:")
    print(open(input(), 'r'))
    print(Fore.RED + "File opened but not executed")
    print(Fore.RED + "Try again")
    first = input("Enter a command:")

 elif first == "./spambot -f -v -s":
    print("Entering Verbose mode....")
    time.sleep(2)
    print(Fore.GREEN + "OK!")
    print("Input a file location to open:")
    c = open(input(), 'r')
    print("Spamming in 5s")
    time.sleep(5)
    for word in c:
        pyautogui.typewrite(word)
        time.sleep(1)
        pyautogui.press("enter")
 elif first == "./spambot -o -v -s":
    print("Input a file location to open:")
    g = open(input(), 'r')
    p = open(input(), 'r')
    print('Spamming in 5s')
    time.sleep(5)
    for worde in g:
        pyautogui.typewrite(worde)
        time.sleep(0.5)
        pyautogui.press("enter")
        for wordo in p:
            pyautogui.typewrite(wordo)
            time.sleep(0.5)
            pyautogui.press("enter")


 elif first == "./spambot":
    print(help)
 elif first == "./spambot -f -s":

    print("Input a file location to open:")
    k = open(input(), 'r')
    print('Spamming in 5s')
    time.sleep(5)
    for word in k:
        pyautogui.write(word)
        time.sleep(0.5)
        pyautogui.press("enter")

 elif first == "spambot -v":
    print("Entering verbose mode..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print("........")
    print(Fore.RED + "Your in verbose mode but not executed.")
    print(Fore.RED + "Try again")
    first = input("Enter a command:")
 else:
    print(Fore.RED + '''

░█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ █ 
░█▀▀▀ █▄▄▀ █▄▄▀ █──█ █▄▄▀ ▀ 
░█▄▄▄ ▀─▀▀ ▀─▀▀ ▀▀▀▀ ▀─▀▀ ▄
    ''')
