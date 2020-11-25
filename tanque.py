# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

"Definición de variables a utilizar"
pi=math.pi
R=4.25 #Radio
e1=10**(-5)
e2=10**(-13)

# Expresión del porcentaje requerido
s=1+1+4+5+7 #Suma del último dígito del padron de cada uno de los integrantes
n=5 #Cantidad de personas en el grupo
porcentaje_pedido=(s/(n*9.5))

# Intervalo en el que debemos buscar la raíz
'Tomamos que x es la altura del tanque y esta debe ser mayor a 0.'
'Por lo tanto, evaluamos entre 0 y 3R ya que, despejando las funciones que modelan el volumen, estas se anulan con x=0 y x=3R.' 
a=0
b=3*R


#%% Función volumen
"Define la función que modela el volumen lleno al 100%."
def f2(x):
    
    return((pi*(x**2)*(3*R-x))/3)

"Define la función que modela el volumen lleno al porcentaje definido por una expresión particular."
def f1(x):

    return(porcentaje_pedido*f2(x))

"Derivadas de f1 y f2"
def fx2(x):
    
    return((pi*(2*x*3*R - 3*(x**2)))/3)

def fx1(x):
    
    return(fx2(x)*porcentaje_pedido)


#%% Definición de funciones a utilizar 

def puntofijo():
    
    return()


def biseccion():
    
    return()


def nr():
    
    return()


def nrm():
    
    return()


def secante():
    
    return()


#%% Gráfico de las funciones y sus derivadas

plt.figure(figsize=[12.8, 9.6])

# Intervalo a graficar
x=np.linspace(a, b) 

y1=f1(x)
y2=f2(x)
yx1=fx1(x)
yx2=fx2(x)

#Grafico de cada función
plt.plot(x, y1, "-r", label=r'$f_1(x)$')
plt.plot(x, y2, "-b", label=r'$f_2(x)$')
plt.plot(x, yx1, "-r", label=r'$\frac{df_1(x)}{dx}$', ls='--') 
plt.plot(x, yx2, "-b", label=r'$\frac{df_2(x)}{dx}$', ls='--')

#Configuración general del gráfico (Ejes, título, grilla, etc)
plt.xlim(a, b)
plt.xlabel('Altura')
plt.ylabel('Volumen')
plt.grid(True, 'both')
plt.legend() #Muestra el cuadro de referencias
plt.title('Funciones volumen (lleno y al porcentaje pedido) y sus derivadas')
plt.show()
plt.savefig('Funciones y sus derivadas.svg') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf








