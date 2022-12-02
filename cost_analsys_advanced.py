"""
Please note that at this time, there is no error handling built in.
Any inaccurate input will likely result in program failure.

NEXT TASK:
1. Make this more robust with error handling for input strings that are inaccurate to the expected input using a while loop.
"""

# Gather name & number of days staying per person, then output a dictionary.
def guest_info(nights): 
    guests = {}
    persist = "continue"
    while persist.lower() != "done":
        name = input("What is the guest's name? ")
        name = name.capitalize()
        
        while True: # Arrival Day
            try:
                arrival_day = int(input("Which day will this person arrive? Please enter any number 1 - {nights}: ".format(nights=nights)))
                while arrival_day > int(nights) or arrival_day <= 0:
                    arrival_day = int(input("Your number doesn't fit the paramaters--any number from 1 - {nights}. Please indicate which day this person will arrive: ".format(nights=nights)))
                break

            except ValueError:
                print("Invalid input, please try again.")
        
        while True: # Departure Day
            try:
                departure_day = int(input("Which day will this person depart? Please enter any number {arrival} - {nights}: ".format(arrival=arrival_day, nights=nights)))
                while departure_day <= arrival_day or arrival_day > nights:
                    departure_day = int(input("Your number doesn't fit the paramaters--any number from {arrival} - {nights}. Please indicate which day this person will arrive: ".format(arrival=arrival_day, nights=nights)))
                break

            except ValueError:
                print("Invalid input, please try again.")

        guests.update({name:[*range(arrival_day,departure_day+1)]})
        print(guests)
        persist = input("Type 'done' if you are finished adding guests or enter/return if you have more to add: ")
    return guests

#Output of this function is a dictionary. {day:person_count}
def nightly_count(guests, nights):
    people_per_night = {}
    for i in range(1, nights+1):
        counter = 0
        for j in guests.values():
            if i in j:
                counter += 1
        people_per_night[i] = counter
    return people_per_night

# Output of this function is a dictionary that returns {day:cost/people}
def cost_analsys(rate, people_per_night):
    nightly_cost = {}
    for i in people_per_night.items():
        nightly_cost[i[0]] = (float("%.2f" % (rate / i[1])))
    return nightly_cost

# Output of this function is a dictionary that returns {name:total_price}
def payment_list(base_cost, guests, nightly_cost):
    name_to_cost = {}
    cost = 0
    for i in guests.items():
        for j in nightly_cost.items():
            if j[0] in i[1]:
                cost += float(j[1])
        cost += float(base_cost)
        name_to_cost.update({i[0]:cost})
        cost = 0
    return name_to_cost

# COLLECT VARIABLES
while True: # Nights
    try:
        nights = int(input("Total nights you will be staying: "))
        while nights <= 0:
            nights = int(input("Total nights you will be staying (must be greater than 0): "))
        break
    except ValueError:
        print("Invalid input, please try again. Must be a number greater than zero")

guests = guest_info(nights)
people_per_night = nightly_count(guests, nights)

while True: # Tax
    try:
        tax = float(input("Tax: "))
        break
    except ValueError:
        print("Invalid input, please try again. Must be a number greater than zero")

while True: # Fees
    try:
        fees = float(input("Total of other fees: ")) + tax
        break
    except ValueError:
        print("Invalid input, please try again. Must be a number greater than zero")

while True: # Rate
    try:
        rate = float(input("Nightly rate: "))
        break
    except ValueError:
        print("Invalid input, please try again.")

while True: # People
    try:
        people = int(max(people_per_night.values()))
        break
    except ValueError:
        print("Invalid input, please try again.")

while True: # Base Cost
    try:
        base_cost = fees / people
        break
    except ValueError:
        print("Invalid input, please try again.")

# RETURN VALUES TO USER
nightly_cost = cost_analsys(rate, people_per_night)
name_to_cost = payment_list(base_cost, guests, nightly_cost)

print("Additional details are as follows: ")
print("Because there are {x} people, each person will pay a one-time {y} in addition to their nightly rate".format(x=people, y=base_cost))

# PRINT LOOPS TO OUTPUT NIGHT COST SPLIT AND NAME TO COST SPLIT.

for i in nightly_cost.items():
    x = i[0]
    y = i[1]
    print("{x} will pay {y}".format(x=x, y=y))

for i in name_to_cost.items():
    x = i[0]
    y = i[1]
    print("{x} will pay {y}".format(x=x, y=y))

for i in guests.items():
    x = i[0]
    y = i[1]
    print("{x} is staying on the following nights: {y}".format(x=x, y=y))

