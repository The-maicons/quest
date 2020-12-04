import tkinter 
import random
import time
import threading
from threading import Timer
from tkinter import filedialog, Text
from tkinter import *

#empieza la parte de inicio de la UI
root = tkinter.Tk()
root.title("TEST")

root.geometry("680x384")

imagen_luagar = tkinter.Frame(root, bg="red")
imagen_luagar.pack(expand=1, fill=tkinter.BOTH)

b1_imagen = PhotoImage(file="C:/Users/carly/Documents/boton_1.png")

texto_lugar = tkinter.Frame(root, bg="blue")
texto_lugar.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.8)


texto = tkinter.StringVar()
texto.set("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sollicitudin ac augue nec ultrices.\n Aliquam lobortis erat vitae nulla commodo aliquam. Sed rutrum, diam id dignissim dapibus, sem justo \ncommodo.")

texto_boton1 = tkinter.StringVar()
texto_boton1.set("test")

texto_boton2 = tkinter.StringVar()
texto_boton2.set("test")

texto_label = tkinter.Label(texto_lugar, bg="blue", fg="white", textvariable=texto)
texto_label.pack(side="top")

boton_1 = tkinter.Button(imagen_luagar, textvariable=texto_boton1)
boton_1.pack(side="left")

boton_2 = tkinter.Button(imagen_luagar, textvariable=texto_boton2)
boton_2.pack(side="right")

# acaba la parte de inicio de la UI

#empieza la logica
def pregunta_inicial():
    texto.set("Bienvenido al nuestro quest! Cuando vimos lo que nos habias dicho hacer, lo decidimos hacer \n cada uno un script y luego enviartelos todos, a la semana de empezar nos dijimos \n-Y si lo hacemos a lo grande!- Y decidimos aprender a hacer GUI con tkinter, y aqui esta \n nuestra version del juego, esperamos que la disfrutes! ")
    t = Timer(1, continuar) #modificar a 10 cuando se acabe el testeo
    t.start()
    
def continuar():
    texto.set("Continuar?")
    texto_boton1.set("Si")
    boton_1.config(command=pregunta_1)
    texto_boton2.set("no")
    boton_2.config(command=quit)

def pregunta_1():
    texto.set("Tu amigo y tu os habeis escapado de una prision espacial, desafortunadamente, \nhan matado a tu amigo y tienes que escaparte solo, actualmente te encuentras \nen un pasillo, en el cual tienes dos maneras de salir de el, por la puerta del final \ndel pasillo o por una trampilla")
    texto_boton1.set("Trampilla")
    texto_boton2.set("Puerta")
    



pregunta_inicial()

root.mainloop()