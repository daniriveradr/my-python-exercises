'''
Write a program for a company that has game rooms for all ages and wants to automatically calculate the price it should charge its customers to enter. The program should ask the user the age of the customer and show the price of the ticket. If the customer is under 4 years old he can enter for free, if he is between 4 and 18 years old he must pay 5 $ and if he is over 18 years old he must pay 10$.
'''

edad = input("Coloca tu edad por favor...")
edad = int(edad)

if edad <= 4:
    print("Puedes entrar gratis")
elif edad > 4 and edad < 18:
    print("Tienes que pagar 5 euros")
elif edad > 18:
    print("Tienes que pagar 10 euros")    
