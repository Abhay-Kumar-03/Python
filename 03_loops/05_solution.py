input_str = str(input("enter your string: "))

for char in input_str:
    if input_str.count(char) == 1:
        print("First Non-Repeated Char is: ", char)
        break