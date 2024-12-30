tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
print(tea_varities[-1])
print(tea_varities[:2])
print(tea_varities[3])

tea_varities[3] = "Herbal"
print(tea_varities)

tea_varities = ["Black", "Green", "Oolong", "White"]
tea_varities[1:2] = "Lemon"
print(tea_varities)
tea_varities = ["Black", "Green", "Oolong", "White"]
tea_varities[1:2] = ["Lemon"]
print(tea_varities)

print(tea_varities[1:1])
tea_varities[1:1] = ["test", "test"]
print(tea_varities)
tea_varities[1:3] = []
print(tea_varities)


for tea in tea_varities:
    print(tea)

for tea in tea_varities:
    print(tea, end="-")

if "Masala" in tea_varities:
    print("I have Masala tea")
tea_varities.append("Masala")
if "Masala" in tea_varities:
    print("\nI have Masala Tea")

tea_varities.pop()
print(tea_varities)

tea_varities.remove("Lemon")
print(tea_varities)

tea_varities.insert(1, "Masala")
print(tea_varities)

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)
print(tea_varities_copy is tea_varities)

tea_varities_copy.append("Lemon")
print(tea_varities_copy)
print(tea_varities)

squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_nums = [y**3 for y in range(10)]
print(cube_nums)