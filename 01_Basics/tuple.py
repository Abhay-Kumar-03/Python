# tuple is unmutable means un changeable

tea_types = ("Black", "Green", "Oolon")
print(tea_types)

print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])

print(len(tea_types))

more_tea = ("Herbal", "Early Grey")
all_tea = more_tea + tea_types
print()
print(all_tea)

if "Green" in all_tea:
    print("Yes")

more_tea = ("Herbal", "Early Grey", "Early Grey")
print(more_tea)
print(more_tea.count("Early Grey"))

print(tea_types)

(black, green, Oolong) = tea_types
print(black)
print(type(tea_types))

