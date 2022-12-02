from scipy.interpolate import lagrange
print('-------------------------------------------------------------------------------------------')
x = list(eval(input("Ingrese los valores de X separados por comas: ")))
y = list(eval(input('Ingrese los valores de Y separados por comas : ')))
p=lagrange(x,y)
print(p)