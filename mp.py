import requests
from bs4 import BeautifulSoup

url_base = 'https://www.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})

if not produtos:
    print("Nenhuma classe encontrada. Verifique a classe ou a estrutura do HTML.")

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    real = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    

    print(produto.prettify())
    print('Título do produto:', titulo.text)
    print('\n\n')
    break
