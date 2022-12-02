from math import *
import numpy as np
import sympy as sp

def derivacion():
    x = sp.symbols('x')
    f = input('Ingrese la funcion de variable (x): ')
    f=sp.lambdify(x, f)
    a= float(input('Digite un valor inicial (Xo): '))
    h= float(input('Digite valor h: '))
    dx=h/2
    n= input("diga cual diferencia (central, progresivo, regresivo): ")

    if n== 'central':
        Aprox1= (f(a +dx) - f(a - dx))/(2*dx)
        print('------------------------------------------------------------------------')
        print('El valor de h es', h)
        print('El metodo usado fue', n)
        print('La primera derivada evaluada en el punto es', Aprox1)
        print('------------------------------------------------------------------------ ')
    elif n== 'progresivo':
        Aprox2= (f(a + dx) -f(a))/dx
        print('------------------------------------------------------------------------ ')
        print('El valor de h es', h)
        print('El metodo usado fue', n)
        print('La primera derivada evaluada en el punto es', Aprox2)
        print(' ------------------------------------------------------------------------')
    elif n== 'regresivo':
        Aprox3= (f(a) - f(a -dx))/dx
        print('------------------------------------------------------------------------ ')
        print('El valor de h es', h)
        print('El metodo usado fue', n)
        print('La primera derivada evaluada en el punto es', Aprox3)
        print('------------------------------------------------------------------------')
    else:
        Aprox1 = (f(a + dx) - f(a - dx))/(2*dx)
        Aprox2 = (f(a + dx) - f(a))/dx
        Aprox3 = (f(a) - f(a - dx))/dx
        print(' ')
        print('El valor de h es', h)
        print(' ')
        print('Diferencias centrales:', Aprox1)
        print('Diferencias progresivas:', Aprox2)
        print('Diferencias regresivas:', Aprox3)
derivacion()