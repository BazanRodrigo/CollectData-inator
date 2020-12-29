import pygame
import numpy as np
import cv2

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
    print('Medidas :', width, heigth)
    print('MouseD: ' , xd, yd)
    print('MouseU: ' , xu, yu)
    print('Centros: ' , centerx, centery)
    print('CentroBounding box: ' , anchob, largob)
    print('medidas de bounding box' , imagena, imagenl)
    print('____________________________________')


def main()  :
    wp = pygame.image.load('/home/rodrigo/RecolectDataNator/DataProgram/WallpaperEtiqueta.jpg')
    img = pygame.image.load('/home/rodrigo/RecolectDataNator/DataBase/v5.jpg')
    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode()
    pygame.display.set_caption("Tag-inator")
    font = pygame.font.SysFont("monospace", 15)
    window.blit(wp, (0,0))
    window.blit(img, (100,100))
    pygame.display.flip()
    running = True
    while running:
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
                medidas(xd, yd, xu, yu)


if __name__ == '__main__':
    main()
