'''
Write a program that asks the user his/her age and shows on the screen all the years he/she has reached (from 1 to his/her age).
'''

edad = int(input("Introduce tu edad "))

for edad in range(0, edad):
    print(edad+1)
