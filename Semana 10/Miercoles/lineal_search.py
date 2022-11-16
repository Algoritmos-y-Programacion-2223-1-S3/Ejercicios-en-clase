def main():
    lista = [3,5,7,1,4,8,9,2,6]
    number = int(input("Please enter a number"))
    if lineal_search(number, lista):
        print("The number", number,"is present")
    else:
        print("The number", number,"is not present")


def lineal_search(number,lista):
    for n in lista:
        if number == n:
            return number

main()