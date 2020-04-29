'''
Write a program that asks the user their age and shows on the screen whether they are of legal age or not.
'''

edad = int(input("Por favor escribe tu edad "))

if edad <= 18:
    print("Eres menor de edad")
elif edad >= 18:
    print("Eres mayor de edad")
