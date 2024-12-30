items = ["apple", "banana", "cherry", "apple", "date", "elderberry"]

unique_item = set() # Create an empty set

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    else:
        unique_item.add(item) # Add item to the set