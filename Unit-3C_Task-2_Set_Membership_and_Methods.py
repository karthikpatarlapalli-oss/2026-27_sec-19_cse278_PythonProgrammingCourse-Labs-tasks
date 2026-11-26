s = {10, 20, 30, 40}

print("Original Set:", s)

print("20 in set:", 20 in s)
print("50 in set:", 50 in s)

s.add(50)
print("After add:", s)

s.remove(30)
print("After remove:", s)

s.discard(60)
print("After discard:", s)