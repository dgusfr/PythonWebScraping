# Web Scraping

## Notícias e Busca de Acomodações no Airbnb

## Logo

<div align="center">
  <img src="img/logo.png" alt="Imagem do Projeto" width="600">
</div>

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Autor](#autor)

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Python" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

## Descrição

Este projeto consiste em dois scripts em Python. O primeiro realiza web scraping de notícias do site G1 da Globo e salva os dados em um arquivo Excel e um arquivo CSV. O segundo script automatiza a busca por acomodações no Airbnb para a cidade de São Paulo, utilizando Selenium para simular a interação com o navegador.

## Funcionalidades

1. O primeiro script coleta os títulos, subtítulos e links das notícias do G1 e os salva em um arquivo Excel e um arquivo CSV.
2. O segundo script automatiza a busca por acomodações no Airbnb para São Paulo, interagindo com elementos da página como campo de pesquisa, botões e seletores.

## Como Usar

1. Instale as dependências do Python`pip install -r requirements.txt`.
2. Execute o script `web_scraping_g1.py` para coletar as notícias do G1 e salvar os dados em arquivos Excel e CSV.
3. Execute o script `automatizacao_airbnb.py` para realizar a busca por acomodações no Airbnb para São Paulo.

## Estrutura do Projeto

- `web_scraping_g1.py`: Script para coletar notícias do G1.
- `automatizacao_airbnb.py`: Script para automatizar a busca por acomodações no Airbnb.
- `noticias.xlsx`: Arquivo Excel com os dados das notícias coletadas.
- `noticias.csv`: Arquivo CSV com os dados das notícias coletadas.
- `requirements.txt`: Arquivo de dependências do Python.
- `img/`: Pasta contendo imagens utilizadas no README.

## Autor

Desenvolvido por Diego Franco.
