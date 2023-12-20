import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

lista_noticias = []

url = 'https://portais.ifsp.edu.br/scl/index.php/ultimas-noticias.html'
resposta = requests.get(url)
html = bs(resposta.text, 'html.parser')

noticias = html.find_all('div', class_='tileItem')
for noticia in noticias:
    titulo = noticia.find('h2', class_='tileHeadline')

    link = titulo.find('a')['href']
    link_formatado = link.replace('/scl/', 'https://portais.ifsp.edu.br/scl/')

    descricao = noticia.find('span', class_='description')
    if(descricao):
        lista_noticias.append([titulo.text.strip(), descricao.text, link_formatado])
    else:
        lista_noticias.append([titulo.text, '', link_formatado])


news = pd.DataFrame(lista_noticias, columns=['Título', 'Descrição', 'Link'])

news.to_excel('Notícias_IFSP.xlsx', index=False)











