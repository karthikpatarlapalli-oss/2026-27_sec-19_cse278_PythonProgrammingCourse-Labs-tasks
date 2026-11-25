students = [
    {"name": "karthik", "marks": 85},
    {"name": "siva", "marks": 95},
    {"name": "venkat", "marks": 75}
]

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
print(ascending)

print("Descending Order:")
print(descending)