import numpy as np
from math import sqrt
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#utilizando numpy
print("La Suma", sum(numeros))
print("La Media", np.mean(numeros))
print("Desviacion estandar", np.std(numeros))

print("-----------------------------------")
#metodo "tradicional"
suma = 0
for num in numeros:
    suma += num

print("La suma", suma)

media = suma/len(numeros)
print("La Media", media)

suma2 = 0
for num in numeros:
    suma2 += (num - media)**2
des = suma2 / len(numeros)

#sqrt solo calcula la raiz cuadrada de un numero
resultado = sqrt(des)

print("Desviacion estandar", resultado )


