import requests
from bs4 import BeautifulSoup
import os
#Esta
print("Ingresa el nombre que deseas que tengan los archivos de la base de datos")
name = input()
print("Ingresa el url para explorar")
url = input()
print("Leido con exito \nScrapeando...")
soup = BeautifulSoup((requests.get(url)).content, "html.parser")
print("Ingresa la clase div del html que buscamos maquina")
classContenedora = input()
print("Ingresa la clase img del html que buscamos maquina")
classToSearch = input()
print("Ingresa el src del html que buscamos maquina")
srcToSearch = input()
images = soup.find_all('div',class_=classContenedora)
i=0
os.chdir('tmp/')
for img in images:
    imagenLocalizada = img.find('img', class_=classToSearch).get(srcToSearch)
    i=i+1
    imagenLink = requests.get(imagenLocalizada)
    nameFile=name+str(i)+'.jpg'
    print("Procesando "+nameFile)
    with open(nameFile, 'wb') as imagen:
        imagen.write(imagenLink.content)