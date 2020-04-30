'''
The tax brackets for filing a tax return in a given country are as follows:

Less than 10,000 euros = 5%
Between 10,000 and 20,000 euros = 15%
Between 200,000 and 35,000 euros = 20%
Between 350000 ? and 60000 ? = 30%
More than 60000 euros = 45%

Write a program that asks the user his annual income and shows on screen the tax rate that corresponds to him.



'''
renta_a = int(input("Coloca el valor de tu renta anual... " + '\n' + "$"))
impuesto = 5
if renta_a <= 10000:
    print("Le corresponde el tipo impositivo del " + str(impuesto*1) + "%")

if (renta_a >= 10000 and renta_a < 20000): 
    print("Le corresponde el tipo impositivo del " + str(impuesto*3) + "%")    

if (renta_a >= 20000 and renta_a < 35000): 
    print("Le corresponde el tipo impositivo del " + str(impuesto*4) + "%")    

if (renta_a >= 35000 and renta_a < 60000): 
    print("Le corresponde el tipo impositivo del " + str(impuesto*6) + "%")    

if (renta_a >= 60000): 
    print("Le corresponde el tipo impositivo del " + str(impuesto*9) + "%")    


# # Solution
# income = float(input("¿Cuál es tu renta anual? "))
# if income < 10000:
#     tax = 5
# elif income < 20000:
#     tax = 15
# elif income < 35000:
#     tax = 20
# elif income < 60000:
#     tax = 30
# else:
#     tax = 45
# print("Tu tipo impositivo es " + str(tax) + "%")
