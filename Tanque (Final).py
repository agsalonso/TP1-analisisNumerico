<<<<<<< HEAD:Tanque (Final).py
=======
<<<<<<< HEAD
>>>>>>> 482447e573e583ad445c56ef6fbd78732d6cc0d0:tanque con b, nr, pf y s.py
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

"Definición de variables a utilizar"
pi=math.pi
R=4.25 #Radio
e1=10**(-5)
e2=10**(-13)

tol=1e-8 #Puedo tomar e1 o e2 dependiendo el error que necesite

n0=100 #Cantidad maxima de iteraciones

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

"Segunda derivada de f2" #ELIMINARRRRRRRRRR
def fxx2(x):
    return((pi*(2*3*R - 6*(x)))/3)


#%% Definición de funciones a utilizar 

def puntofijo(gx,a,tolera, iteramax = 100):
    
    iteraciones=[]
    raices=[]
    
    iteracion=[0, a]
    iteraciones.append(iteracion)
    raices.append(a)
    
    i = 1 # iteración
    b = gx(a)
    tramo = abs(b-a)
    
    iteracion=[0, b]
    iteraciones.append(iteracion)
    raices.append(b)
    
    while(tramo>=tolera and i<=iteramax ):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        print("error",tramo)
        i = i+1
        iteracion=[i, b]
        iteraciones.append(iteracion)
        raices.append(b)
    print("SE IMPRIMEN LAS RAICES DE PUNTO FIJO:",raices)
    respuesta = b
    # Validar respuesta
    if (i>=iteramax ):
        respuesta = np.nan
    
    print("Solucion aproximada PUNTO FIJO: {:.10}".format(respuesta))
    print("numero de iteraciones PUNTO FIJO: {:d}".format(i))
    #return(respuesta, i)
    return(respuesta, i, iteraciones, raices)



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
        raices=[]
        
        x=xbis(a,b)
        y=f(x)
        i=0 #Número de iteración
        e=1+t
        iteracion=[i, x]
        iteraciones.append(iteracion)
        raices.append(x)
        
        while (y!=0) and (e>t):
            
            if f(x)*f(a)>0: #Verifico si tienen mismo signo
                
                fant=v(x)
                a=x #Intervalo ahora es desde x hasta b
                x=xbis(a,b)
                y=f(x)
                i=i+1
                e=abs(y-fant)
                
                iteracion=[i, x]
                iteraciones.append(iteracion)
                raices.append(x)
                
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
                raices.append(x)
                
                print(i,x, e)
        
        #print('MÉTODO DE BISECCIÓN')        
        #print('La altura del tanque que logra contener el volumen requerido al 100% es',x, 'y se obtiene luego de', i,'iteraciones.')
        
        print("Solucion aproximada BISECCIÓN: {:.10}".format(x))
        print("numero de iteraciones BISECCIÓN: {:d}".format(i))
        print ()
        
        return(x, i, iteraciones, raices)



'''Método de Newton-Raphson''' #Belu
""" Realiza el calculo del metodo N-R"""
def calcular(f,df,panterior):

    pactual = panterior - (f(panterior)/df(panterior))
    return pactual

def calcularModificado(f,df,d2f,panterior):
    
    pactual = panterior -  (f(panterior)*df(panterior)) /   (   (df(panterior))**2 - f(panterior)*d2f(panterior) )    
    return pactual

""" Metodo Newton-Raphson: se reciben parametros y se realiza el metodo hasta que se obtenga un error menor a la tolerancia"""
def newton(f,df, po,tolerancia):
    iteraciones=[]
    raices=[]
  
    panterior = po
    
    iteracion=[0,panterior]
    iteraciones.append(iteracion)
    raices.append(panterior)
    
    error = tolerancia+1
    i = 1
    
    while error > tolerancia: 
        
        pactual = calcular(f,df, panterior)
        error = abs(pactual - panterior)
        panterior = pactual
        iteracion=[i, pactual]
        iteraciones.append(iteracion)
        raices.append(pactual)
       # print("actual", pactual, "anterior", panterior)
        i+=1
        print(error)
    print("Solucion aproximada NR: {:.10}".format(pactual))
    print("numero de iteraciones NR: {:d}".format(i))
    print ()
    
    return(pactual, i, iteraciones, raices)

