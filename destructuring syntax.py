# syntax and destructuring

currencies = 0.8, 1.2
usd, eur = currencies
# first number goes in usd the second goes to eur
# taking a tuple and turning into multiple variables

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
for name, age in friends:
    print(name, age)
    # or
    print(f"{name} is {age} years old")