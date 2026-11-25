subjects = {
    "Python": 90,
    "Maths": 85,
    "English": 88
}

print("Subject Names:")
for key in subjects.keys():
    print(key)

print("Subject Marks:")
for value in subjects.values():
    print(value)

print("Subject and Marks:")
for key, value in subjects.items():
    print(key, ":", value)