"""Método de Newton-Raphson Modificado"""
def nrm(f,df,d2f,po,tolerancia):
    
    iteraciones=[]
    raices=[]
  
    panterior = po
    iteracion=[0,panterior]
    iteraciones.append(iteracion)
    raices.append(po)
    error = tolerancia+1
    i = 1
    
    while error > tolerancia: 
        
        pactual = calcularModificado(f,df, d2f, panterior)
        error = abs(pactual - panterior)
        print("actual", pactual, "anterior", panterior)
        panterior = pactual
        iteracion=[i, pactual]
        iteraciones.append(iteracion)
        raices.append(pactual)
        
        i+=1
        print(error)
    print("Solucion aproximada NR MODIFICADO: {:.10}".format(pactual))
    print("numero de iteraciones NR MODIFICADO: {:d}".format(i))
    print ()
    
    return(pactual, i, iteraciones, raices)



""" Pre: los parametros recibidos son válidos. En el caso del intervalo, se asume que cumple que el producto del intervalo evaluado en la funcion
    es menor a cero (f(a)*f(b) < 0; garantizando existencia de raíz por el teorema de Bolzano"""
def secante(f, pn_1, pn_2, tolerancia): 
    error = tolerancia + 1
    iteracion=[0,pn_1]
    i = 0
    iteraciones=[]
    raices=[]
    
    iteraciones.append(iteracion)
    raices.append(pn_1)
    
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
        raices.append(pn)
        
        print(pn)
        
    print("Solucion aproximada SECANTE: {:.10}".format(pn))
    print("numero de iteraciones SECANTE: {:d}".format(i))
    
    return(pn, i, iteraciones, raices)



def convergencia(numiteraciones,iteraciones):
    alphas=[] #Esto es para almacenar alpha y comparar que todas sean iguales - tienen que ser todos 1(convergencia lineal) o todos 2 (convergencia cuadrática)
    lambdas=[] #Lo mismo que la lista alphas, para comparar que tiendan a un mismo valor


    for i in range (3-1,numiteraciones-1):

        masuno=iteraciones[i+1][1]-iteraciones[i][1]
        menosuno=iteraciones[i][1]-iteraciones[i-1][1]
        menosdos=iteraciones[i-1][1]-iteraciones[i-2][1]
        
        if menosuno!=0 and menosdos!=0:
            alpha=((np.log10(np.abs(masuno/menosuno)))/(np.log10(np.abs(menosuno/menosdos))))
            alphas.append(alpha)
        if menosuno!=0:
            cteconvergencia=((np.abs(masuno))/((np.abs(menosuno))**alpha))
            lambdas.append(cteconvergencia)
        i=i+1
        
    
    
    return(alphas, lambdas)

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

plt.savefig('Funciones y sus derivadas.pdf') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf
plt.show()

#%% Cálculo de la solución

#Primero, busco cuánto vale el volumen maximo/cuál es el volumen del tanque más grande cuando lo llenamos al porcentaje que nos piden
#Por lo tanto, debemos buscar las raíces de la función que modela al tanque
#Haciendo un analisis cualitativo antes de ingresar datos, notamos que el valor máximo se obtiene cuando la altura es 2R.

b=2*R

p=xbis(a,b) #Semilla

"Define el volumen del tanque de máxima capacidad, lleno al porcentaje pedido."
vmax=lambda x: porcentaje_pedido*(4/3)*pi*(R**3)

"Define la función que modela el volumen lleno al 100%."
def f2(x):
    
    return((pi*(x**2)*(3*R-x))/3)


volumenmax=(4/3)*pi*(4.25**3)*(18/(5*9.5))
v= lambda x: (pi*4.25*(x**2)-(pi/3)*(x**3)-volumenmax)
dv=lambda x: 2*pi*4.25*(x)-pi*(x**2)
d2v=lambda x: 2*pi*4.25-2*pi*x
g= lambda x:((((x**3)+4*(4.25**3)*(18/(5*9.5)))/(3*4.25)))**(1/2)

