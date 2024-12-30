pet_type = str(input("Enter your pet type dog or cat: "))
pet_age = int(input("Enter age of your pet age: "))

if pet_type == "dog":
    if pet_age < 2:
        food = "Puppy Food"
    else:
        food = "Adult Food"
    print(food ,"is suitable for your pet!")
elif pet_type == "cat":
    if pet_age < 5:
        food = "Junior Food"
    else:
        food = "Senior Food"
    print(food ,"is suitable for your pet!")