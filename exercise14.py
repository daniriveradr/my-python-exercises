'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total.
'''


precio = 3.49
descuento = 60/100

pan_fresco = 0
pan_vendido = input("Panes vendidos?..." + '\n' + "panes ")
pan_vendido = float(pan_vendido)

precio_panes = precio*pan_vendido
precio_oferta = precio_panes*descuento
print("Precio de venta normal $" + str(precio) + '\n' + "Su pan tiene una oferta del 60% de descuento por ser pan de ayer")

print("Su barra de pan tiene un precio de ... $" + str(round(precio_oferta, 2)))
