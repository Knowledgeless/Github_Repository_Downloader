
# Modules 
from lib2to3.pgen2 import grammar
import requests as rq
import bs4 as bs
import os




class Colors():
    green = "\033[92m"
    red = "\033[91m"
    warning = "\033[93m"    


class CodeScraper(Colors):
    def __init__(self, url):
        self.user = url

    def banner(self):
        print(Colors.red + '''
        \t\t\t\tWelcome to Github Repo Scraper
        \t_____ _ _   _       _      _____                _____                         
        \t|   __|_| |_| |_ _ _| |_   | __  |___ ___ ___   |   __|___ ___ ___ ___ ___ ___ 
        \t|  |  | |  _|   | | | . |  |    -| -_| . | . |  |__   |  _|  _| .'| . | -_|  _|
        \t|_____|_|_| |_|_|___|___|  |__|__|___|  _|___|  |_____|___|_| |__,|  _|___|_|  
        \t                                     |_|                          |_|          
        ''')
    
    def scraper(self):
        
        link = "https://github.com/"+self.user+"?tab=repositories"
        response = rq.get(link).text
        search = bs.BeautifulSoup(response, 'html.parser')
						# detecting urls
        source = search.find_all('a')
        links = []
        
        for i in source:
            link =  i.get('href')
		    # checking href is a url or not
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
            print(Colors.warning + "Downloading Repository: {}".format(d_link))
            os.system("git clone {}".format(d_link))
            print(Colors.green + "Completed..!")


if __name__ == "__main__":
    
    user = input("Enter your username: ")

    obj = CodeScraper(user)
    obj.banner()
    obj1 = DownloadCode(user)
    obj1.names()
