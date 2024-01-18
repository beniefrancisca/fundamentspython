# python keywords when used inside a loop
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("stopping the production line")
        break #this will stop the loop so when it reaches faulty it will stop the loop
    print(f"This car is {status}")
    print("shipping new car to customer")

# if theres a faulty car but we just want to skip the line instead this is what to do

for status in cars:
    if status == "faulty":
        print("found faulty car, skipping")
        continue # it will jump back to the start of the loop
    print(f"This car is {status}")
    print("shipping new car to customer")

my_friends = {
    'Jose': 6,
    'Rolf': 12,
    'Anne': 6
}

do_i_know = 'Anne'

if do_i_know in my_friends:
    print(f'I know {do_i_know}')



