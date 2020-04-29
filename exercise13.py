'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de 
ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''

deposito = input("Bienvenido a tu banco!. Por favor ingresa la cantidad a depositar ..." +'\n'+ "$")
print("Si el banco te remunerara los intereses estos serían los resultados")
deposito = float(deposito)
intereses = 4/100
reembolso = float(deposito) * intereses
print("Este es tu saldo en 1 año + $" + str(round(deposito+reembolso*1, 2)) + '\n' + "Este es tu saldo en 2 años + $" + str(round(deposito+reembolso*2, 2)) + '\n' + "Este es tu saldo en 3 años + $" + str(round(deposito+reembolso*3, 2)) + '\n')

'''print("Si el banco te cobrara los intereses estos serían los resultados")

cobro_intereses = float(deposito) *4/100
restante = float(deposito) - float(cobro_intereses)
restante1 = float(deposito) - (float(cobro_intereses) * 3)
print("Este es tu saldo en 1 año - $" + str(round(float(deposito) - (float(cobro_intereses) * 1))) + '\n' + "Este es tu saldo en 2 años - $" + str(round(float(deposito) - (float(cobro_intereses) * 2))) + '\n' + "Este es tu saldo en 3 años - $" + str(round(float(deposito) - (float(cobro_intereses) * 3))))
print(restante1)
# print(cobro_intereses)
'''
