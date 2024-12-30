number = int(input("Enter your number: "))

if number > 1:
    print("Enter valid number")
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")