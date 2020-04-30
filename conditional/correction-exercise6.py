'''Students in a course have been divided into two groups A and B according to gender and name. Group A consists of women with a name before M and men with a name after N and group B for the rest. Write a program that asks the user his/her name and sex, and shows the corresponding group on the screen.


Note: Sorry if it looks ugly all the code I didn't know how to use some way to write less lines of code, but the important thing is that it meets the objective and works.
'''
nombre = input("Introduce tu nombre ")
genero = input("Introduce tu genero ")
nombre = nombre.lower()
letra = nombre[0]
# print(letra)
genero = genero.lower()

if (genero == "femenino" and nombre < 'm') or (genero == "masculino" and nombre > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)

'''
I didn't know that I could use less than and greater than; and that Python detects that I'm referring to the alphabet 
No sabia que podía hacer uso de menor que y mayor que; y que python detecta que me refiero al alfabeto.
'''
