cars = ["ok", "ok", "ok", "faulty", "ok", "ok"] # list of strings
all_successful = True
for status in cars:
    if status == "faulty":
        print("stopping the production line")
        all_successful = False
        break #terminates the loops
    print(f"This car is {status}")
    print("shipping new car to customer")

else:
    print("All cars built successfully. No faulty cars")
