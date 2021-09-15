from tkinter import *
import Util
from Dado import Dado

#crear ventana
v = Tk()
v.title("Juego de Dados")
#Imagenes de los dados
lblDado1=Util.agregarImagen(v, "1.png", 0, 0)
lblDado2=Util.agregarImagen(v, "1.png", 0, 1)

#Etiquetas
Label(v, text="Lanzamientos").grid(row=2, column=0)
Label(v, text="Cenas").grid(row=2, column=1)
#Cajas de texto para mostrar estado de los lanzamientos
txtLanzamientos=Util.agregarCajaTextoSalida(v, 3, 3, 0, "Arial 48 bold")
txtCenas=Util.agregarCajaTextoSalida(v, 3, 3, 1, "Arial 48 bold")
#creamos los dos dados
dado1 = Dado() ### dado es la clase
dado2 = Dado()
lanzamientos=0  ### contador de los lanzamientos
cenas=0 ## contador de las cenas
def lanzarDados():
    ### cada instancia lanza
    global lanzamientos,cenas ## definimos cuales son variables globales
    dado1.lanzar()
    dado2.lanzar()
    
    ### mostrar los dados
    dado1.mostrar(lblDado1)
    dado2.mostrar(lblDado2)
    
    ## administrar contadores
    lanzamientos+=1
    Util.mostrarCajaTexto(txtLanzamientos,lanzamientos)
    if dado1.obtenerNumero()+dado2.obtenerNumero()>=11:
        cenas+=1
        Util.mostrarCajaTexto(txtCenas,cenas)
Button(v, text="Lanzar", command=lanzarDados).grid(row=1, column=0)

v.mainloop()
