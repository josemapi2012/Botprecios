import requests
from bs4 import BeautifulSoup
import time

def AirForce():
    URL = 'https://www.supremenewyork.com/shop/all/shoes'

    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    zapas = "Supreme®/Nike® Air Force 1"
    #Busca todos los span de la pagina, despues crea un loop en el cual si contiene la palabra guardada en la variable zapas diga que ya esta disponible esas zapatillas
    for i in soup.findAll("a"):
        if (i.get_text().find(zapas) != -1):
            print("Se encontro la zapatilla")
            break
        else:
            x = datetime.datetime.now()
            f = open("log.txt","a")
            f.write(f"{x} - Todavia no estan esos zapatos en supremestore \n")
            f.close()