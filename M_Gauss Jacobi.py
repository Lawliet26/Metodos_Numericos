import numpy as np

def jacobi(A,b,x0,tol,n):
    D=np.diag(np.diag(A))
    LU=A-D
    x=x0
    for i in range (n):
        D_inv=np.linalg.inv(D)
        xtemp=x
        x=np.dot(D_inv,np.dot(-LU,x))+np.dot(D_inv,b)
        print("Iteracion",i,": x = ",x)
        if np.linalg.norm(x-xtemp)<tol:
            return x
    return x

filas =int(input("Introduce numero de filas: "))
columnas = int(input("Introduce numero de columnas: "))

A =[]
for i in range(filas):
    A.append([])
    for j in range (columnas):
        valor = float(input("Fila{}, Columna {} : ".format(i+1, j+1)))
        A[i].append(valor)

b = list(eval(input('Ingrese los valores de los vectores separados por coma (,): ')))
x0 = np.zeros(int(input("Ingrese el numero de incognitas: ")))
tol = float(input("Digite tolerancia: "))
n = int(input("Digite numero de iteraciones: "))
x = jacobi (A,b,x0,tol,n)