numbers = [i for i in range(1, 11)]

squares = [i**2 for i in numbers]

even = [i for i in numbers if i % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even Numbers:", even)