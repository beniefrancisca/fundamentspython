# used to repeat thing number of time
# using booleans

is_learning = True

while is_learning:
    print("You're learning")

# it will repeat it as long as the condition is true

# it will print repeatedly unless you have to stop the loop by doing

is_learning = True

while is_learning:
    print("You're learning")
    user_input = input("Are you still learning? ")
    is_learning = user_input == "yes"
# adding it will make it stop looping as you are inserting an answer

user_input = input("do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We stopped running")
