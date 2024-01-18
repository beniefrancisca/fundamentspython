numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)
print(doubled_numbers)



doubled_numbers = [number * 2 for number in numbers]
# this is a more simplified version of whats above

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old" for age in friend_ages]
print(age_strings)

# names = ["Rolf", "Bob", "Jen"]
# lower = [name.lower() for name in names]
# print(lower)

friend = input("Enter your friend name: ")
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends:
    print(f"{friend.title} is one of your friends")
m