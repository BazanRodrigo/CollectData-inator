# Esta version filtra las imagenes para saber cuales si funcionan y cuales no y esta funcionando
from PIL import Image
import requests
from io import BytesIO
import pygame
url = 'https://lastfm.freetls.fastly.net/i/u/770x0/144ffbc80d11b8414f7098896e5c233b.jpg'


def Filtrador(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
    print("Te sirve?")
    res = input()
    nameFile = 'diosaDua.jpg'

    if res == 'y':
        with open(nameFile, 'wb') as imagen:
            imagen.write(response.content)

Filtrador(url)
