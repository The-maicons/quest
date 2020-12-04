import tkinter 
import random
from tkinter import filedialog, Text

root = tkinter.Tk()
root.title("TEST")

root.geometry("680x384")

imagen_luagar = tkinter.Frame(root, bg="red")
imagen_luagar.pack(expand=1, fill=tkinter.BOTH)


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


root.mainloop()