plt.figure(figsize=[12.8, 9.6])

# Intervalo a graficar
x=np.linspace(a, b) 

y1=v(x)
y2=dv(x)

#Grafico de cada función
plt.plot(x, y1, "-r", label=r'$v(x))$')
plt.plot(x, y2, "-b", label=r'$dv(x)$', ls='--')

#Marco eje x para distinguir donde estan los puntos con diferencia nula (Los que me interesan en este caso)
plt.axhline(color='black', lw=0.5)

#Configuración general del gráfico (Ejes, título, grilla, etc)
plt.xlim(a, b)
plt.xlabel('Altura')

plt.grid(True, 'both')
plt.legend() #Muestra el cuadro de referencias
plt.title('Funciones volumen y su derivada')

plt.savefig('V y dV.pdf') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf
plt.show()

pare='false'

raiz_biseccion, cant_it_biseccion, iteraciones_biseccion, raices_biseccion = biseccion(v,a,b,tol)
raiz_nr, cant_it_nr, iteraciones_nr, raices_nr = newton(v,dv,3.7,tol)
raiz_secante, cant_it_secante, iteraciones_secante, raices_secante = secante(v,a,b,tol)
raiz_nrm, cant_it_nrm, iteraciones_nrm, raices_nrm = nrm(v,dv, d2v ,3.6,tol)
raiz_pf, cant_it_pf, iteraciones_pf, raices_pf = puntofijo(g,a,tol)



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

plt.savefig('Volumen pedido vs altura.pdf') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf
plt.show()

#%% Convergencia 
alphapf, ctespf=convergencia(cant_it_pf, iteraciones_pf)
print('Método de punto fijo')
print(alphapf)
print()
print(ctespf)
print()
print()

alphab, ctesb=convergencia(cant_it_biseccion, iteraciones_biseccion)
print('Método de bisección')
print(alphab)
print()
print(ctesb)
print()
print()

alphanr, ctesnr=convergencia(cant_it_nr, iteraciones_nr)
print('Método de Newton-Raphson')
print(alphanr)
print()
print(ctesnr)
print()
print()

alphanrm, ctesnrm=convergencia(cant_it_nrm, iteraciones_nrm)
print('Método de Newton-Raphson Modificado')
print(alphanrm)
print()
print(ctesnrm)
print()
print()

alphas, ctess=convergencia(cant_it_secante, iteraciones_secante)
print('Método de la secante')
print(alphas)
print()
print(ctess)

#%% Gráfico raiz estimada
plt.figure(figsize=[12.8, 9.6])

#x=np.linspace(a,b)
biseccion=plt.plot(raices_biseccion, "-y", marker=".", label=r'$Bisección$')
newtonraphson=plt.plot(raices_nr, "-g",marker="D", label=r'$Newton-Raphson$')
secante=plt.plot(raices_secante, "-b", label=r'$Secante$')
puntofijo=plt.plot(raices_pf, "-r", marker="*", label=r'$Punto Fijo$')
#newtonraphsonmodificado=plt.plot(raices_nrm,"m", marker="D", label=r'$Newton-Raphson Modificado$')

i=0

plt.xlabel('Iteraciones')
plt.ylabel('Valor que toma la raíz')

plt.legend() #Muestra el cuadro de referencias
plt.title('Raíz estimada')

plt.savefig('Raiz estimada.pdf')
plt.show()

#%% Gráfico orden de convergencia
plt.figure(figsize=[12.8, 9.6])

#x=np.linspace(a,b)
biseccion=plt.plot(alphab, "-y", marker=".", label=r'$Bisección$')
newtonraphson=plt.plot(alphanr, "-g",marker="$+$", label=r'$Newton-Raphson$')
secante=plt.plot(alphas, "-b", label=r'$Secante$')
puntofijo=plt.plot(alphapf, "-r", marker="*", label=r'$Punto Fijo$')
newtonraphsonmodificado=plt.plot(alphanrm,"m", marker="$x$", label=r'$Newton-Raphson Modificado$')


