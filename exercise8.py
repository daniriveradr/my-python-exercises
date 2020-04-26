# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el 
# usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

tu_nombre = input("Por favor escribe tu nombre... ")
# print(tu_nombre.upper())
# tu_nombre = tu_nombre.upper()
# print(tu_nombre.count(''))
print(tu_nombre.upper() + " Tu nombre tiene " + str(len(tu_nombre)) + " sletras")

# location = 'Da'
# print(location.count(''))
