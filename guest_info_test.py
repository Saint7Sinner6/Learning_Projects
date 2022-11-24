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

test = guest_info(5)
print(test)