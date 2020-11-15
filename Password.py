import requests
from bs4 import BeautifulSoup
import datetime
import os

def passworld():
    URL = 'https://cactusplantfleamarket.com/password'

    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    password = soup.findAll("div", {"class" : "Password"})

    if password:
        x = datetime.datetime.now()
        f = open("log.txt","a")
        f.write(f"{x} - Todavia tiene contrasena la pagina \n")
        f.close()
    else:
        os.system(f"telegram-send 'La pagina no tiene contraseña'")