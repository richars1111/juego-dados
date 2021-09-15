from tkinter import *

def agregarImagen(ventana, archivo, fila, columna):
    img = PhotoImage(file=archivo)### carga la imagen en la memoria y recibe como parametro el nombre del archivo
    lbl= Label(ventana)### se instancio
    lbl.config(image=img) ### ala etiqueta se la asigno la imagen
    lbl.image=img
    lbl.grid(row=fila, column=columna)### se ubica en la fila y columna que se quiere
    return lbl

def agregarCajaTextoSalida(ventana, ancho, fila, columna, fuente):
    txt = Entry(ventana, width=ancho, font=fuente)
    txt.grid(row=fila, column=columna)
    txt.configure(state=DISABLED)
    return txt
    
def mostrarCajaTexto(txt, valor):
    txt.configure(state=NORMAL)
    txt.delete(0, END)
    txt.insert(0, valor)
    txt.configure(state=DISABLED)
