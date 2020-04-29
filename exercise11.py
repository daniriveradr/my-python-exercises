'''Write a program that asks the user an amount to invest, 
the annual interest and the number of years, and shows by screen the capital obtained in the investment.'''

inversion= input("Cuanto dinero vas a invertir?  $")
print("$" + inversion+ " USD")

interes = input("Qué cuota de intereses anual desea??")
print(interes + "%")

tiempo_a = input("Por cuantos años va a mantener su inversión? " )
print(tiempo_a + " años")

# resultado1 = float(inversion) * float(interes)
# retorno = float(resultado1) * float(tiempo)
tiempo = float(tiempo_a) * 12
interes_m = float(interes)/tiempo
retorno = float(interes_m)*float(inversion)

# print(str(tiempo))

print("Este seria el dinero $" + str(round(retorno, 2)) +" que obtendrias inviertiendo $" + inversion + " en " + str(tiempo_a) +" años")
# print(str(resultado1))






''' Codigo de prueba 🔻🔻🔻🔻








# inversion_m = float(inversion_m)
# interes_a = float(interes_a)
# tiempo = float(tiempo)

# intereses = interes_a*100/100

# # inversion_a = inversion_m * intereses
# # interes_m = interes_a / 12
# # inversion_a = interes_m * inversion_m
# # print(interes_m)
# # print(inversion_m)
# print(intereses)
# # print(inversion_a)


# # retorno = inversion * tiempo


# # print("Este es el retorno de su inversión: $" + str((retorno)) + " en " + str(round(tiempo)))

# dinero = 1000
# interes_m = 0.0375
# tiempo = 12

# # rentabilidad = dinero * interes_m * tiempo
# resultado = dinero * tiempo * interes_m/100

# print(str(resultado) + "%")

# dinero = 1000
# interes_m = 4.5
# tiempo = 12

# # rentabilidad = dinero * interes_m * tiempo
# resultado = dinero * tiempo * interes_m/100

# print(str(resultado) + "%")

'''
