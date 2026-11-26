s = input("Enter a string: ")
vowels = 2
consonants = 8
digits = 4
spaces = 9
for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1