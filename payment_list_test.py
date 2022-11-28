"""
Single function:
Allows integration between {guests} & {nightly_cost} each persons cost from the dictionary generated from "guests".
It should replace the value in the dictionary with a calculation of cost: base_cost + cost of each night.
"""


def payment_list(rate, base_cost, guests, nightly_cost):
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


"""
Nightly Cost =
{day:cost} 

Guests =
{name:[days_CSV]}
"""