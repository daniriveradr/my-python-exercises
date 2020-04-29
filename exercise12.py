peso_payaso = 112
peso_barbie = 75

cantidad_payasos = input("Cuantos payasos vendimos este mes? ")
cantidad_barbies = input("Cuantas muñecas vendimos este mes? ") 

total_payasos = peso_payaso * int(cantidad_payasos)
total_barbies = peso_barbie * int(cantidad_barbies)
pedido_total = total_payasos+total_barbies

print("Este mes vendimos " + cantidad_payasos +" de payasos y " + cantidad_barbies + " de muñecas. Y el peso total del envío fue de " + str(pedido_total) + "gr")
