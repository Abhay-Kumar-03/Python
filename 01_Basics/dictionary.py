chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

print(chai_types.get("Masala"))
print(chai_types["Masala"])

chai_types["Green"] = "Fresh"
print(chai_types)


print(chai_types)
for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

if "Masala" in chai_types:
    print("I have Masala Chai in Dictionary")

print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"
print(chai_types)

chai_types.popitem()
print(chai_types)
del chai_types["Green"]
print(chai_types)

chai_types_copy = chai_types.copy()

tea_shop = {
    "chai": {"Masala" : "Spicy", "Ginger" : "Zesty"},
    "Tea": {"Green" : "Mild", "Black" : "Strong"}
}
print()
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])
print(tea_shop["Tea"]["Green"])


squared_num = {x:x**2 for x in range(6)}
print(squared_num)
print(squared_num.clear())

keys = ["Masala", "Ginger", "Lemon"]
print(keys)
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)