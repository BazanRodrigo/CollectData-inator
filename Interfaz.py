#import os
from tkinter import *

#os.chdir('DataProgram/')
#wallpaper = 'wallpaperPrincipal.jpg'
window = Tk()
window.title('RecolectDataNator')
window.geometry('720x480')

url = StringVar()
url.set("Escribe el url")

boton = Button(window, text="Enviar", command = window.iconify)

urlText = Entry(window).place(x=170, y =10)
boton.pack()



window.mainloop()
