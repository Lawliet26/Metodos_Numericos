import sympy as sp
from math import *                                                #se importan todas las funciones de la libreria

def newtonraphson():
    x=sp.symbols('x')                                             #se crea la variable y se define cual va a ser su invocaion
    print('-------------------------------------------------------------------------------------------')
    f= input('Ingrese la funcion de variable (x): ')              #se utilizara X como variable
    df=sp.diff(f)                                                 #se realiza la derivada de la funcion introducida
    f=sp.lambdify(x,f)                                            #Se nombra la funcion de la libreria que permite variar un simbolo
    df=sp.lambdify(x,df)                                          #Se nombra la funcion que permite variar un simbolo dentrod e la derivada
    x0=input('digite valor un valor inicial: ')                   #Se crean las entradas
    x0=float(x0)                                                  #Se le da formato a las entradas
    n = input('digite la cantidad de iteraciones a realizar: ')   #Se crea entrada de la cantidad de iteraciones
    n = int (n)                                                   #Se le da formato a las entradas
    tol = input('digite el error maximo permitido: ')             #Se crea la entrada del error maximo permitido
    tol = float(tol)                                              #Se le da formato al error
    print('-------------------------------------------------------------------------------------------')
    for k in range(n):                                            #Se crea el rango en el que se va a plaicar las formulas
        x1=x0-(f(x0)/df(x0))                                      #Se programa la formula general de newton raphson
        if((abs(x1-x0))<tol):                                     #Se crea la condicion del programa
            print('x',k+1,'=',x1,end=' ')                         #Se imprimen la repuesta de los calculos hechos
            print('Es una buena aproximación')                    #Se imprime el mensaje si se cumple la condicion
            return
        x0=x1                                                     #Se actualiza la nueva variable y se retorna a la funcion
        print('x',k+1,'=',x1)
newtonraphson()