plt.xlabel('Iteraciones')
plt.ylabel('Alfa')

plt.legend() #Muestra el cuadro de referencias
plt.title('Orden de convergencia')

plt.savefig('Convergencias.pdf')
plt.show()

#%%

print()
print("BIS", raiz_biseccion, v(raiz_biseccion))
print("N R", raiz_nr, v(raiz_nr))
print("SEC", raiz_secante, v(raiz_secante))
print("NRM", raiz_nrm, v(raiz_nrm))
print("P F", raiz_pf, v(raiz_pf))


#%%


fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

"""df = [[0, 4.25,0, 3.7,0, 3.6, 0,0,0, 0],
      [1, 2.125,1, 3.5585965900110637, 1, 3.557853744703987, 1, 3.020979276571371,1,3.2210526315789454],
      [2, 3.1875, 2, 3.5579176008547964, 2, 3.5579175825603797, 2, 3.359866211006268,2, 3.7910798122065725],
      [3, 3.71875, 3, 3.5579175827208025, 3, 3.5579175827208025,3, 3.4786638320982495,3, 3.554652843043188],
      [4, 3.453125,4, 3.557917582720802,"","", 4, 3.5253278792762472,4, 3.5578911513828166],
      [5, 3.5859375,"","","","", 5, 3.544375028761565,5, 3.5579175861230334],
      ["...", "...","","","","", "...", "..." ,6, 3.557917582720799],
      [30, 3.557917585829273,"","","","",17, 3.557917192978901,"",""],
      [31, 3.5579175838502124,"","","","",18, 3.5579174195832213,"",""],
      [32, 3.557917582860682, "","","","",19, 3.557917514434915, "",""],
      [33, 3.557917582365917, "","","","",20, 3.557917554137796,"",""], 
      [34, 3.5579175826132996,"","","","",21, 3.5579175707565693,"",""],
      [35, 3.557917582736991,"","","","",22, 3.5579175777128316,"",""]]"""


df = [[0, 4.25," "," ",
       0, 3.7," "," ",
       0, 3.6," "," ", 
       0,0," "," ",
       0, 0," "," "],
      
  [1, 2.125," "," ",
   1, 3.5585965900110637," "," ", 
   1, 3.557853744703987," "," ",
   1, 3.020979276571371," "," ",
   1,3.2210526315789454," "," "],
  
  [2, 3.1875," "," ", 
   2, 3.5579176008547964," "," ", 
   2, 3.5579175825603797," "," ", 
   2, 3.359866211006268," "," ",
   2, 3.7910798122065725," "," "],
      
  [3, 3.71875, 1.0, 0.5, 
3, 3.5579175827208025, 1.9724727008507454, 0.0321778874316884, 
3, 3.5579175827208025, 1.9859738886466718, 0.03437724148744091,
3, 3.4786638320982495, 0.47916058648500726, 0.19952023589292706,
3, 3.554652843043188, 0.5081736511562648, 0.3145896694408941],

     [4, 3.453125, 1.0, 0.5,
4, 3.557917582720802, 1.6642047953514383, 0.0033956468811862568,
"","", "","", 
4, 3.5253278792762472, 0.8914397440716146,0.3116991014894441,
4, 3.5578911513828166, "",""],

      [5, 3.5859375, 1.0, 0.5,
"","","","",
"","", "","",
5, 3.544375028761565, 0.9589159977044562 , 0.3598852585853662,
5, 3.5579175861230334,1.1206219223220522, 0.016299228695533484],
      ["...", "...","...","...",
       "","","","",
       "","","","", 
       "...", "...", "...","..." ,
       6, 3.557917582720799,"",""],
      
[30, 3.557917585829273,1.0,0.5,
"","","","",
"","","","",
17, 3.557917192978901,  0.9999973280595035, 0.41856364821872555,
"","","",""],
      
[31, 3.5579175838502124,1.0,0.5,
"","","","",
"","","","",
18, 3.5579174195832213, 0.9999988809544775, 0.4185718949151463,
"","","",""],

[32, 3.557917582860682,1.0,0.5,
 "","","","",
"","","","",
19, 3.557917514434915, 0.999999530787148, 0.41857558280593965,
"","","",""],
      
[33, 3.557917582365917,1.0,0.5,
 "","","","",
"","","","",
20, 3.557917554137796,  0.999999805815623, 0.4185772438981626,
"","","",""], 
      
[34, 3.5579175826132996,1.0,0.5,
"","","","",
"","","","",
21, 3.5579175707565693, 0.9999999267165008,0.418578018179187,
"","","",""],
      
[35, 3.557917582736991,1.0,0.5,
"","","","",
"","","","",
22, 3.5579175777128316, 0.9999999629403974, 0.41857826337174153,
"","", "",""]]


