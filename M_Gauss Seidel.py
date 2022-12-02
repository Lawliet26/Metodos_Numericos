import numpy as np

print('-------------------------------------------------------------------------------------------')
m=int(input('Ingrese el numero de Filas(m):'))        #Se genera la entrada para las filas
n=int(input('Ingrese el numero de columnas(n):'))     #Se genera la entrada para las columnas
matrix = np.zeros((m,n))                           #se define la matriz en 0s
x=np.zeros((m))                                    #Se define el vector solucion tambien en 0s

vector=np.zeros((n))
comp=np.zeros((m))
error=[]

print('-------------------------------------------------------------------------------------------')
print ('Método de Gauss-Seidel')
print ('Introduce la matriz de coeficientes y el vector solución')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] ")) #Se crea un ciclo para introducir los valores de la matriz
    vector[(r)]=float(input('b['+str(r+1)+']: '))

itera=int(input('Digite el numero de iteraciones que quiere realizar:'))
tol=float(input('Error maximo permitido:'))

print('-------------------------------------------------------------------------------------------')
#Metodo de Gauss-Seidel
k=0
while k<itera:
    suma=0
    k=k+1
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            if (c != r):
                suma=suma+matrix[r,c]*x[c]           #Se realiza el despeje de las ecuaciones
        x[r]=(vector[r]-suma)/matrix[r,r]
        print('x['+str(r)+']: '+str(x[r]))
    del error[:]

    print('-------------------------------------------------------------------------------------------')
    #Comprobación
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            suma=suma+matrix[r,c]*x[c]
        comp[r]=suma
        dif=abs(comp[r]-vector[r])
        error.append(dif)
        print('Error en x[',r,']=b',error[r])
    print('Iteraciones: ',k)
    if all(i>tol for i in error) == True:
        break

print('El ejercicio ha terminado')