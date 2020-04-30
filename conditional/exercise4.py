'''Write a program that asks the user for an integer and displays whether it is odd or even.
'''
num = int(input("Escribe un numero..." + '\n'))

# division = num /2
# print(round(division))

if num%2==0:
    print(str(num) + " es par")
else:
    print(str(num) + " es impar")
