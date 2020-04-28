peso = float(input("Escribe tu peso en kg:"))

altura = float(input("Escribe tu altura en mt:"))

imc = peso/altura**2

print("Tu indice de masa corporal es: " + str(round(imc, 2)))
