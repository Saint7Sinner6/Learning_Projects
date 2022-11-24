"""Class Creation"""
"""
Default Requirements and attributes:

The premis is going to be creating a nested dictionary where each instantiated object appends to a dictionary and contains the elements for nights, cost, etc :
Eg. {name_key : {nights:[1, 3, 4], total:$_value, }

1. Intake total number of nights from a pre-defined variable (feed this through via the for loop)
2. 
3. Append the name as key and a list as value to dictionary
"""

# Gather names & number of days staying per person.
def guest_info(nights):
    guests = {}
    persist = "continue"
    while persist.lower() != "done":
        name = input("What is the guest's name? ")
        name = name.capitalize()
        days = int(input("How many days will this person be staying? "))
        while days > int(nights) or days <= 0:
            days = int(input("Please input a number less than {x} and greater than 0: ".format(x=nights)))
        guests.update({name:days})
        persist = input("Type 'done' if you are finished adding guests or enter/return if you have more to add: ")
    return guests


#Output of this function is a dictionary. Day number is key, person count is value.
def nightly_count(nights):
    people_per_night = {}
    x = 1
    for i in range(nights):
        count = int(input("How many people will be staying on night {}? ".format(str(x))))
        people_per_night[x] = count
        x += 1
    return people_per_night

def cost_analsys(rate, people_per_night):
    nightly_cost = {}
    for i in people_per_night.items():
        nightly_cost[i[0]] = (float("%.2f" % (rate / i[1])))
    return nightly_cost

# COLLECT VARIABLES
nights = int(input("Total nights you will be staying: "))
while nights <= 0:
    nights = int(input("Total nights you will be staying (must be greater than 0): "))
guests = guest_info(nights)
people_per_night = nightly_count(nights)
tax = float(input("Tax: "))
fees = float(input("Total of other fees: ")) + tax
rate = float(input("Nightly rate: "))
people = int(max(people_per_night.values()))
base_cost = fees / people

# Return Values to user
cost_breakdown = cost_analsys(base_cost, rate, people_per_night)

print("Additional details are as follows: ")
print("Because there are {x} people, each person will pay a one-time {y} in addition to their nightly rate".format(x=people, y=base_cost))

for i in cost_breakdown.items():
    x = i[0]
    y = i[1]
    print("Those staying on night {x} will pay {y}".format(x=x, y=y))



"""
NEXT TASK:
1. Make this more robust with error handling for input strings that are inaccurate to the expected input using a while loop.
2. Add the ability to input the names of those staying, and calculate the totals for each person based on how many nights they are staying.
"""