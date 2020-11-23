#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random 
import matplotlib.pyplot as plt

"""Se define de forma aleatoria una clave para un candado de cuatro digitos enteros y positivos."""
def definirClave(): 
    
    clave = str(random.randint(0000,9999)).zfill(4)
   
    return clave


""" Pre: se recibe la clave de un candado y se compara con una posible contraseña hasta dar con la correcta.
    Aclaración: la clave hace referencia a los dígitos correctos con los cuales se abre el candado.
    Post: Se devuelve la cantidad de intentos efectuados hasta que coincidan clave y contraseña probada.  """
def realizarExperimento(): 
   
    clave = definirClave()
    contrasenia =  str(0).zfill(4)    
    intentos = 1
    while(clave != contrasenia): 
        intentos+=1
        contrasenia = int(contrasenia)+1
        contrasenia = str(contrasenia).zfill(4)
        
    # print(intentos)    
    return intentos


"""Se realizan la cantidad indicada de experimentos, en este caso, 100.000"""
def experimentos():
    
    datos = []
    maxExperimentos = 100000 
    cantidadExperimentos = 0
    
    while(cantidadExperimentos < maxExperimentos):
        intento = realizarExperimento()
        cantidadExperimentos+=1
        datos.append(intento)
       
    return datos
        

"""Se realiza un histograma con la cantidad de intentos que fueron necesarios para descubrir la clave en cada experimento realizado."""
def histogram(datos):
 
    
    num_bins = 1000 #cantidad de columnas / 0-10, 10-20, ... 
    plt.hist(datos, num_bins, facecolor='blue', alpha=5)
    plt.title('¿Cuántos intentos se realizan hasta que se descubre la clave?')
    plt.xlabel('Intentos realizados')
    plt.ylabel('Cantidad de experimentos')

    plt.show()



"""Ejecución del programa"""
histogram(experimentos())