from math import *
import sympy as sp

def puntofijo():
    x= sp.symbols('x')
    print('-------------------------------------------------------------------------------------------')
    g=input('digite la funcion despejada: ')
    g=sp.lambdify(x,g)
    x0=input('digite valor un valor inicial: ')
    x0=float(x0)
    n = input('digite la cantidad de iteraciones a realizar: ')
    n = int (n)
    tol = input('digite el error maximo permitido: ')
    tol = float(tol)
    print('-------------------------------------------------------------------------------------------')
    for k in range(n):
        x1=g(x0)
        if(abs(x1-x0)<tol):
            print('x',k+1,'=',x1,'es un punto fijo')
            return
        x0=x1
        print('x',k+1,'=',x1)
puntofijo()
