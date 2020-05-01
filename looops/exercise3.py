'''
Write a program that asks the user for a positive integer and displays all odd numbers from 1 to that number separated by commas.
'''

num = int(input("Escribe un numero entero positivo: "))

for num in range(1, num+1):
    if num%2==0:
        pass
    else:
        print(str(num) + " es impar")
    # print(num+1)

# division = num /2
# print(round(division))

