order_size = str(input("Enter your size: "))
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with extra shot"
else:
    coffee = order_size + " coffee"
print("Your ", coffee)