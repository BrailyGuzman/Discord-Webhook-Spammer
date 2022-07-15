import os
from time import sleep

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

try:
    from colorama import Fore, init
except ImportError:
    os.system('pip install colorama')
    from colorama import Fore, init

init(autoreset=False)
print(f"{Fore.GREEN}Discord Webhook Spammer {Fore.WHITE}| {Fore.LIGHTRED_EX}Braily Guzman")
sleep(2)

os.system('cls')
print(f"{Fore.LIGHTRED_EX}Webhook URL {Fore.WHITE}")
webhook = input("[ENTER]: ")
os.system('cls')
print(f"{Fore.LIGHTRED_EX}Message{Fore.WHITE}")
text = input("[ENTER]: ")

proxy = set()
with open("proxies.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())

proxies = {
    'http': 'http://'+line1
    }

sent = 0
os.system('cls')
while True:
    Message = {
        "content": text
    }
    requests.post(webhook, data=Message, proxies=proxies)
    sent += 1

    print(f"{Fore.LIGHTRED_EX}[SENT] {Fore.GREEN}{sent}", end='\r')
    sleep(1)