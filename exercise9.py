peso = float(input("Escribe tu peso en kg:"))
print(type(peso))
altura = float(input("Escribe tu altura en mt:"))
print(type(altura))

imc = peso/altura**2

print("Tu indice de masa corporal es: " + str(round(imc, 2)))
