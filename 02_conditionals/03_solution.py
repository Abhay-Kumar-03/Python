score = int(input("Enter Your Score: "))

if score > 100:
    print("Wrong Score")
    exit()
elif score < 0:
    print("Wrong Score")
    exit()
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")