number = input("Please enter a number: ")

if number.isnumeric():
    number = int(number)
    number= number+1 
    for number in range(1,number):
        print("*"*number)

else:
    print("Input Error")