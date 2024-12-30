chai = "lemon chai"
print(chai)

chai = "masala chai"
first_char = chai[0]
print(first_char)

slice_chai = chai[0:7]
print(slice_chai)

num_list = "0123456789"
num_list[:]
print(num_list)
num_list[2:7:2]
print(num_list)

print(chai.lower())
print(chai.upper())

chai = "   Masala Chai  "
print(chai)
print(chai.strip())


chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))
print(chai)

# string to list
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split())
print(chai.split(", "))

chai = "Masala Chai"
print(chai.find("Chai"))
print(chai.find("Chai")) # it gives (-1) because it can not find value

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} of {} chai"
print(order)
print(order.format(quantity, chai_type))

chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)
print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety))

chai = "Masala Chai"
print(len(chai))
for letter in chai:
    print(letter)

chai = "He said, \"Masala Chai is awesom\" "
print(chai)
chai = "Masala\nChai"
print(chai)
chai = r"Masala\nChai"
print(chai)

chai = "Masala Chai"
print("Masala" in chai)
print("masala" in chai)

