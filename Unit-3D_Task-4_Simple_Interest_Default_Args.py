def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    print("Simple Interest =", si)

simple_interest(1000, 2)

simple_interest(1000, 2, 10)