import csv
import webbrowser
import requests

# Google Maps API Key
API_KEY = "YOUR_API_KEY_HERE"

# Start time for the route (7 AM)
start_time = "7:00"

# Time between stops (15 minutes)
stop_time = 15

# Load addresses from CSV file
addresses = []
with open("addresses.csv", "r") as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    for row in reader:
        # Extract the customer name and address
        customer = row[0]
        address = row[1]
        addresses.append(address)

# Create a list of waypoints for the Google Maps API
waypoints = "|".join(addresses)

# Request route from Google Maps API
url = f"https://maps.googleapis.com/maps/api/directions/json?origin={addresses[0]}&destination={addresses[-1]}&waypoints=optimize:true|{waypoints}&departure_time={start_time}&traffic_model=best_guess&key={API_KEY}"
response = requests.get(url)
data = response.json()

# Extract the optimized order of addresses
order = [addresses[0]]
for step in data["routes"][0]["legs"]:
    order.append(step["end_address"])

# Open the optimized route in Safari on a Mac computer
map_url = f"https://www.google.com/maps/dir/?api=1&origin={addresses[0]}&destination={addresses[-1]}&waypoints={waypoints}&departure_time={start_time}&traffic_model=best_guess&key={API_KEY}"
webbrowser.open(map_url, new=2, autoraise=True)
