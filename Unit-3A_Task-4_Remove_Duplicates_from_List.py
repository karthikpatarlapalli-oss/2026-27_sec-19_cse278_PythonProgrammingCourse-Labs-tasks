
list_data = [1, 2, 3, 4, 2, 3, 5, ]
unique = []

for item in list_data:
    if item not in unique:
        unique.append(item)

print("Original:", list_data)
print("Without duplicates:", unique)