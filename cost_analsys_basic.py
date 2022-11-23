#Output of this function is a dictionary. Day number is key, person count is value.
def nightly_count(nights):
    people_per_night = {}
    x = 1
    for i in range(nights):
        count = int(input("How many people will be staying on night {}? ".format(str(x))))
        people_per_night[x] = count
        x += 1
    return people_per_night

def cost_analsys(base_cost, rate, people_per_night)
    nightly_cost = {}
    for i in people_per_night.items():
        nightly_cost[i[0]] = (float("%.2f" % (rate / i[1])) + base_cost)
    return nightly_cost

# COLLECT VARIABLES
nights = int(input("Total nights you will be staying: "))
people_per_night = nightly_count(nights)
tax = int(input("Tax: "))
fees = int(input("Total of other fees: ")) + tax
rate = int(input("Nightly rate: "))
people = int(max(people_per_night.values()))
base_cost = fees / people

# Return Values to user
cost_breakdown = cost_analsys(base_cost, rate, people_per_night)
print(cost_breakdown)