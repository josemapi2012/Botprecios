import requests
from bs4 import BeautifulSoup
import smtpd

URL = {'https://www.amazon.es/Xiaomi-Tel%C3%A9fono-Pantalla-Octa-Core-Procesador/dp/B08B1GVJ9J/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=redmi+9&qid=1604832504&quartzVehicle=93-1829&replacementKeywords=redmi&sr=8-2',
'https://www.amazon.es/Nintendo-Switch-Consola-color-Modelo/dp/B07WKNQ8JT/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=NZ64WV1QMFAG&dchild=1&keywords=nintendo+switch+consola&qid=1604851874&sprefix=nitendo+sw%2Caps%2C205&sr=8-1'}

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'}


for i in URL:
    
    page = requests.get(i, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price =(price[0:3])
    
    print(converted_price)

