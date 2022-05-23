import tkinter as tk

from setuptools import Command


ventana = tk.Tk()
ventana.geometry("1000x680+200+10")
ventana.resizable(width=False, height=False)

etiqueta = tk.Label(ventana,text="Esto es  un label")
etiqueta.pack()


entrada = tk.Entry()
entrada.pack()

boton = tk.Button(text="Ejecutar", command= c)
boton.pack()


def c():
    if (boton.selection_get):
        quit

ventana.mainloop()