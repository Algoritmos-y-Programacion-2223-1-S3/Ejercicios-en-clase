from selection import selection

def main():
    lista = [3,5,7,1,4,8,9,2,6]
    lista = selection(lista)
    number = int(input("Please enter a number"))
    if binary_search(number, lista) != -1:
        print("The number", number,"is present")
    else:
        print("The number", number,"is not present")


def binary_search(number,lista):
    start = 0
    final = len(lista)-1
    middle = (start + final)// 2
    if len(lista) == 1:
        if lista[0] == number:
            return number
        else:
            return -1
        
    if number > lista[middle]:
        return binary_search(number,lista[middle:final])
    elif number < lista[middle]:
        return binary_search(number,lista[start:middle])
    else:
        return lista[middle]


main()