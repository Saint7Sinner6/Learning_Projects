

""" Try creating a for loop that allows the total number of days to dictate variables in each iteration.

You could also try dynamically mapping each variable to a dictionary to allow for the recall of individual daily costs per person.
Doing so would provide a static platform to then manipulate.
Program becomes more robust.
"""

"""Nightly Rate Calculator Function"""

"""
Requirements:
1. Intake info: [Number of nights, Cost per night, Tax, Fees, People
2. Calculate base cost to even-split with all people
    Simple tax + fees
3. Based on count of nights for a person, output cost for individual using program.
4. Consider using a dictionary to store this information
5. Consider creating a class that would allow you to output variables for individuals and save the output into said dictionary.
"""

class guest():
    def __init__(self, name, nights):
        self.name = name
        self.nights = nights
    

print("This program calculates the split cost of a single person based on the number of nights they will be staying compared to the total number of nights for the rental")

# COLLECT VARIABLES
nights = int(input("Total nights you will be staying: "))
tax = int(input("Tax: "))
fees = int(input("Total of other fees: "))
people = int(input("Total Number of people: "))
rate = int(input("Nightly rate: "))
fees += tax
base_cost = fees / people

""" Current project: Build a for loop that handles the variable day input and calculates the nights out to their full """
# CALCULATING SINGLE PERSON COST


"""Figure out how to make a list of objects that adopt the class elements for guest, the build that into a primary function...
that will allow you to dynamically calculate the cost of each guest."""


"""Create a list to store the number of people staying per night initially.
Eventually append this information to a dictionary for each person, then use a function to iterate and add details per."""

people_per_night = {}
x = 1
for i in range(nights):
    count = int(input("How many people will be staying on night {}? ".format(str(x))))
    people_per_night[x] = count
    x += 1



"""Create a dictionary of lists. One list per person. key = name, value = name, list of nights staying (this needs to be identified for saving)"""



"""Guest loop practice:"""
people_dict = {}


"""Loop to set number of people staying per night"""
x = 1
total = 0
for guest in guests:
    for i in range(nights):
        count = int(input("How many people will be staying on night {}? ".format(str(x))))
        x += 1





x = 1
total = 0
for i in range(nights):
    count = int(input("How many people will be staying on night {}? ".format(str(x))))
    night_cost = rate/count
    total += night_cost
    x += 1
    
total += base_cost
print(total)


"""
Input:
1. Total number of nights
2. Cost per night
3. Fees (that do not change based on length of booking)

Output:
1. Cost of individual person referenced

Optional:
Create for-loop with input trigger to 


Plan:
1. Create primary calculation function
2. Wrap function in for-loop allowing the global() user_input=user_input_2
"""