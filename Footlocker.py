import requests
from bs4 import BeautifulSoup
import datetime
import os


def HighMocha():
    URL = 'https://www.footlocker.es/es/search?query=Jordan%201%20High%20Mocha'

    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    zapas = "Jordan 1 High Mocha"
    #Busca todos los span de la pagina, despues crea un loop en el cual si contiene la palabra guardada en la variable zapas diga que ya esta disponible esas zapatillas
    for i in soup.findAll("span", {"class" : "ProductName-primary"}):
        if (i.get_text().find(zapas) != -1):
            os.system(f"telegram-send 'Una variante de las High Mocha esta disponible en Footlocker'")
            break
        else:
            x = datetime.datetime.now()
            f = open("log.txt","a")
            f.write(f"{x} - No esta disponible las high mocha en footlocker \n")
            f.close()
            break

def CourtPurple():
    URL = 'https://www.footlocker.es/es/search?query=Nike%20Air%20Jordan%201%20High%20Court%20Purple'

    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    zapas = "Air Jordan 1 Low"
    #Busca todos los span de la pagina, despues crea un loop en el cual si contiene la palabra guardada en la variable zapas diga que ya esta disponible esas zapatillas
    for i in soup.findAll("span", {"class" : "ProductName-primary"}):
        if (i.get_text().find(zapas) != -1):
            os.system(f"telegram-send 'Una variante de las Jordan 1 Low esta disponible en Footlocker'")
            break
        else:
            x = datetime.datetime.now()
            f = open("log.txt","a")
            f.write(f"{x} - No esta disponible las Jordan Air Court Purple en footlocker \n")
            f.close()
            break

def sbDunkLow():
    URL = 'https://www.footlocker.es/es/search?query=nike%20sb%20Dunk%20Low'

    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    zapas = "nike sb dunk low"
    #Busca todos los span de la pagina, despues crea un loop en el cual si contiene la palabra guardada en la variable zapas diga que ya esta disponible esas zapatillas
    for i in soup.findAll("span", {"class" : "ProductName-primary"}):
        if (i.get_text().find(zapas) != -1):
            os.system(f"telegram-send 'Una variante de las sb Dunk Low esta disponible en Footlocker'")
            break
        else:
            x = datetime.datetime.now()
            f = open("log.txt","a")
            f.write(f"{x} - No esta disponible las sb Dunk Low en footlocker \n")
            f.close()
            break


def sbDunkHigh():
    URL = 'https://www.footlocker.es/es/search?query=nike%20sb%20Dunk%20High'

    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    zapas = "nike sb dunk high"
    #Busca todos los span de la pagina, despues crea un loop en el cual si contiene la palabra guardada en la variable zapas diga que ya esta disponible esas zapatillas
    for i in soup.findAll("span", {"class" : "ProductName-primary"}):
        if (i.get_text().find(zapas) != -1):
            os.system(f"telegram-send 'Una variante de las sb Dunk High esta disponible en Footlocker'")
            break
        else:
            x = datetime.datetime.now()
            f = open("log.txt","a")
            f.write(f"{x} - No esta disponible las sb Dunk High en footlocker \n")
            f.close()
            break


def prueba():
    URL = 'https://www.footlocker.es/es/search?query=Air'

    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    zapas = "Air"
    #Busca todos los span de la pagina, despues crea un loop en el cual si contiene la palabra guardada en la variable zapas diga que ya esta disponible esas zapatillas
    for i in soup.findAll("span", {"class" : "ProductName-primary"}):
        if (i.get_text().find(zapas) != -1):
            os.system(f"telegram-send 'La prueba fue completada con exito'")
            break
        else:
            x = datetime.datetime.now()
            f = open("log.txt","a")
            f.write(f"{x} - No funciono la prueba \n")
            f.close()
            break