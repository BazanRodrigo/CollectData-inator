import pygame
from pygame import *
import os
import cv2
import numpy as np

def medidas(xd, yd, xu, yu):
    xd = xd - 100
    xu = xu - 100
    yd = yd - 100
    yu = yu - 100
    jpg = cv2.imread('/home/rodrigo/RecolectDataNator/DataBase/v5.jpg')
    heigth, width = jpg.shape[0:2]
    centerx = (abs(xd-xu))/2
    centery = (abs(yd-yu))/2
    anchob = (centerx+xd)/width
    largob = (centery+yd)/heigth
    imagena = (abs(xd-xu))/width
    imagenl = (abs(yd-yu))/heigth
    anchob = round(anchob, 5)
    largob = round(largob, 5)
    imagena = round(imagena, 5)
    imagenl = round(imagenl, 5)
    data = 0, anchob, largob, imagena, imagenl
    return str(data)

def savingData(data, lista, i):
    file = open('/home/rodrigo/RecolectDataNator/DataBase/txt/'+ str(lista[i]) +'.txt', 'w')
    file.write(data + os.linesep)
    file.close()

def main()  :
    r = 0
    wp = pygame.image.load('/home/rodrigo/RecolectDataNator/DataProgram/WallpaperEtiqueta.jpg')
    img = pygame.image.load('/home/rodrigo/RecolectDataNator/DataBase/'+str(loader()[r])+'.jpg')
    save = pygame.image.load('/home/rodrigo/RecolectDataNator/Icons/save.png')
    next = pygame.image.load('/home/rodrigo/RecolectDataNator/Icons/next.png')
    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode()
    pygame.display.set_caption("Tag-inator")
    font = pygame.font.SysFont("arial", 30)
    window.blit(wp, (0,0))
    window.blit(img, (100,100))
    pygame.display.flip()
    running = True
    while running:
        pygame.display.flip()
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                md = pygame.mouse.get_pos()
                xd = md[0]
                yd = md[1]
            if event.type == pygame.MOUSEBUTTONUP:
                mu = pygame.mouse.get_pos()
                xu = mu[0]
                yu = mu[1]
                if xu>768 and xu<800 and yu>50 and yu<82:
                    savingData(data, loader(), r)
                    r = r + 1
                    try:
                        img = pygame.image.load('/home/rodrigo/RecolectDataNator/DataBase/'+str(loader()[r])+'.jpg')
                    except FileNotFoundError:
                        finmessage = font.render('Proceso terminado', 2,(255, 160, 122), (88, 24, 69))
                        window.blit(finmessage,(512,512))
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False
                    window.blit(wp, (0,0))
                    window.blit(img, (100,100))
                    pygame.display.flip()
                    continue
                data = medidas(xd, yd, xu, yu)
                message = font.render(data, 1,(255, 195, 0),(144, 12, 63))
                window.blit(message, (512,0))
                window.blit(save, (768,50))
                window.blit(next, (820,50))
                pygame.display.flip()
                data = medidas(xd, yd, xu, yu)

def loader():
    lista = os.listdir()
    j = 0
    for elements in lista:
        try:
            point = elements.index('.')
        except ValueError:
            continue
        terminacion = elements[point:]
        if terminacion != '.jpg' :
            lista.pop(j)
        lista[j] = (lista[j])[:point]
        j = j + 1
    lista = lista
    return lista

if __name__ == '__main__':
    main()

