import argparse
import time
import os
import random
from googlesearch import search
from colorama import Fore, init

def kitty(text):
    print(text)

os.system('clear')
BAN = """
            This Tools Created By LyxCodex
      Enjoy using the tools that I have provided
to check updates on git pull or in the main tools, thank you"""

def uagen(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

UserAgent = uagen('.uagen_list.txt')

def randomuser():
    return random.choice(UserAgent)

def uamati(mati):
    with open("ua-mati.log", 'a') as log:
        log.write(f"{mati}\n")

def dorker(dork, taldork):
    kitty(f"{Fore.MAGENTA}looking for the target website..{Fore.RESET}")
    count = 0
    while count < taldork:
        uamu = randomuser()
        try:
            for result in search(dork, num=10, user_agent=uamu):
                kitty(result)
                with open("result.txt", 'a') as f:
                    f.write(f"{result}\n")
                time.sleep(1)
                count += 1
                if count >= taldork:
                    return
        except Exception as e:
            if "429" in str(e):
                kitty(f"{Fore.RED}Too many requests detected [UserAgent - Off] - Change new UserAgent{Fore.RESET}")
                uamati(uamu)
                time.sleep(2)
            elif "404" in str(e):
                kitty(f"{Fore.RED}404 Not Found - Skip{Fore.RESET}")
            else:
                kitty(f"{Fore.MAGENTA}the website cannot be entered{Fore.RESET}")
                break

if __name__ == '__main__':
    init(autoreset=True)
    print(BAN)
    parser = argparse.ArgumentParser()
    parser.add_argument("-dork", dest="dork", help="Ex: intext:KEYWORD")
    args = parser.parse_args()
    
    if args.dork:
        dork = args.dork
    else:
        dork = input("dorkmu: ")
        
    taldork = min(int(input("total max 1k: ")), 1000)
    dorker(dork, taldork)
    
    simpan = input("disave ga? y/n ")
    if simpan == 'y':
        name = f"{taldork}.txt"
        with open(name, 'w') as file:
            file.write(f"{dork}\n")
            for result in search(dork, num=500, user_agent=randomuser()):
                file.write(result + '\n')
        print(f"saved on {name}")
    else:
        print("thank you")
      
