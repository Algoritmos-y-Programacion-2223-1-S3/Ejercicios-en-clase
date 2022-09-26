number = input("Please enter a number: ")
aux = 1

if number.isnumeric(): 
    number = int(number)
    number= number+1
    for number in range(1,number,2):
        while number>=1:
            if number == 1:
                print(number*2-1) 
            else:
                print(number, end=" ")
            number-=2

else:
    print("Input Error")