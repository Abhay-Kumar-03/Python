password = str(input("Enter Your Password: "))

if len(password) < 6:
    print("Your Password is Week!")
elif len(password) <=10:
    print("Your Password is Medium!")
else:
    print("Your Password is Strong!")