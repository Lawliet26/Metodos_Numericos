import numpy as np
import matplotlib.pyplot as plt

#se define la formula del trapecio y las variables a utilizar

def trapecio(n,x,fx,t):
    sum=0
    for i in range(1,n):
        sum=sum+fx[i]
        print(sum)
    I=(x[n]-x[0])*(fx[0]+2*sum+fx[n])/(2*t)        #se programa la formula del trapecio
    return I
#Se piden los valores y se programan las entradas
print('-------------------------------------------------------------------------------------------')

num=int(input('numero de datos a analizar:'))
h=float(input('ingrese el ancho de los trapecios'))
n=num
x=np.zeros([n])
fx=np.zeros([n])
print('introduce los datos')
for i in range(0,n):
    x[i]=input("x["+str(i)+']=')            #Ingrese el valor de los datos de x
    fx[i]= input("fx[" + str(i)+']=')         # Ingrese el valor de los datos de fx

#se programa la posicion de los valores dentro del arreglo
print('-------------------------------------------------------------------------------------------')

n=num-1
t=(x[n]-x[0])/h
print('El valor de la integral:', trapecio(n,x,fx,t))

#Grafica de la integral

plt.plot(x,fx)
plt.ylabel('fx')
plt.xlabel('x')
plt.show()