#columns=("", "bisección","", "Newton - Raphson","","Newton - Raphson Modificado","","Punto fijo","", "Secante")
columns=("", "bisección","P","\u03BB","", "Newton - Raphson","P","\u03BB","","Newton - Raphson Modificado","P","\u03BB","","Punto fijo","P","\u03BB","", "Secante","P","\u03BB")
tabla=ax.table(cellText=df, loc='center', colLabels=columns)
#tabla.auto_set_font_size(False)
#tabla.set_fontsize(2.5)


#fig.tight_layout()
plt.savefig("cuadro.pdf")
plt.show()



#%% Cálculo de la raíz con una función definida por Scipy

from scipy import optimize
root=optimize.brentq(v,0,2*R)
print ("Método scipy", root)

#%% Cálculo de la raíz con el programa resolvente.py

def f(a,b,c):
    x1= (-b+(b**2-4*a*c)**(1/2) )/(2*a)
    x2= (-b-(b**2-4*a*c)**(1/2) )/(2*a)
    return (x1,x2)


def calcularResolvente(a,b,c):
    epsilon = 1e3
    tol= 1e-5

    if 4*a*c>b**2:
        print ("MATH ERROR")
    else:
        if abs( b**2-4*a*c)<tol:
            print ("Hay una única x y es: ", round (f(a,b,c)[1],7))
        else:
            print ("x1 es: ",  (f(a,b,c)[0]))
            print ("x2 es: ",  (f(a,b,c)[1]))
       
print()
print('Método resolvente.py')
calcularResolvente(-pi,2*pi * 4.25,0)

<<<<<<< HEAD:Tanque (Final).py
=======
=======
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

"Definición de variables a utilizar"
pi=math.pi
R=4.25 #Radio
e1=10**(-5)
e2=10**(-13)

tol=1e-10 #Puedo tomar e1 o e2 dependiendo el error que necesite

n0=100 #Cantidad maxima de iteraciones

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

"Segunda derivada de f2" #ELIMINARRRRRRRRRR
def fxx2(x):
    return((pi*(2*3*R - 6*(x)))/3)


#%% Definición de funciones a utilizar 

