'''Write a program that stores the password string in a variable, 
ask the user for the password, 
and print out on screen if the password entered by the user matches the one 
stored in the variable regardless of case.
'''

password = "contraseña"

palabra = input("Introduce tu contraseña" + '\n')
palabra = palabra.lower()

if palabra == password:
    print("contraseña correcta")
elif palabra != password:
    print("contraseña incorrecta")
