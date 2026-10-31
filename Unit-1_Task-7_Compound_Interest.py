
# Compound Interest Calculator

p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate: "))
t = float(input("Enter time in years: "))

amount = p * (1 + r / 100) ** t

ci = amount - p

print("Compound Interest =", ci)
print("Total Amount =", amount)
