import tkinter 
import random
import time
import threading
from threading import Timer
from tkinter import filedialog, Text
from tkinter import *
import os
import keyboard

#empieza la parte de inicio de la UI
root = tkinter.Tk()
root.title("TEST")

root.geometry("680x384")

lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(lugar_del_archivo, "1.png")

i = PhotoImage(file=archivo)
print(archivo)


imagen_luagar = tkinter.Frame(root, bg="grey") #se ha puesto gris para no dañar a la vista, de normal es blanco, hasta que se pongan las imagenes
imagen_luagar.pack(expand=1, fill=tkinter.BOTH)

imagen = tkinter.Label(imagen_luagar, image=i)


desplegable_texto = tkinter.StringVar()
desplegable_texto.set("")

desplegable_texto2 = tkinter.StringVar()
desplegable_texto.set("")


deplegable = tkinter.Frame(imagen_luagar, bg="black")
lugar_texto_desplegable1 = tkinter.Label(deplegable, textvariable=desplegable_texto, fg="white", bg="black")
lugar_texto_desplegable2 = tkinter.Label(deplegable, textvariable=desplegable_texto2, fg="white", bg="black")

texto_palo = tkinter.Label(imagen_luagar, text="Tienes el palo", fg="gold")

texto_lugar = tkinter.Frame(root, bg="blue")
texto_lugar.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.8)

caja_input = tkinter.Entry(texto_lugar)


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
p = False
p2 = False
p3 = False
i = 1

has_cogido_palo = False



def inventario(callback):
    global i
    global has_cogido_palo
    print("pulsado")
    if i == 1:
       deplegable.place(relheight=1, relwidth=0.8, relx=0.1, rely=0.1)
       lugar_texto_desplegable1.pack(side="top")
       desplegable_texto.set("INVENTARIO")
       lugar_texto_desplegable2.place(rely=0.2)
       if has_cogido_palo == True:
           desplegable_texto2.set("-Un palo! Espero que sirva")
       t3 = Timer(0.1, la_i)
       t3.start()
    
    if i == 2:
        deplegable.place_forget()
        t4 = Timer(0.1, la_i2)
        t4.start()
        i = 1
    return i

keyboard.on_press_key("i", inventario)


def la_i():
    global i
    i = 2
    return i


def la_i2():
    global i
    i = 1
    return i


def pregunta_inicial():
    global p
    global numero_random 
    numero_random = random.randint(1, 100)
    if p == False:
        texto.set("Bienvenido al nuestro quest! Cuando vimos lo que nos habias dicho hacer, lo decidimos hacer \n cada uno un script y luego enviartelos todos, a la semana de empezar nos dijimos \n-Y si lo hacemos a lo grande!- Y decidimos aprender a hacer GUI con tkinter, y aqui esta \n nuestra version del juego, esperamos que la disfrutes! ")
        t = Timer(1, pregunta_inicial) #modificar a 10 cuando se acabe el testeo
        t.start()
        
        p = True
    elif p == True:
        texto.set("Continuar?")
        texto_boton1.set("Si")
        boton_1.config(command=pregunta_11)
        texto_boton2.set("no")
        boton_2.config(command=quit)
    return numero_random
    


def pregunta_11():
    global p2
    texto_boton1.set("")
    texto_boton2.set("")
    if p2 == False:
        texto.set("Tu amigo y tu estais encerrados en una prision espacial")
        #imagen.config(image=i2)
        t1 = Timer(3, pregunta_11)
        t1.start()
        p2 = True
    elif p2 == True:
        texto.set("Intentais escapar, pero en el intento matan a tu amigo")
        #imagen.config(image=i3)
        t2 = Timer(3, pregunta_12)
        t2.start()


   




def pregunta_12():
        texto.set("sigues corriendo y te encuentras una puerta y una escotilla de cristal, por cual vas?")
        #imagen.config(image=i4)
        texto_boton1.set("Puerta")
        texto_boton2.set("Escotilla")
        boton_1.config(command=puerta)
        boton_2.config(command=escotilla)


# Parte del codigo dedicada a la eleccion de la escotilla
def escotilla():
    texto.set("Al cruzar la escotilla te encuentras un palo, lo quieres recoger?")
    texto_boton1.set("Si")
    boton_1.config(command=si_palo)
    texto_boton2.set("No")
    boton_2.config(command=no_palo)


def no_palo():
    global p3
    global has_cogido_palo
    if p3 == False:
        texto.set("Al salir de la tuberia debajo de la escotilla, te encuentras una rata la cual te dice:")
        t2 = Timer(3, si_palo)
        t2.start()
        p3 = True
    elif p3 == True:
        texto.set(f"-Hola forastero, me gustaria que respondieras a una simple pregunta cuanto es 13 x {numero_random}")
        caja_input.pack(side="bottom")
        texto_boton1.set("confirmar")
        boton_1.config(command=revisar)
        texto_boton2.set("")
        boton_2.config(command=None)
        return numero_random


def destruccion():
    texto_palo.place_forget()


def si_palo():
    global p3
    global has_cogido_palo
    texto_palo.place()
    has_cogido_palo = True
    if p3 == False:
        texto.set("Al salir de la tuberia debajo de la escotilla, te encuentras una rata la cual te dice:")
        t2 = Timer(3, si_palo)
        t2.start()
        p3 = True
        texto_palo.place(rely=0.1)
        texto_palo.after(5000, destruccion) #se hace asi para que sea como una notificacion, porque tengo planteado hacer boton de inventario (I)
    elif p3 == True:
        texto.set(f"-Hola forastero, me gustaria que respondieras a una simple pregunta cuanto es 13 x {numero_random}")
        caja_input.pack(side="bottom")
        texto_boton1.set("confirmar")
        boton_1.config(command=revisar)
        texto_boton2.set("")
        boton_2.config(command=None)
    return has_cogido_palo


def revisar():
    resultado_correcto = 13*numero_random
    resultado = caja_input.get()
    caja_input.pack_forget()
    if resultado == resultado_correcto:
        texto.set("Como la rata ve que tienes potencial te lleva a un experimento en donde mueres dolorosamente") #cambiar cuando se nos ocurra algo
        texto_boton1.set("reinicar")
        boton_1.config(command=pregunta_inicial)
        texto_boton2.set("salir")
        boton_2.config(command=quit)
    elif resultado != resultado_correcto:
        texto.set("La rata sorprendida se va corriendo") #cambiar historia segun se nos ocurra
        texto_boton1.set("???????")
        boton_1.config(command=None)
        texto_boton2.set("???????")
        boton_2.config(command=quit)


#parte del codigo dedicada a la eleccion de la puerta
def puerta():
    texto.set("Al cruzar la puerta te encuentras un alien, tienes dos opciones o hacerte el dormido o salir corriendo")
    texto_boton1.set("Hacerse el dormido")
    boton_1.config(command=hacerse_el_dormido)
    texto_boton2.set("Correr")


def hacerse_el_dormido():
    texto.set("El alien te ha encontrado y aunque estes dormido te va a ejecutar, HAS MUERTO") #a cambiar segun veamos 
    texto_boton1.set("salir")
    boton_1.config(command=quit)
    texto_boton2.set("reiniciar")
    boton_2.config(command=pregunta_inicial)


def correr():
    texto.set("Consigues escapar sin que el alien te vea") #Cuando estemos todos decidiremos esto
    texto_boton1.set("??????????????")
    boton_1.config()
    texto_boton2.set("???????????????")
    boton_2.config()

    


pregunta_inicial()

root.mainloop()