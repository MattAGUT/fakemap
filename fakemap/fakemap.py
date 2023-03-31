"""Main module."""

import random

# Generate random latitude and longitude coordinates
def Generate_random_location():
    "Generates a Random Latitude and Longitude "
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)

    # Print the coordinates
    print("Latitude: ", lat)
    print("Longitude: ", lon)
