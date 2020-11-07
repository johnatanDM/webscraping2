import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.gilenofilho.com.br/')

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find('title'))

titulo = soup.find('h3', attrs={'class': 'ctitle'})

print(titulo)

titulos = soup.find_all('h3', attrs={'class': 'ctitle'})
for t in titulos:
    print(t)