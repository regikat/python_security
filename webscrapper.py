from bs4 import BeautifulSoup
import requests
site = requests.get("https://www.climatempo.com.br/").content
#objeto site está recebendo o conteudo da requisição
# httpdo siste ....
soup = BeautifulSoup(site, 'html.parser')
#objeto soup esta baixando do site html
#print(soup.prettify())
#prettify transforma a estrutura html em string e o print exibe o html
#transforma html em string e o print vai exibir o html
temperatura = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")
print(temperatura.string)
#pegar o titulo
#print(soup.title.string)

#procura a primeira tag 'p'  q ele encontrar no codigo da pagina
#print(soup.p.string)

#fazer um find no codigo
#print(soup.find('admin'))