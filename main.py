# the end. (by rinfysbanned and swedewtf)

from colorama import Fore, Style, init
init(convert=True)
import requests
import os
import time
import threading

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE

threads = []
num_threads = 10

def main():
    os.system("cls && title The End ┃^┃ @swedewtf @rinfysbanned")
    print(fr"""{red}                                           

    ████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
    ╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
    ░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
    ░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
    ░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░   
                                                                    
    > {white}developed by @swedewtf, @rinfysbanned (the end :moyai: :wine:)
    """)
    choice = str(input(f"{white}[{red}END{white}] Choice >>> "))
    if choice in ["01", "1", "one"]:
        selfbot.spamchannels()
    if choice in ["02", "2", "two"]:
        selfbot.webhookspam()
    if choice in ["03", "3", "three"]:
        selfbot.banall()

class selfbot:
    def banall():
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }
        members = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/members-search", headers=headers).json()
        print(members)
        while True:
            for member in members:
                banreq = requests.put(f"https://discord.com/api/v9/guilds/{guildid}/bans/{member}", headers={"Authorization": token})
                if banreq.status_code in [200, 201, 204]:
                    print(f"{green} [+] Banned {member}")
                    with open("bannedmembers.txt", "a") as bannedamount:
                       bannedamount.append(member)
                elif "retry_after" in banreq.text:
                    time.sleep(banreq.json()['retry_after'])
                else:
                    print(f"{red}{banreq.text}")
                    break
    

    def webhookspam():
        yes = input(f"{white}[{red}END{white}] Are you sure? (Y or N)")
        if yes == "Y" or yes == "y" or yes == "yes":
            channel_id = input(f"{white}[{red}END{white}] Enter channel ID for webhook: ")
            headers = {
                "Authorization": token,
                "Content-Type": "application/json",
            }
            webhook_ids = "test"
            guild_id = 1132072878263762994
            real12 = {"name": "stellar owns u"}
            test23 = {"content": "stellar owns u"}
            test123 = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/webhooks", headers=headers).json
            urls = test123.content
            things12 = requests.get(f"https://discord.com/api/guilds/{guild_id}/channels", headers=headers)
            channels = things12.json()
            print(channels)
            for channel in channels:
                for url in urls:
                    spam = requests.post(url, headers=headers, json=test23)
                    print(spam.content)

    def spamchannels():
            yes = input(f"{white}[{red}END{white}] Are you sure? (Y or N)")
            if yes == "Y" or "y" or "yes":
                print(f"{white}[{red}END{white}] its joeover.")
                time.sleep(1)
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json",
                }
                real = {"name": "stellar owns u"} 
                test1 = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/preview", headers=headers)
                if test1.status_code>205:
                    print(f"{red}[-] ERR: The guild ID doesnt exist")
                    time.sleep(3)
                    main()
                elif test1.status_code == 200 or 201 or 202 or 203:
                    print(f"{green}[+] The guild ID exists (Continuing process)")
                    i=1
                    while i<10:
                        spam = requests.post(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers=headers, json=real)
                        if spam.status_code == 201:
                            print(f"{green}[+] Created channel")
                        else:
                            while spam.status_code<201:
                                spam = requests.post(f"https://discord.com/api/v9/guilds/{guildid}/channels", headers=headers, json=real)
                                print(f"{green}[+] Trying to create")

guildid = input(f"{white}[{red}END{white}] Server ID: ")
token = input(f"{white}[{red}END{white}] Enter selfbot token (must have admin in server): ")

main()