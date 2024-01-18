# for loop used to repeat something a number of times
# it has a different way about itself

friends = ["Rolf", "Jen", "Anne"]

for friend in friends:  #it is a boolean comparison. friend is not defined but its teeling you to give you a new
    #variable etc basically saying for new variable in list and then you get one iteration out
    print(friend)


elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in elements:
    print(index)

    # it will print 10 times it can even work with text
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in elements:
    print("Hello world")

for index in range(10):
    print("Hello world")
# similar to the one above

for index in range(2, 20, 3):
    print(index)
    # it will print numbers 2 to 19 but every 3 numbers

# can be used in a list of dictionaries

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 75},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}")