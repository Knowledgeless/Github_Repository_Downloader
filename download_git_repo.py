#!/usr/bin/python -O
try:
    import requests as rq
    import bs4 as bs
    import os, sys
    import tqdm


    class Colors():
        green = "\033[92m"
        red = "\033[91m"
        warning = "\033[93m"  

    class Banner(Colors):
        def banner(self):
            if sys.platform.lower() == "win32":
                print(Colors.green + '''
                \t\t\t\tWelcome to Github Repo Scraper
                \t_____ _ _   _       _      _____                _____                         
                \t|   __|_| |_| |_ _ _| |_   | __  |___ ___ ___   |   __|___ ___ ___ ___ ___ ___ 
                \t|  |  | |  _|   | | | . |  |    -| -_| . | . |  |__   |  _|  _| .'| . | -_|  _|
                \t|_____|_|_| |_|_|___|___|  |__|__|___|  _|___|  |_____|___|_| |__,|  _|___|_|  
                \t                                     |_|                          |_|      

                \t[+] Ctrl + c to exit forcefully \n\n''')
            elif sys.platform == "linux" or sys.platform == "unix":
                os.system("figlet Github Repo Scraper")
            else:
                pass  

    class CodeScraper(Colors):
        def __init__(self, username):
            self.user = username
            
        def scraper(self):
            
            link = "https://github.com/"+self.user+"?tab=repositories"
            if rq.get(link).status_code == 404:
                print("\n\n\t\tOppss, Invalid Username. Try Again..!\n\n")

            else:
                response = rq.get(link).text
                search = bs.BeautifulSoup(response, 'html.parser')
                source = search.find_all('a')
                links = []

                os.system("mkdir {}".format(self.user))
                os.chdir("{}".format(self.user))

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
            for i in self.scr:
                d_link = "https://github.com"+i+".git"
                print(Colors.warning + "\nDownloading Repository: {}".format(d_link))
                os.system("git clone {}".format(d_link))
                print(Colors.green + "Download Completed..!".format(i))


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
        os.system("pip3 install tqdm")
    else:

        print(Colors.warning+"\n\t\tExiting Code...Bye...Bye...!\n")
        exit()
except KeyboardInterrupt:
    print(Colors.warning+"\n\n\t\tExiting Code...Bye...Bye...!\n")
except Exception as e:
    print(Colors.warning + "\n\n\t\tYou are facing this issue: {}\n\n".format(e))
