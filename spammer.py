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

#Input 
os.system('cls')
print(f"{Fore.LIGHTRED_EX}Webhook URL {Fore.WHITE}")
webhook = input("[ENTER]: ")
os.system('cls')
print(f"{Fore.LIGHTRED_EX}Message{Fore.WHITE}")
text = input("[ENTER]: ")

#Proxies
proxies = open("proxies.txt", "r").readlines()


sent = 0
os.system('cls')

#Spam
while True:
    for proxy in proxies:
        proxy_dict = {"http": f"http://{proxy.rstrip()}"}
        payload = {
            "content": text
        }
        requests.post(webhook, data=payload, proxies=proxy_dict)
        sent += 1

        print(f"{Fore.LIGHTRED_EX}[SENT] {Fore.GREEN}{sent}", end='\r')
        # You can get rate limited very quickly, if you set sleep as 2 or 3 you should be good.
        sleep(2)
