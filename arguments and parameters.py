# using arguments and parameters in def functions and also using dictionaries
def calculate_mpg():

    car = {
         "make": "ford",
         "model": "fiesta",
        "mileage": 2300,
        "fuel_consumed": 460
    }
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")

calculate_mpg()

# how to simplify the code above but yet still limited because of the structure

car = {
    "make": "ford",
    "model": "fiesta",
    "mileage": 2300,
    "fuel_consumed": 460
}

def calculate_mpg(car_to_calculate): #using whats inside the bracket so when you call
    # the function we must pass in data
    # like the dictionary above which goes inside the fucntion giving it an argument
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")

calculate_mpg({
    "make": "ford",
    "model": "fiesta",
    "mileage": 2300,
    "fuel_consumed": 460
})


#argument is a value you pass into the function
#parameter is a variable that accepts a value inside the function
