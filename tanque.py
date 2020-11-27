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


'''Método de Bisección'''

def error(fant,fpost):
    
    e=(abs(fpost-fant))
    
    return(e)

'''Método de Bisección: 
Recibe intervalo en el que se debe buscar la raíz y tolerancia.
Realiza las iteraciones que sean necesarias hasta hallar la raiz o hasta que el error sea menor a la tolerancia.
Devuelve la x que cumple con f(x)=0 o que tiene un error parecido a la tolerancia dada.'''


def xbis(a,b): #Se obtiene la x que será utilizada por el método de bisección 
    return((a+b)/2)
                      
def biseccion(a, b, t): #Calcula la solución
    iteraciones=[]
    iteracion=[]
    
    x=xbis(a,b)
    y=f2(x)
    i=0 #Número de iteración
    e=1 #Sé que, por lo general, la tolerancia es menor a 1. Así que lo inicializo con ese valor.
    iteracion=[i, x]
    iteraciones.append(iteracion)
    
    while (y!=0) and (e>t):
        iteracion=[]
        if f2(x)*f2(a)>0: #Verifico si tienen mismo signo
            
            fant=f2(x)
            a=x #Intervalo ahora es desde x hasta b
            x=xbis(a,b)
            y=f2(x)
            i=i+1
            e=error(fant,y)
            
            iteracion=[i, x]
            iteraciones.append(iteracion)
            
            print(i,x, e)
            
        elif f2(x)*f2(b)>0:
            
            fant=f2(x)
            b=x #Intervalo ahora es desde a hasta x     
            x=xbis(a,b)
            y=f2(x)
            i=i+1
            e=error(fant,y)
            
            iteracion=[i, x]
            iteraciones.append(iteracion)
            
            print(i,x, e)
    print ()
    print('MÉTODO DE BISECCIÓN')        
    print('La altura del tanque que logra modelar el volumen máximo es',x, 'y se obtiene luego de', i,'iteraciones.')
    return(x, iteraciones)


'''Método de Newton-Raphson'''
""" Realiza el calculo del metodo N-R"""
def calcular(f,df,panterior):

    pactual = panterior - (f(panterior)/df(panterior))
    return pactual

""" Metodo Newton-Raphson: se reciben parametros y se realiza el metodo hasta que se obtenga un error menor a la tolerancia"""
def newton(f,df, po,tolerancia):
  
    panterior = po
    error = tolerancia+1
    iteraciones = 1
    
    while error > tolerancia: 
        
        pactual = calcular(f,df, panterior)
        error = abs(pactual - panterior)
        panterior = pactual
       # print("actual", pactual, "anterior", panterior)
        iteraciones+=1
        print(error)
    print("Solucion aproximada: {:.10}".format(pactual))
    print("numero de iteraciones: {:d}".format(iteraciones))


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


#%% Cálculo de la solución

p=xbis(a,b)
t1=10**(-5)
newton(f1, f1x, p, t1 )





