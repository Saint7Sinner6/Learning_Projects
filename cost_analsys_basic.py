#Output of this function is a dictionary. Day number is key, person count is value.
def nightly_count(nights):
    people_per_night = {}
    x = 1
    for i in range(nights):
        count = int(input("How many people will be staying on night {}? ".format(str(x))))
        people_per_night[x] = count
        x += 1
    return people_per_night

def cost_analsys(base_cost, rate, people_per_night):
    nightly_cost = {}
    for i in people_per_night.items():
        nightly_cost[i[0]] = (float("%.2f" % (rate / i[1])))
    return nightly_cost

# COLLECT VARIABLES
nights = int(input("Total nights you will be staying: "))
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