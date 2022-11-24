def guest_info(nights):
    guests = {}
    persist = "continue"
    while persist.lower() != "done":
        name = input("What is the guest's name? ")
        name = name.capitalize()
        
        arrival_day = int(input("Which day will this person arrive? Please enter any number 1 - {nights}: ".format(nights=nights)))
        while arrival_day > int(nights) or arrival_day <= 0:
            arrival_day = int(input("Your number doesn't fit the paramaters--any number from 1 - {nights}. Please indicate which day this person will arrive: ".format(nights=nights)))
       
        departure_day = int(input("Which day will this person depart? Please enter any number {arrival} - {nights}: ".format(arrival=arrival_day, nights=nights)))
        while departure_day <= arrival_day or arrival_day > nights:
            departure_day = int(input("Your number doesn't fit the paramaters--any number from {arrival} - {nights}. Please indicate which day this person will arrive: ".format(arrival=arrival_day, nights=nights)))
        
        guests.update({name:[*range(arrival_day,departure_day+1)]})
        persist = input("Type 'done' if you are finished adding guests or enter/return if you have more to add: ")
    return guests

test = guest_info(5)
print(test)