# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:17:27 2021

@author: Asus
"""
import random
from tkinter import *
class dado():
    ### metodo constructor
    def __init__(varclase):### nrmalmente varclse lo llaman self pero uno puede utilizar cualquier nombre
        varclase.numero=1
    def lanzar(varclase):
        ### generar al azar valor entre 1 y 6
        varclase.numero=ramdom.randrange(1,7)
        
    def obtenernumero(varclase):
        return varclase.numero
    def mostrar(varclase,lbl):
        ### primero cargamos la imagen photoimage
        img=PhotoImage(file=str(varclase.numero)+".png")
        ### cuando ya esta cargado mostramos la imagen
        lbl.config(image=img) ## con este le decimos que el label va mostrar imagenes y no texto
        lbl.image=img
        
        