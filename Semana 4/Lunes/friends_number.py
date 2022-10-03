def main():
    number = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))
    aux = number - 1
    aux2 = number2 - 1
    acum = 0
    acum2 = 0

    while aux >= 1:
        if number % aux == 0:
            acum += aux
        aux -= 1

    while aux2 >= 1:
        if number2 % aux2 == 0:
            acum2 += aux2
        aux2 -= 1

    if acum == number2 and acum2 == number:
        print(f"The numbers {number} and {number2} are friends") 
    else:
        print(f"The numbers {number} and {number2} are not friends") 


main()