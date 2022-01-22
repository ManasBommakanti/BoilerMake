import csv
import requests
import plotly.graph_objects as gp

all_data = {'United States': 840, 'China': 156, 'United Kingdom': 826, 'India': 356, 'Russia': 643}
year = list(range(1950, 2021, 10))

# Define the remote URL
country = input().title()

# Creating instance of the figure
fig = gp.Figure()

for x in year:
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
            # print(row)

            y_age.append(row[0])
            x_M.append(int(row[1]))
            # print("M", x_M)
            x_F.append(int(row[2]) * -1)
            # print("F", x_F)

# Adding Male data to the figure
fig.add_trace(gp.Bar(y=y_age, x=x_M,
                     name='Male',
                     orientation='h'))

# Adding Female data to the figure
fig.add_trace(gp.Bar(y=y_age, x=x_F,
                     name='Female', orientation='h'))

# Updating the layout for our graph
graph_title = 'Population Pyramid of ' + country + '-2019'
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