'''Bella Napoli Pizzeria offers vegetarian and non-vegetarian pizzas to its customers. The ingredients for each type of pizza are listed below.

Vegetarian ingredients: Pepper and tofu.
Non vegetarian ingredients: Pepperoni, Ham and Salmon.
Write a program that asks the user if they want a vegetarian pizza or not, and depending on their answer show them a menu with the available ingredients to choose from. You can only choose one ingredient besides the mozzarella and tomato that are in all the pizzas. At the end, the screen must show whether the pizza chosen is vegetarian or not and all the ingredients it contains.
'''


print("Bievenido a la Pizzeria Bella Napolitana")
pizza = input("Quieres pizza de Carnes o Vegetariana? ")

pizza = pizza.lower()

pimiento = "Pimiento"
tofu = "Tofu"

peperoni = "Peperoni"
jamon = "Jamón"
salmon = "Salmón"

if pizza == "vegetariana":
    # print("Haz elegido la pizza Vegetariana")
    print("Los ingredientes disponibles son" + '\n' + pimiento + '\n' + tofu)

    ingrediente = input("Elige un ingrediente ")
    ingrediente = ingrediente.lower()
        
    if ingrediente == "pimiento":
        print("Haz elegido una pizza " + pizza + " con " + pimiento)
    
    elif ingrediente == "tofu":
        print("Haz elegido una pizza " + pizza + " con " + tofu)


if pizza == "carnes":
    # print("Haz elegido la pizza Vegetariana")
    print("Los ingredientes disponibles son" + '\n' + peperoni + '\n' + jamon + '\n' + salmon + '\n')

    ingrediente = input("Elige un ingrediente: ")
    ingrediente = ingrediente.lower()
    pizza = ("de "+pizza)
        
    if ingrediente == "peperoni":
        pass
        # print("Haz elegido una pizza " + pizza + " con " + peperoni)
    
    elif ingrediente == "jamon":
        pass
        # print("Haz elegido una pizza " + pizza + " con " + jamon)

    elif ingrediente == "salmon":
        pass
        # print("Haz elegido una pizza " + pizza + " con " + salmon)



print("Tu pizza " + pizza + " lleva queso mozzarella, salsa de tomate, y " + ingrediente)


