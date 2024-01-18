ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)


friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]
#going to turn everything into lowercase names

# guests_lower = [g.lower() for g in guests]

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower

]
print(present_friends)

# make code more readable by doing this

present_friends = [
    name.title()
    for name in guests
    if name.lower() in [f.lower() for f in friends]
]
print(present_friends)