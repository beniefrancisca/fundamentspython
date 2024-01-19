# first class functions
# assigns functions to variables using them as values to lists

def greet():
    print("hello")

greet()

# or
def greet():
    print("hello")


hello = greet
hello()

# more useful example to calculate the average of a sequence

def average(seq):
    return sum(seq) / len(seq)

# example 2

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"students:{name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == "top":
        print(top(grades))

# we can make this code shorter by doing an operation dictionary
# then you just get the operations functions, removing the if statements instead

operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"students: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades))