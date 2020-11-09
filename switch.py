import requests
from bs4 import BeautifulSoup
import os
URL = 'https://www.amazon.es/Xiaomi-Tel%C3%A9fono-Pantalla-Octa-Core-Procesador/dp/B08B1GVJ9J/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=redmi+9&qid=1604832504&quartzVehicle=93-1829&replacementKeywords=redmi&sr=8-2'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price =(price[0:3])
    
    
    if (int(converted_price) < 146):
    	os.system(f"telegram-send 'El precio del movil es '{converted_price}")

check_price()
