import requests
from bs4 import BeautifulSoup

def funcion_poblacion(lista):
    resultado=[]
    try:
        for i in lista:
            res = requests.get(i)
            soup = BeautifulSoup(res.content,"html.parser")
            textaco = soup.findAll("div", {"class":"figureLabel___2OYTW"})
            resultado.append(textaco[0].getText())
    except:
        resultado.append("No hay dato")
    return resultado