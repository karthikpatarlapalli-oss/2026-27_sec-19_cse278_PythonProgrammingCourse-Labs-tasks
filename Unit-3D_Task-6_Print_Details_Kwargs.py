def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(name="Karthik", age=19, city="vijayawada")