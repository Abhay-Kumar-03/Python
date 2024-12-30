age = int(input("Enter Your Age First: "))

day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2


print("Ticekt Price for you is $", price)