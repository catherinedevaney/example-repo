def cities():
    """
    Print the options for the destination cities.
    """
    print("Cities:")
    print("a = Paris")
    print("b = Barcelona")
    print("c = Milan")
    print("d = Dublin")
    print("q = quit")

# Define function hotel_cost which will calculate the total cost of the hotel
def hotel_cost(num_nights):
    """
    This function will take num_nights as an argument and return a total cost for the 
    hotel stay (you can choose the price per night charged at the hotel).
    """
    return num_nights * 100

# Define the function plane_cost, which will return the associated cost for each destination
def plane_cost(city_flight):
    """
    Obtain the price of the flight to a certain destination.

    Parameters:
    city_flight: user input choice of destination

    Returns:
    The current price for the flight
    """
    if cities_dict[city_flight] == "Paris":
        return 120
    if cities_dict[city_flight]  == "Barcelona":
        return 80
    if cities_dict[city_flight]  == "Milan":
        return 110
    if cities_dict[city_flight]  == "Dublin":
        return 70
    else:
        return 0


# Define the function car_rental which calculates the total cost for car hire
def car_rental(rental_days):
    """
    Calculate the cost for car hire.

    Parameters:
    rental_days: the number of days the user would like to hire a car for.

    Returns:
    The total cost for car hire for the whole period.
    """
    return rental_days * 30



# Define function holiday_cost which will calculate the total cost for the holiday
def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculate the total cost for the holiday.

    Parameters:
    num_nights: the number of night's the user would like to go away for
    city_flight: the cost of the flight
    rental_days: the number of days car hire is required for

    Return:
    The total holiday cost.
    """
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total


city_list = ["Paris", "Barcelona", "Milan", "Dublin"]


cities_dict = {"a": "Paris",
               "b": "Barcelona",
               "c": "Milan",
               "d": "Dublin"
               }


while True:
    # Display the city options
    cities()# Ask user to select their destination and assign to variable city_flight
    city_flight = input("Please choose which city you would like to visit:")
    
    if city_flight == "q":
        print("You have chosen to quit the programme.")
        break
    
    elif cities_dict.get(city_flight) in city_list:
        # Ask the user to enter the number of nights they want to go away for, save this as variable num_nights and check this the characters are digits after stripping any leading '-'
        while True:
            num_nights = input("How many nights do you want to stay?")
            if num_nights.lstrip('-').isdigit():
                num_nights = int(num_nights)
                break
            else:
                print("Invalid input, please enter a valid option")
            
        # Ask the user to enter the number of days they would like to hire a car for, save this as variable rental_days and check for valid input
            
        while True:
            rental_days = input("How many days would you like to hire a car for?")
            if rental_days.lstrip('-').isdigit():
                rental_days = int(rental_days)
                break
            else:
                print("Invalid input, please enter a number")
        
        print(f"The hotel cost is £{hotel_cost(num_nights)}, the flight cost is £{plane_cost(city_flight)} and the car rental cost is £{car_rental(rental_days)}.")
        print(f"The total cost is £{holiday_cost(num_nights,city_flight, rental_days)}")

    else:
        print("Invalid input, please choose an option from the list")