def puntofijo(gx,a,tolera, iteramax = 100):
    
    iteraciones=[]
    raices=[]
    
    iteracion=[0, a]
    iteraciones.append(iteracion)
    raices.append(a)
    
    i = 1 # iteración
    b = gx(a)
    tramo = abs(b-a)
    
    iteracion=[0, b]
    iteraciones.append(iteracion)
    raices.append(b)
    
    while(tramo>=tolera and i<=iteramax ):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        print("error",tramo)
        i = i+1
        iteracion=[i, b]
        iteraciones.append(iteracion)
        raices.append(b)
    print("SE IMPRIMEN LAS RAICES DE PUNTO FIJO:",raices)
    respuesta = b
    # Validar respuesta
    if (i>=iteramax ):
        respuesta = np.nan
    
    print("Solucion aproximada PUNTO FIJO: {:.10}".format(respuesta))
    print("numero de iteraciones PUNTO FIJO: {:d}".format(i))
    #return(respuesta, i)
    return(respuesta, i, iteraciones, raices)



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
        raices=[]
        
        x=xbis(a,b)
        y=f(x)
        i=0 #Número de iteración
        e=1+t
        iteracion=[i, x]
        iteraciones.append(iteracion)
        raices.append(x)
        
        while (y!=0) and (e>t):
            
            if f(x)*f(a)>0: #Verifico si tienen mismo signo
                
                fant=v(x)
                a=x #Intervalo ahora es desde x hasta b
                x=xbis(a,b)
                y=f(x)
                i=i+1
                e=abs(y-fant)
                
                iteracion=[i, x]
                iteraciones.append(iteracion)
                raices.append(x)
                
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
                raices.append(x)
                
                print(i,x, e)
        
        #print('MÉTODO DE BISECCIÓN')        
        #print('La altura del tanque que logra contener el volumen requerido al 100% es',x, 'y se obtiene luego de', i,'iteraciones.')
        
        print("Solucion aproximada BISECCIÓN: {:.10}".format(x))
        print("numero de iteraciones BISECCIÓN: {:d}".format(i))
        print ()
        
        return(x, i, iteraciones, raices)



'''Método de Newton-Raphson''' #Belu
""" Realiza el calculo del metodo N-R"""
def calcular(f,df,panterior):

    pactual = panterior - (f(panterior)/df(panterior))
    return pactual

def calcularModificado(f,df,d2f,panterior):
    
    pactual = panterior -  (f(panterior)*df(panterior)) /   (   (df(panterior))**2 - f(panterior)*d2f(panterior) )    
    return pactual

""" Metodo Newton-Raphson: se reciben parametros y se realiza el metodo hasta que se obtenga un error menor a la tolerancia"""
def newton(f,df, po,tolerancia):
    iteraciones=[]
    raices=[]
  
    panterior = po
    
    iteracion=[0,panterior]
    iteraciones.append(iteracion)
    raices.append(panterior)
    
    error = tolerancia+1
    i = 1
    
    while error > tolerancia: 
        
        pactual = calcular(f,df, panterior)
        error = abs(pactual - panterior)
        panterior = pactual
        iteracion=[i, pactual]
        iteraciones.append(iteracion)
        raices.append(pactual)
       # print("actual", pactual, "anterior", panterior)
        i+=1
        print(error)
    print("Solucion aproximada NR: {:.10}".format(pactual))
    print("numero de iteraciones NR: {:d}".format(i))
    print ()
    
    return(pactual, i, iteraciones, raices)

"""Método de Newton-Raphson Modificado"""
def nrm(f,df,d2f,po,tolerancia):
    
    iteraciones=[]
    raices=[]
  
    panterior = po
    iteracion=[0,panterior]
    iteraciones.append(iteracion)
    raices.append(po)
    error = tolerancia+1
    i = 1
    
    while error > tolerancia: 
        
        pactual = calcularModificado(f,df, d2f, panterior)
        error = abs(pactual - panterior)
        print("actual", pactual, "anterior", panterior)
        panterior = pactual
        iteracion=[i, pactual]
        iteraciones.append(iteracion)
        raices.append(pactual)
        
        i+=1
        print(error)
    print("Solucion aproximada NR MODIFICADO: {:.10}".format(pactual))
    print("numero de iteraciones NR MODIFICADO: {:d}".format(i))
    print ()
    
    return(pactual, i, iteraciones, raices)



""" Pre: los parametros recibidos son válidos. En el caso del intervalo, se asume que cumple que el producto del intervalo evaluado en la funcion
    es menor a cero (f(a)*f(b) < 0; garantizando existencia de raíz por el teorema de Bolzano"""
def secante(f, pn_1, pn_2, tolerancia): 
    error = tolerancia + 1
    iteracion=[0,pn_1]
    i = 1
    iteraciones=[]
    raices=[]
    
    iteraciones.append(iteracion)
    raices.append(pn_1)
    
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
        raices.append(pn)
        
        print(pn)
        
    print("Solucion aproximada SECANTE: {:.10}".format(pn))
    print("numero de iteraciones SECANTE: {:d}".format(i))
    
    return(pn, i, iteraciones, raices)



