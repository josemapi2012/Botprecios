import requests
from bs4 import BeautifulSoup
import os
import datetime

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}


def switch():
    page = requests.get('https://www.amazon.es/Nintendo-Switch-Consola-color-Modelo/dp/B07W13KJZC/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nintendo+switch&qid=1604946320&sr=8-3https://www.amazon.es/Nintendo-Switch-Consola-color-Modelo/dp/B07W13KJZC/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=nintendo+switch&qid=1604946320&sr=8-3', headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price =(price[0:3])
    
    if (int(converted_price) < 296):
    	os.system(f"telegram-send 'El precio de la nintendo switch es  '{converted_price}")
    else:
            x = datetime.datetime.now()
            f = open("log.txt","a")
            f.write(f"{x} - La nintendo switch todavia no ha bajado de precio \n")
            f.close()