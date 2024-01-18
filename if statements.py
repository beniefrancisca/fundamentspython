# how to use if statements
friend = "Rolf"
user_name = input("Enter upur name: ")

if user_name == friend:
    print("Hello, friend")
else:
    print("Hello, stranger!")


# have to be indented by four spaces for the if statement to run
# if you use print outside the if statement body it won't run
# it must be indented inside the body

# there is also the else statement, if the statement is false it will run the else
#statement


# everything in if statements can be a value or a boolean

name = input("enter your name: ")
print(bool(name))

if name:
    print("We know your name.")

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]
A
user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend")

elif user_name in family:
    print("Hello, family")
else:
    print("i don't know you")

# good examples