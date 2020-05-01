'''
In a given company, its employees are evaluated at the end of each year. The points that they can obtain in the evaluation start at 0.0 and can be increased, translating into better benefits. The points that employees can get can be 0.0, 0.4, 0.6 or more, but not intermediate values between the figures mentioned. Below is a table with the levels corresponding to each score. The amount of money achieved in each level is 2,400 euros multiplied by the score of the level.

Level Score
Unacceptable = 0.0
Acceptable = 0.4
Meritorious = 0.6 or more
Write a program that reads the user's score and indicates their level of performance, as well as the amount of money the user will receive.

'''
calificacion = input("Calificación de empleado Pepe Perez...")

salario = 2400

if calificacion == 'inaceptable':
    calificacion_n = ((salario* 0.0) + (salario))
elif calificacion == 'aceptable':
    calificacion_n = ((salario* 0.4) + (salario))
elif calificacion == 'meritorio':
    calificacion_n = ((salario* 0.6) + (salario))    

print("Su calificación es " + calificacion + " y recibe un salario de: " + str(calificacion_n))

