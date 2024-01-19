# one example

friends = ["Rolf", "John", "Anne"]

counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)

# another example

friends = ["Rolf", "John", "Anne"]

for counter, friend in enumerate(friends, start = 1):
    print(counter)
    print(friend)
print(list(enumerate(friends)))
print(dict(enumerate(friends)))