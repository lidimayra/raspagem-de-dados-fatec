import requests
from bs4 import BeautifulSoup

url = 'http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm'

params = { 'objetos': 'codigo_de_rastreamento' }
headers = { 'Referer': 'http://www2.correios.com.br/sistemas/rastreamento/default.cfm' }

html = requests.post(url, data=params, headers=headers)

soup = BeautifulSoup(html.text, 'html.parser')
print(soup.strong.text)
