#!/usr/bin/python -O

try:
    import requests as rq
    import bs4 as bs
    import os, sys


    class Colors():
        green = "\033[92m"
        red = "\033[91m"
        warning = "\033[93m"  

    class Banner(Colors):
        def banner(self):
            if sys.platform.lower() == "win32":
                print(Colors.green + '''
                \t\t\t\tWelcome to Github Repo Scraper
\t              ________.__  __  .__         ___.     __________                           .__  __                        ________                      .__                    .___            
\t /  _____/|__|/  |_|  |__  __ _\_ |__   \______   \ ____ ______   ____  _____|__|/  |_  ___________ ___.__. \______ \   ______  _  ______ |  |   _________     __| _/___________ 
\t/   \  ___|  \   __\  |  \|  |  \ __ \   |       _// __ \\____ \ /  _ \/  ___/  \   __\/  _ \_  __ <   |  |  |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \
\t\    \_\  \  ||  | |   Y  \  |  / \_\ \  |    |   \  ___/|  |_> >  <_> )___ \|  ||  | (  <_> )  | \/\___  |  |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
\t \______  /__||__| |___|  /____/|___  /  |____|_  /\___  >   __/ \____/____  >__||__|  \____/|__|   / ____| /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   
\t        \/              \/          \/          \/     \/|__|              \/                       \/              \/                  \/                \/      \/    \/       

                \t[+] Ctrl + c to exit forcefully \n\n''')
            elif sys.platform == "linux" or sys.platform == "unix":
                os.system("figlet Github Repo Scraper")
            else:
                pass  

    class CodeScraper(Colors):
        def __init__(self, username):
            self.user = username
            
        def scraper(self):
            links = []
            link = "https://github.com/"+self.user+"?tab=repositories"
            
            if rq.get(link).status_code == 404:
                print("\n\n\t\tOppss, Invalid Username. Try Again..!\n\n")

            else:
                response = rq.get(link).text
                search = bs.BeautifulSoup(response, 'html.parser')
                source = search.find_all('a')
                

                for i in source:
                    link =  i.get('href')
                    if link.startswith("/{}/".format(self.user.title())):
                        links.append(link)
                    elif link.startswith("/{}/".format(self.user)):
                        links.append(link)
                    
            return links
        
    class DownloadCode(CodeScraper):

        def names(self):
            self.scr = CodeScraper.scraper(self)
            if len(self.scr) !=0 :
                choice = input("Total {} repository found. Do you want tho download them? (Y/n): ".format(len(self.scr)))
                if choice.lower() == "y":
                    os.system("mkdir {}".format(self.user))
                    os.chdir("{}".format(self.user))

                    for i in self.scr:
                        d_link = "https://github.com"+i+".git"
                        print(Colors.warning + "\nDownloading Repository: {}".format(d_link))
                        os.system("git clone {}".format(d_link))
                        print(Colors.green + "Download Completed..!".format(i))
            else:
                pass

    if __name__ == "__main__":

        while True:
            colors = Colors()
            banner = Banner()
            banner.banner()

            user = input("Enter your username: ")
            if user.startswith("http") or user.endswith(".com") or user.endswith("/"):
                    print(colors.red+"\n\t\tPlease Enter Your Targeted Username Only & Try Again.\n")
                    
            downloader = DownloadCode(user)
            downloader.names()


####### Error Handling Starts #######
    
except ModuleNotFoundError:
    print("""
    \t\tYou have to install these MODULE's
    \t1. bs4
    \t2. requests
    """)
    confirmation = input("\t\tDo you want to install?(Y/n): ")
    if confirmation.lower() == "y":
        print("bs4 Module Installing...")
        os.system("pip3 install bs4")
        print("Requests Module Installing...")
        os.system("pip3 install requests")
        print("tqdm Module Installing...")

    else:
        print(Colors.warning+"\n\t\tExiting Code...Bye...Bye...!\n")
        exit()

except KeyboardInterrupt:
    print(Colors.warning+"\n\n\t\tExiting Code...Bye...Bye...!\n")

except Exception as e:
    print(Colors.warning + "\n\n\t\tYou are facing this issue: {}\n\n".format(e))
