import pygame
import os
import shutil
from pygame.locals import *
img = 1
def guardador(img):
    dir = 'DataBase'
    try:
        path = os.path.join(dir)
        os.mkdir(path)
        print('Creado '+path)
    except FileExistsError:
        print('Creado '+path)

    r = str(img)
    print('tmp/Yedisbb'+str(img)+'.jpg aloh')
    origen = '/home/rodrigo/RecolectDataNator/tmp/Yedisbb' +str(img)+'.jpg'
    destino = '/home/rodrigo/RecolectDataNator/DataBase/Yedisbb' +str(img)+'.jpg'
    shutil.copy(origen, destino)
    #os.rename(imagenf, 'DataBase/Yedisbb' +str(img)+'.jpg')

    return

def loader():
    global img
    global file
    try:
        r = str(img)
        print('tmp/Yedisbb'+str(img)+'.jpg aloh')
        imagen = pygame.image.load('tmp/Yedisbb' +str(img)+'.jpg')
        img += 1
    except FileNotFoundError:
        img = 1
        r = str(img)
        file = 'tmp/Yedisbb'+str(img)+'.jpg aloh'
        imagen = pygame.image.load('tmp/Yedisbb' +str(img)+'.jpg')
        img += 1

    return imagen

def main():
    wp = pygame.image.load('DataProgram/wallpaperPrincipal.jpg')
    correctimg = pygame.image.load('Icons/correct.png')
    incorrectimg = pygame.image.load('Icons/incorrect.png')
    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode()
    window.blit(wp, (0,0))
    window.blit(correctimg, (100,800))
    window.blit(incorrectimg, (400,800))
    pygame.display.flip()
    window.blit(loader(), (200,200))
    pygame.display.flip()
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>100 and x<225 and y>800 and y<928:
                    print("Si le sabes")
                    guardador(img)
                if x>400 and x<525 and y>800 and y<928:
                    print("No le sabes")
                window.blit(loader(), (200,200))
                pygame.display.flip()

if __name__  == '__main__':
    main()
