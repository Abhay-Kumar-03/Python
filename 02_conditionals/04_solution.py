fruit = str(input("Enter your fruit name: "))
color = str(input("Enter the color of your fruit: "))

if fruit == "banana":
    if color == "green":
        print("Your fruit is a Green Banana and it is unripe.")
    elif color == "yellow":
        print("Your fruit is a Yellow Banana and it is ripe.")
    elif color == "brown":
        print("Your fruit is a Brown Banana and it is overripe.")
else:
    print("Your fruit is not a banana.")