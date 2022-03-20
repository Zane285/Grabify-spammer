import requests, os
import numpy as np
from time import sleep

print("THIS WILL USE YOUR OWN IP TO SPAM")
sleep(5)
os.system('cls')

amount = int(input("How many times do you want to spam the link?: "))

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.130 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1'
}
req = requests.Session()
website = input("Enter grabify Link: ")
for x in range(amount):
    fun = req.get(website, headers=headers, allow_redirects=False )
    if fun.status_code == 202 or 200:        
        print(fun.status_code)
    elif fun.status_code == 404:
        print("Not found")
    elif fun.status_code == 403:
        print("Rate limited/Forbidden")
