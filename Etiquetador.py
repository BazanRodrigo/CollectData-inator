import pygame
import os
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
    print('CentroBounding box: ' , anchob, largob)
    print('medidas de bounding box' , imagena, imagenl)
    print('____________________________________')
    data = 0, anchob, largob, imagena, imagenl
    return str(data)

def savingData(data):
    file = open("/home/rodrigo/RecolectDataNator/DataBase/v5.txt", "w")
    file.write(data + os.linesep)
    file.close()

def main()  :
    wp = pygame.image.load('/home/rodrigo/RecolectDataNator/DataProgram/WallpaperEtiqueta.jpg')
    img = pygame.image.load('/home/rodrigo/RecolectDataNator/DataBase/v5.jpg')
    save = pygame.image.load('/home/rodrigo/RecolectDataNator/Icons/save.png')
    restar = pygame.image.load('/home/rodrigo/RecolectDataNator/Icons/restart.png')
    clean = pygame.image.load('/home/rodrigo/RecolectDataNator/Icons/clean.png')
    pygame.init()
    pygame.display.init()
    window = pygame.display.set_mode()
    pygame.display.set_caption("Tag-inator")
    font = pygame.font.SysFont("monospace", 30)
    window.blit(wp, (0,0))
    window.blit(img, (100,100))
    pygame.draw.rect(window, (144, 12, 63), [492, 0, 720, 40])
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
                    print('Segun guardado XD')
                    savingData(data)
                    continue
                data = medidas(xd, yd, xu, yu)
                pygame.draw.rect(window, (144, 12, 63), [492, 0, 720, 40])
                message = font.render(data, 1,(255, 195, 0))
                window.blit(message, (512,0))
                window.blit(save, (768,50))
                pygame.display.flip()
                data = medidas(xd, yd, xu, yu)



if __name__ == '__main__':
    main()
