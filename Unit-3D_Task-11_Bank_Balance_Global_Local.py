balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("After deposit:", balance)

def local_balance():
    balance = 500
    print("Local balance:", balance)

print("Initial balance:", balance)
deposit(500)
local_balance()
print("Final account balance:", balance)