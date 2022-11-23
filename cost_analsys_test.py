def nightly_count(nights):
    people_per_night = {}
    x = 1
    for i in range(nights):
        count = int(input("How many people will be staying on night {}? ".format(str(x))))
        people_per_night[x] = count
        x += 1
    return people_per_night

x = nightly_count(5)
print(x)