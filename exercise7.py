# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = input("Cuantas horas trabajas? ")
print(str("Trabajaste ")+ (horas_trabajadas) + str(" Horas"))
precio_hora = input("Cuanto cuesta la hora en $USD? ")
print((precio_hora) + " Dólares")
pago = int(horas_trabajadas) +  int(precio_hora)
print("Tu pago de hoy es de... $" + str(pago))
