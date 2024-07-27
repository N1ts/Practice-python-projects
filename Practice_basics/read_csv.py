import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city name:")

for row in data[1:]:
    # here row[0] belongs to 1st column means city, so it will start search one by one through out the rows
    if city == row[0]:
        # here row[1] belongs to 2nd column where all the temperatues will be show, and it will print the matched city's temp.
        print(row[1])