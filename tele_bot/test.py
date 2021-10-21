import requests
from bs4 import BeautifulSoup

url = 'https://www.zabka.pl/produkty/szukaj-piwa-po-kolorze-polki'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
lista = soup.find_all('div', class_='grid__col -auto-height -col-sm-6 -col-md-4 -col-xl-3')
piwa=[]
quote={}
for x in lista:
    quote['alkohol']= x.img['alt']
    quote['cena']= (x.select_one("span.price.product__price").text[9])+"."+(x.select_one("span.price.product__price").text[10:12])
    piwa.append(quote.copy())

#kurwa = str(piwa)
print(piwa)