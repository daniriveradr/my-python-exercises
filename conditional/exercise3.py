'''
Write a program that asks the user for two numbers and returns their division. 
If the user does not enter any numbers he must return an error message and if the divisor is zero as well.
'''
num1 = int(input("Ingrese un numero" + '\n'))
num2 = int(input("Ingrese un numero" + '\n'))

if num2 == 0:
    print("Error!!")
elif num2 >= 1:
    operacion = num1/num2
    print(int(operacion))    
