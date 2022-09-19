print("*** Welcome to Bella Napoli ***")
option = input("Please enter a option: \n1-Vegetarian\n2-Non Vegetarian\n->")
if option.isnumeric():
    option=int(option)
    if option == 1:
        ingredient = input("Please enter an ingredient: \n1-Pimiento\n2-Tofu\n->")
        if ingredient == "1":
            ingredient = "Pimiento"
        else:
            ingredient = "Tofu" 
        print(f"The pizza is vegetarian and have {ingredient}")
    elif option == 2:
        ingredient = input("Please enter an ingredient: \n1-Pepperoni\n2-Jamon\n3-Salmon\n->")
        if ingredient == "1":
            ingredient = "Pepperoni"
        elif ingredient == "2":
            ingredient = "Jamon" 
        else: 
            ingredient = "Salmon"
        print(f"The pizza is non vegetarian and have {ingredient}")
    else:
        print("Invalid option")
else: 
    print("Error")