def convergencia(numiteraciones,iteraciones):
    alphas=[] #Esto es para almacenar alpha y comparar que todas sean iguales - tienen que ser todos 1(convergencia lineal) o todos 2 (convergencia cuadrática)
    lambdas=[] #Lo mismo que la lista alphas, para comparar que tiendan a un mismo valor

    #i=2
    #while i<numiteraciones-1:
    for i in range (3-1,numiteraciones-1):
        print("Toy entrando a la convergenciaaa asdasasd")
        masuno=iteraciones[i+1][1]-iteraciones[i][1]
        menosuno=iteraciones[i][1]-iteraciones[i-1][1]
        menosdos=iteraciones[i-1][1]-iteraciones[i-2][1]
        
        if menosuno!=0 and menosdos!=0:
            alpha=((np.log10(np.abs(masuno/menosuno)))/(np.log10(np.abs(menosuno/menosdos))))
            alphas.append(alpha)
        if menosuno!=0:
            cteconvergencia=((np.abs(masuno))/((np.abs(menosuno))**alpha))
            lambdas.append(cteconvergencia)
        i=i+1
        
    
    
    return(alphas, lambdas)

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

plt.savefig('Funciones y sus derivadas.pdf') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf
plt.show()

#%% Cálculo de la solución

#Primero, busco cuánto vale el volumen maximo/cuál es el volumen del tanque más grande cuando lo llenamos al porcentaje que nos piden
#Por lo tanto, debemos buscar las raíces de la función que modela al tanque
#Haciendo un analisis cualitativo antes de ingresar datos, notamos que el valor máximo se obtiene cuando la altura es 2R.

b=2*R

p=xbis(a,b) #Semilla

"Define el volumen del tanque de máxima capacidad, lleno al porcentaje pedido."
vmax=lambda x: porcentaje_pedido*(4/3)*pi*(R**3)

"Define la función que modela el volumen lleno al 100%."
def f2(x):
    
    return((pi*(x**2)*(3*R-x))/3)

"Define la funcion para buscar la altura tal que, al llenar completamente el tanque, "
"éste contenga el volumen pedido."
"""v=lambda x:f2(x)-vmax(x)
dv=lambda x:fx2(x)
d2v=lambda x: fxx2(x) #Para utilizar en punto fijo

g= lambda x:x-v(x)
dg= lambda x:((v(x)*d2v(x))/((dv(x))**2))"""


volumenmax=(4/3)*pi*(4.25**3)*(18/(5*9.5))
v= lambda x: (pi*4.25*(x**2)-(pi/3)*(x**3)-volumenmax)
dv=lambda x: 2*pi*4.25*(x)-pi*(x**2)
d2v=lambda x: 2*pi*4.25-2*pi*x
g= lambda x:((((x**3)+4*(4.25**3)*(18/(5*9.5)))/(3*4.25)))**(1/2)

plt.figure(figsize=[12.8, 9.6])

# Intervalo a graficar
x=np.linspace(a, b) 

y1=v(x)
y2=dv(x)
#yx1=fx1(x)
#yx2=fx2(x)

#Grafico de cada función
plt.plot(x, y1, "-r", label=r'$v(x))$')
#plt.plot(x, y2, "-b", label=r'$f_2(x)$')
#plt.plot(x, yx1, "-r", label=r'$\frac{df_1(x)}{dx}$', ls='--') 
plt.plot(x, y2, "-b", label=r'$dv(x)$', ls='--')

#Marco eje x para distinguir donde estan los puntos con diferencia nula (Los que me interesan en este caso)
plt.axhline(color='black', lw=0.5)

#Configuración general del gráfico (Ejes, título, grilla, etc)
plt.xlim(a, b)
plt.xlabel('Altura')
#plt.ylabel('g')
plt.grid(True, 'both')
plt.legend() #Muestra el cuadro de referencias
#plt.title('Funciones volumen (lleno y al porcentaje pedido) y sus derivadas')

#plt.savefig('Funciones y sus derivadas.pdf') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf
plt.show()

