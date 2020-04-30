'''To pay a certain tax you must be over 16 years old and have an income equal to or greater than 1000 euros 
per month. Write a program that asks the user his/her age and monthly income and shows on the screen if 
the user has to pay taxes or not.
'''


print("Sistema tributario")

edad = int(input("Escriba su edad: "))
ingresos = int(input("Sus ingresos: $"))

if  edad >= 16:
    if ingresos >= 1000:
        print("Debes contribuir con tus impuestos")
else:   
    print("No debes contribuir aún")
