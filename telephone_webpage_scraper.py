#!/usr/bin/env python


from requests_html import HTMLSession 
import re
from bs4 import BeautifulSoup as BS
from bs4 import Comment
import requests
from bs4 import BeautifulSoup

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def printascii():
    print("""
 _____  __    __       __                                                 
/__   \/ / /\ \ \_ __ / _\ ___ _ __ __ _ _ __   ___ _ __                  
  / /\/\ \/  \/ / '_ \\ \ / __| '__/ _` | '_ \ / _ \ '__|                 
 / /    \  /\  /| |_) |\ \ (__| | | (_| | |_) |  __/ |                    
 \/      \/  \/ | .__/\__/\___|_|  \__,_| .__/ \___|_|                    
                |_|                     |_|                               
            
               By Luca Romano - CyberAuror                        
          """)

printascii()

url=input("Inserisci la pagina-web Target:  ")
telephone_regex=r"\b[\s(.)\d-]{6,}\d\b"


session = HTMLSession()
response = session.get(url)

response.html.render()

body = response.html.find("body")[0]

#estrazione numeri telefono
numbers = re.findall(r"\b[\s(.)\d-]{6,}\d\b", body.text)
for index,number in enumerate(numbers):
    print("")
    print("------->","Numero di telefono", index+1, ":")
    print("")
    print(numbers)
    print("")
    print("----------------------------------------------------------------------------------------------------")
    print("")