pare='false'

raiz_biseccion, cant_it_biseccion, iteraciones_biseccion, raices_biseccion = biseccion(v,a,b,tol)
raiz_nr, cant_it_nr, iteraciones_nr, raices_nr = newton(v,dv,3.7,tol)
raiz_secante, cant_it_secante, iteraciones_secante, raices_secante = secante(v,a,b,tol)
raiz_nrm, cant_it_nrm, iteraciones_nrm, raices_nrm = nrm(v,dv, d2v ,3.6,tol)
raiz_pf, cant_it_pf, iteraciones_pf, raices_pf = puntofijo(g,a,tol)



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

plt.savefig('Volumen pedido vs altura.pdf') #Para agregarlo al informe hay que convertir el archivo de .svg a .emf
plt.show()

#%% Convergencia 
alphapf, ctespf=convergencia(cant_it_pf, iteraciones_pf)
print('Método de punto fijo')
print(alphapf)
print()
print(ctespf)
print()
print()

alphab, ctesb=convergencia(cant_it_biseccion, iteraciones_biseccion)
print('Método de bisección')
print(alphab)
print()
print(ctesb)
print()
print()

alphanr, ctesnr=convergencia(cant_it_nr, iteraciones_nr)
print('Método de Newton-Raphson')
print(alphanr)
print()
print(ctesnr)
print()
print()

alphanrm, ctesnrm=convergencia(cant_it_nrm, iteraciones_nrm)
print('Método de Newton-Raphson Modificado')
print(alphanrm)
print()
print(ctesnrm)
print()
print()

alphas, ctess=convergencia(cant_it_secante, iteraciones_secante)
print('Método de la secante')
print(alphas)
print()
print(ctess)

#%% Gráfico raiz estimada
plt.figure(figsize=[12.8, 9.6])

#x=np.linspace(a,b)
biseccion=plt.plot(raices_biseccion, "-y", marker=".", label=r'$Bisección$')
newtonraphson=plt.plot(raices_nr, "-g",marker="D", label=r'$Newton-Raphson$')
secante=plt.plot(raices_secante, "-b", label=r'$Secante$')
puntofijo=plt.plot(raices_pf, "-r", marker="*", label=r'$Punto Fijo$')
#newtonraphsonmodificado=plt.plot(raices_nrm,"m", marker="D", label=r'$Newton-Raphson Modificado$')

i=0

plt.xlabel('Iteraciones')
plt.ylabel('Valor que toma la raíz')

plt.legend() #Muestra el cuadro de referencias
plt.title('Raíz estimada')

plt.savefig('Raiz estimada.pdf')
plt.show()

#%% Gráfico orden de convergencia
plt.figure(figsize=[12.8, 9.6])

#x=np.linspace(a,b)
biseccion=plt.plot(alphab, "-y", marker=".", label=r'$Bisección$')
newtonraphson=plt.plot(alphanr, "-g",marker="$+$", label=r'$Newton-Raphson$')
secante=plt.plot(alphas, "-b", label=r'$Secante$')
puntofijo=plt.plot(alphapf, "-r", marker="*", label=r'$Punto Fijo$')
newtonraphsonmodificado=plt.plot(alphanrm,"m", marker="$x$", label=r'$Newton-Raphson Modificado$')


plt.xlabel('Iteraciones')
plt.ylabel('Alfa')

plt.legend() #Muestra el cuadro de referencias
plt.title('Orden de convergencia')

plt.savefig('Convergencias.pdf')
plt.show()

#%%

print()
print("BIS", raiz_biseccion, v(raiz_biseccion))
print("N R", raiz_nr, v(raiz_nr))
print("SEC", raiz_secante, v(raiz_secante))
print("NRM", raiz_nrm, v(raiz_nrm))
print("P F", raiz_pf, v(raiz_pf))


>>>>>>> d33e19aec20a4cf7ee993e27c6b87141b63f71dc
>>>>>>> 482447e573e583ad445c56ef6fbd78732d6cc0d0:tanque con b, nr, pf y s.py
