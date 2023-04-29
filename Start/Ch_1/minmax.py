# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# The min() function finds the minimum value
print(f"The minimum value is: {min(values)}")
print(f"The minimum value is: {min(strings)}")

# The max() function finds the maximum value
print(f"The maximum value is: {max(values)}")
print(f"The maximum value is: {max(strings)}")

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data['metadata']['title'])
print(len(data['features']))

# custom function to get magnitude value


def get_magnitude(data_item):
    magnitude = data_item['properties']['mag']
    if magnitude is None:
        magnitude = 0
    return float(magnitude)


print(f"The minimum value is: {min(data['features'], key=get_magnitude)}")
print(f"The maximum value is: {max(data['features'], key=get_magnitude)}")
