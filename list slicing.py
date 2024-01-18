# slicing is a process of getting a part of a list

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[2:4])
# this prints out from index number 2 to 4

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[1:])
# this prints from index 1 to the end of list

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[:4])
# prints from the start of the list and not the 4th

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[:])
# prints everything in the list but a new list

# you can use negative numbers to count from the end of the list
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[-3:])
# start points and end points