import csv
import requests

all_data = {'USA': 840, 'China': 156, 'United Kingdom': 826, 'India': 356, 'Russia': 643}
year = list(range(1950, 2021, 10))

# Define the remote URL
country = input()

for x in year:
    url = "https://www.populationpyramid.net/api/pp/" + str(all_data[country]) + "/" + str(x) + "/?csv=true"
    # Send HTTP GET request via requests
    data = requests.get(url)
    # Convert to iterator by splitting on \n chars
    lines = data.text.splitlines()
    # Parse as CSV object
    reader = csv.reader(lines)


    # View Result
    for row in reader:
        if row[1] != "M":
            row[1] = int(row[1])

        if row[2] != "F":
            row[2] = int(row[2])


        print(row)