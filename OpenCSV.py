import csv
import requests
import plotly.graph_objects as gp
import plotly.express as px
import pandas as pi
import numpy as np

all_data = {'United States': 840, 'China': 156, 'United Kingdom': 826, 'India': 356, 'Russia': 643}
year = list(range(1950, 2021, 10))

# Creating instance of the figure
fig = gp.FigureWidget()
graph_data = []
count = 0
for x in year:
    for country in all_data:
        print(country + " " + str(x))
        url = "https://www.populationpyramid.net/api/pp/" + str(all_data[country]) + "/" + str(x) + "/?csv=true"
        # Send HTTP GET request via requests
        data = requests.get(url)
        # Convert to iterator by splitting on \n chars
        lines = data.text.splitlines()
        # Parse as CSV object
        reader = csv.reader(lines)
        y_age, x_M, x_F = [], [], []
        # View Result
        for row in reader:
            if row[1] != "M" and row[2] != "F":
                row[1] = int(row[1])
                row[2] = int(row[2])
                row.append(x)

                y_age.append(row[0])
                x_M.append(int(row[1]))
                x_F.append(int(row[2]) * -1)
        graph_data.append([y_age, x_M, x_F, x])

print("Would you like to begin the program? (y/n)")
response = input().lower()
while response == "y":
    print("Enter a country: ")
    country = input().title()
    print("Enter a year: ")
    year_selected = int(input())
    year_index = year.index(year_selected)

    print(year_index)
    # Adding Male data to the figure
    if count == 0:
        fig.add_trace(gp.Bar(y=graph_data[year_index][0], x=graph_data[year_index][1],
                             name='Male',
                             orientation='h'))

        # Adding Female data to the figure
        fig.add_trace(gp.Bar(y=graph_data[year_index][0], x=graph_data[year_index][2],
                             name='Female', orientation='h'))
        graph_title = 'Population Pyramid of ' + country + ' - ' + str(year_selected)
    else:
        fig = gp.FigureWidget()
        fig.add_trace(gp.Bar(y=graph_data[year_index][0], x=graph_data[year_index][1],
                             name='Male',
                             orientation='h'))

        # Adding Female data to the figure
        fig.add_trace(gp.Bar(y=graph_data[year_index][0], x=graph_data[year_index][2],
                             name='Female', orientation='h'))
        graph_title = 'Population Pyramid of ' + country + ' - ' + str(year_selected)
    fig.update_layout(title=graph_title,
                      title_font_size=22, barmode='relative',
                      bargap=0.0, bargroupgap=0,
                      xaxis=dict(tickvals=[-60000000, -40000000, -20000000,
                                           0, 20000000, 40000000, 60000000],
                                 ticktext=['6M', '4M', '2M', '0',
                                           '2M', '4M', '6M'],
                                 title='Population in Millions',
                                 title_font_size=14)
                      )
    fig.show()
    # Updating the layout for our graph

    count += 1
    print("Would you like to continue?(y/n)")
    response = input().lower()

