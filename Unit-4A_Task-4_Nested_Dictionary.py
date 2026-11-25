students = {
    1: {"name": "karthik", "marks": 90},
    2: {"name": "siva", "marks": 85},
    3: {"name": "venkat", "marks": 95}
}

for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()