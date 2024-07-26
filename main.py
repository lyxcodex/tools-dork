import os, pyfiglet
import subprocess
import sys
import requests

def pear(text):
    print(text)
    
def banner(text):
    banner = pyfiglet.figlet_format(text)
    print(banner)

os.system("clear")

def update():
    if ".git" in os.listdir():
        _ = subprocess.run(["git", "stash"], check=True)
        _ = subprocess.run(["git", "pull"], check=True)
    else:
        source = requests.get(
            "https://raw.githubusercontent.com/lyxcodex/tools-dork/main/main.py"
        ).content
        with open("main.py", "wb") as file:
            file.write(source)
            
def main():
    while True:
        banner("PELIMUCILIK")
        print("""
        1. Engine Single V1
        2. Engine Single V2 [ HOT🔥 ]
        3. Engine Ask.com
        4. Engine Yahoo.com
        5. update
        o. exit""")
        jembut_galau = input("\nchoose~# ")
        if jembut_galau == "1":
            os.system("python3 ./dork/google.py")
        elif jembut_galau == "2":
            os.system("python3 ./dork/bing.py")
        elif jembut_galau == "3":
            os.system("python3 ./dork/ask.py")
        elif jembut_galau == "4":
            os.system("python3 ./dork/yahoo.py")
        elif jembut_galau == "5":
            update()
            print("dah")
        elif jembut_galau == "o":
            print("out")
            break
        else:
            print("inputmu salah")
            
if __name__ == "__main__":
    main()
