import argparse
import time
import os
import random
import requests
from bs4 import BeautifulSoup
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

def yahoo_search(query, user_agent):
    headers = {
        'User-Agent': user_agent
    }
    url = f'https://search.yahoo.com/search?p={query}&fr=yfp-hrmob&fr2=p%3Afp%2Cm%3Asb&.tsrc=yfp-hrmob&ei=UTF-8&fp=1&toggle=1&cop=mss'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='dd algo algo-sr Sr')
    return [result.find('a')['href'] for result in results if result.find('a')]

def dorker(dork, taldork):
    kitty(f"{Fore.MAGENTA}looking for the target website..{Fore.RESET}")
    count = 0
    while count < taldork:
        uamu = randomuser()
        try:
            results = yahoo_search(dork, uamu)
            for result in results:
                kitty(result)
                with open("result.txt", 'a') as f:
                    f.write(f"{result}\n")
                time.sleep(1)  # Reduced sleep time to 1 second
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
            results = yahoo_search(dork, randomuser())
            for result in results:
                file.write(result + '\n')
        print(f"saved on {name}")
    else:
        print("thank you")
        
