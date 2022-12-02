from math import *
import sympy as sp

def biseccion():
    x = sp.symbols('x')
    print('-------------------------------------------------------------------------------------------')
    f = input("escriba una función con variable : ")
    f= sp.lambdify(x,f)
    a=float(input('Ingrese el valor del limite inferior del rango:'))
    b=float(input('ingrese el valor del limite superior del rango:'))
    tol=float(input('ingrese el valor del error maximo permitido:'))
    m1=a;
    m=b;
    k=0;
    if(f(a)*f(b)>0):                         #se pone la condicion para evitar que la funcion no tenga solucion
        print('La funcion no tiene raiz')

    while(abs(m1-m)>tol):
        m1=m;
        m=(a+b)/2;
        if(f(a)*f(m)<0):     #Si el la operacion es menos a 0 por lo tanto cambia se signo en el intervalo [a,m]
            b=m;
        if (f(m) * f(b) < 0):  # Si el la operacion es menos a 0 por lo tanto cambia se signo en el intervalo [m,b]
                a = m
        print('-------------------------------------------------------------------------------------------')
        print('el intervalo es [',a,',',b,']')   #se imprime el intervalo en el que se encuentra el punto
        k=k+1;
    print('x',k,'=',m,'Es una buena aproximacion')  #se imprime la aproximacion que cumple con la condicion y se indica como la mas exacta

biseccion()


