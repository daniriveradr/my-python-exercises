# Escribir un programa que lea un entero positivo, 𝑛, introducido por el usuario y 
# después muestre en pantalla la suma de todos los enteros desde 1 hasta 𝑛. 
# La suma de los 𝑛 primeros enteros positivos puede ser calculada de la siguiente forma:
# suma=𝑛(𝑛+1)/2

n = input("Por favor introduce un numero... ")
n = int(n)
print(type(n))
# # n = int(n)
# operacion = (n+1)/(2)
operacion = n*(n+1)/(2)
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(round(operacion)))
