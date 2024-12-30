distance = int(input("Enter you distance: "))

if distance <= 3:
    mode = "Walk"
elif distance <= 15:
    mode = "bike"
else:
    mode = "car"
print( "Your Transport Mode is: ", mode)