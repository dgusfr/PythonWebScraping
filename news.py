import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
  # Título
  titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

  # print(titulo.text)
  # print(titulo['href']) # link da notícia

  # Subtítulo: div class="feed-post-body-resumo"
  subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

  if subtitulo:
    # Se possuir subtítulo, adiciona título, subtítulo e link da notícia à lista
    lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
  else:
    # Se não possuir subtítulo, adiciona apenas título e link da notícia à lista
    lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)
news.to_csv('noticias.csv', index=False)


# print(news)