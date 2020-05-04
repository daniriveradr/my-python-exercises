'''
Write a program that asks the user for a positive integer and displays the countdown from that number to zero separated by commas.
'''

num = int(input("Escribe un numero entero positivo: "))

for num in range(num, -1, -1):
    # num = str(num.sort(reverse=True))
    num = (num)
    print(num, end = ", ")
    
    

