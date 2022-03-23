#Coded by EmADs
#Use for legal purposes only!
#Enjoy!

import os
from simple_colors import *
from requests import get

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole() 

print(yellow("""
    ___       __          _          _______           __         
   /   | ____/ /___ ___  (_)___     / ____(_)___  ____/ /__  _____
  / /| |/ __  / __ `__ \/ / __ \   / /_  / / __ \/ __  / _ \/ ___/
 / ___ / /_/ / / / / / / / / / /  / __/ / / / / / /_/ /  __/ /    
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/  /_/   /_/_/ /_/\__,_/\___/_/     
.----------------------------------.
|#Author: Seyed Emad Reza Ghahhari |      
|#GitHub: EmADsec                  |
|#Discord: EmADs#4017              |
'----------------------------------'                       
""")) 

target = input(blue("Enter The Target Website: "))
target = "http://"+Target
wl = input(blue("Select a WordList File: "))
wl = open(WL,"r").read().splitlines()

print(""

"")

for url in wl:
    full_address = target+"/"+url
    respons = get(full_address)
    if respons.status_code == 200:
       print(green(f" {full_address} ===> [*] Admin Page Found!"))
    else:
       print(red(f" {full_address} ===> Error 404!"))
       
       
      
        
#Coded by EmADs
#Pls don't change the source code!
#Stay safe
