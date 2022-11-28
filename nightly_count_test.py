def nightly_count(guests, nights):
    people_per_night = {}
    for i in range(1, nights+1):
        counter = 0
        for j in guests.values():
            if i in j:
                counter += 1
        people_per_night[i] = counter
    return people_per_night

people_per_night = nightly_count({"Seth":[2, 3, 4, 5], "Hailey":[1,2,3,4,5], "Nano":[3,4,5]}, 5)
print(people_per_night)