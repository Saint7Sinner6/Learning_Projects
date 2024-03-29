#!/usr/bin/env python3

"""
COST SPLIT CALCULATOR FOR VACATION AND TRAVEL ARRANGEMENTS.
"""
print("Thank you for using this cost calculator.\n"
      "You will be asked a series of questions regarding your trip, then we will calculate the split.\n"
      "Most accommodations have a flat rate fee and taxes based on the number of nights you will be staying, so everyone will split that equally.\n"
      "The nightly rate for each person based on the night will be calculated separately, then each person will be assigned their grand total.")

# INPUT ERROR HANDLING
def prompt_input(prompt, validation_func):
    while True:
        try:
            value = validation_func(input(prompt))
            return value
        except ValueError:
            print("Invalid input, please try again.")

def get_guest_info(nights): 
    guests = {}
    while True:
        name = prompt_input("What is the guest's name? ", str).capitalize()
        arrival_day = prompt_input("Which day will this person arrive? Please enter any number 1 - {}: ".format(nights), int)
        departure_day = prompt_input("Which day will this person depart? Please enter any number {} - {}: ".format(arrival_day, nights), int)
        guests.update({name:[*range(arrival_day, departure_day+1)]})
        
        persist = input("Type 'done' if you are finished adding guests or enter/return if you have more to add: ")
        if persist.lower() == 'done':
            break
    return guests

# RETURNS DICT: {day:total}
def calculate_counts(guests, nights):
    return {i: sum(i in j for j in guests.values()) for i in range(1, nights+1)}

# RETURNS DICT: {day:cost}
# COMPENSATES DIVISION FUNCTION FOR 0 GUESTS ON ANY NIGHT ALSO
def calculate_costs(rate, people_per_night):
    return {i: round(rate / count, 2) if count > 0 else 0 for i, count in people_per_night.items()}

# RETURNS DICT: {name:cost}
def calculate_payments(base_cost, guests, nightly_cost):
    return {name: sum(nightly_cost[night] for night in nights) + base_cost for name, nights in guests.items()}

# COLLECT USER INPUT
while True:
    try:
        nights = prompt_input("Total nights you will be staying (must be greater than 0): ", int)
        if nights != 0:
            break
    except:
        print("You entered 0, please try again.")

guests = get_guest_info(nights)
people_per_night = calculate_counts(guests, nights)
tax = prompt_input("Tax: ", float)
fees = prompt_input("Total of other fees: ", float) + tax
rate = prompt_input("Nightly rate: ", float)
people = max(people_per_night.values())
base_cost = fees / people if people > 0 else 0

# RETURN VALUES TO USER
nightly_cost = calculate_costs(rate, people_per_night)
name_to_cost = calculate_payments(base_cost, guests, nightly_cost)

print("Additional details are as follows: ")
print(f"Because there are {people} people, each person will pay a one-time {base_cost} in addition to their nightly rate.")

for day, cost in nightly_cost.items():
    print(f"Day {day} will cost {cost}")
    
for name, cost in name_to_cost.items():
    print(f"{name} will pay {cost}")

for name, nights in guests.items():
    print(f"{name} is staying on the following nights: {nights}")

for day, guest_count in people_per_night.items():
    if guest_count == 0:
        print(f"No one is stayin on night {day}. Consider removing this day from your reservation. Otherwise, someone will have to pay {rate}")