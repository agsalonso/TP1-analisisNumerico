# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

"Definición de variables a utilizar"
pi=math.pi
R=4.25 #Radio
e1=10**(-5)
e2=10**(-13)

tol=e1 #Puedo tomar e1 o e2 dependiendo el error que necesite

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
'''Recibe intervalo en el que se debe buscar la raíz y tolerancia.
Realiza las iteraciones que sean necesarias hasta hallar la raiz o hasta que el error sea menor a la tolerancia.
Devuelve la x que cumple con f(x)=0 o que tiene un error parecido a la tolerancia dada.'''

def xbis(a,b): #Se obtiene la x que será utilizada por el método de bisección 
    return((a+b)/2)
                      
def biseccion(f, a, b, t): #Calcula la solución

    if f(a)*f(b)>=0:
        print('Error')
        return('Error','Error')
    else:
        iteraciones=[]
        iteracion=[]
        
        x=xbis(a,b)
        y=f(x)
        i=0 #Número de iteración
        e=1+t
        iteracion=[i, x]
        iteraciones.append(iteracion)
        
        while (y!=0) and (e>t):
            iteracion=[]
            if f(x)*f(a)>0: #Verifico si tienen mismo signo
                
                fant=v(x)
                a=x #Intervalo ahora es desde x hasta b
                x=xbis(a,b)
                y=f(x)
                i=i+1
                e=abs(y-fant)
                
                iteracion=[i, x]
                iteraciones.append(iteracion)
                
                print(i,x, e)
                
            elif f(x)*f(b)>0:
                
                fant=f(x)
                b=x #Intervalo ahora es desde a hasta x     
                x=xbis(a,b)
                y=f(x)
                i=i+1
                e=abs(y-fant)
                
                iteracion=[i, x]
                iteraciones.append(iteracion)
                
                print(i,x, e)
        
        #print('MÉTODO DE BISECCIÓN')        
        #print('La altura del tanque que logra contener el volumen requerido al 100% es',x, 'y se obtiene luego de', i,'iteraciones.')
        
        print("Solucion aproximada (Bisección): {:.10}".format(x))
        print("numero de iteraciones: {:d}".format(i))
        print ()
        
        return(x, i, iteraciones)



'''Método de Newton-Raphson''' #Belu
""" Realiza el calculo del metodo N-R"""
def calcular(f,df,panterior):

    pactual = panterior - (f(panterior)/df(panterior))
    return pactual

""" Metodo Newton-Raphson: se reciben parametros y se realiza el metodo hasta que se obtenga un error menor a la tolerancia"""
def newton(f,df, po,tolerancia):
    iteraciones=[]
  
    panterior = po
    iteracion=[0,panterior]
    iteraciones.append(iteracion)
    error = tolerancia+1
    i = 1
    
    while error > tolerancia: 
        
        pactual = calcular(f,df, panterior)
        error = abs(pactual - panterior)
        panterior = pactual
        iteracion=[i, pactual]
        iteraciones.append(iteracion)
       # print("actual", pactual, "anterior", panterior)
        i+=1
        print(error)
    print("Solucion aproximada: {:.10}".format(pactual))
    print("numero de iteraciones: {:d}".format(i))
    print ()
    
    return(pactual, i, iteraciones)


    
def nrm():
    
    return()


""" Pre: los parametros recibidos son válidos. En el caso del intervalo, se asume que cumple que el producto del intervalo evaluado en la funcion
    es menor a cero (f(a)*f(b) < 0; garantizando existencia de raíz por el teorema de Bolzano"""
def secante(f, pn_1, pn_2, tolerancia): 
    error = tolerancia + 1
    i = -1 
    iteraciones=[]
    
    while error > tolerancia: 
        
        pn = pn_1 - ( ((pn_1-pn_2)/(f(pn_1)-f(pn_2)))*f(pn_1) )
        
        error = abs(pn - pn_1)
        #WARNING: ojo que si ya se cumplió el error, entonces se estarian actualizando igual los p
        if error>tolerancia:
            pn_2 = pn_1
            pn_1 = pn
        i+= 1
        iteracion=[i, pn]
        iteraciones.append(iteracion)
        
        print(pn)
        
    print("Solucion aproximada (Secante): {:.10}".format(pn))
    print("numero de iteraciones: {:d}".format(i))
    
    return(pn, i, iteraciones)


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

p=xbis(a,b) #Semilla 


#Primero, busco cuánto vale el volumen maximo/cuál es el volumen del tanque más grande cuando lo llenamos al porcentaje que nos piden
#Por lo tanto, debemos buscar las raíces de la función que modela al tanque
#Haciendo un analisis cualitativo antes de ingresar datos, notamos que el valor máximo se obtiene cuando la altura es 2R.

b=2*R

"Define el volumen del tanque de máxima capacidad, lleno al porcentaje pedido."
vmax=lambda x: porcentaje_pedido*(4/3)*pi*(R**3)


"Define la funcion para buscar la altura tal que, al llenar completamente el tanque, éste contenga el volumen pedido."
v=lambda x:f2(x)-vmax(x)
dv=lambda x:fx2(x)

raiz_biseccion, cant_it_biseccion, iteraciones_biseccion = biseccion(v,a,b,tol)
raiz_nr, cant_it_newton, iteraciones_nr = newton(v,dv,p,tol)
raiz_secante, cant_it_secante, iteraciones_secante = secante(v,a,b,tol)


#%%Grafico de la función
plt.figure(figsize=[12.8, 9.6])

# Intervalo a graficar
x=np.linspace(a, b) 

y1=v(x)

plt.plot(x, y1, "-r", label=r'$V(x)-Vmax$')

#Marco eje x para distinguir donde estan los puntos con diferencia nula (Los que me interesan en este caso)
plt.axhline(color='black', lw=0.5)

#Configuración general del gráfico (Ejes, título, grilla, etc)
plt.xlim(a, b)
plt.xlabel('Altura')
plt.ylabel('Diferencia entre el volumen a una altura x y el volumen máx. pedido')
plt.grid(True, 'both')
plt.legend() #Muestra el cuadro de referencias
plt.title('Gráfico Volumen pedido vs. altura de tanque al 100%')
plt.show()
plt.savefig('Volumen pedido vs altura.svg') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf
