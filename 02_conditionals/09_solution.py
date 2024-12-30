year = int(input("enter your year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("It is a Leap Year")
else:
    print("It is not an leap year")