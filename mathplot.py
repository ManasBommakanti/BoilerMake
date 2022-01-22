import numpy as np
import csv
import requests
import pandas as pd

import datapane as dp
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import interact, interactive, fixed, interact_manual

all_data = {'United States': 840, 'China': 156, 'United Kingdom': 826, 'India': 356, 'Russia': 643}



country = input("Enter country: ")
year = int(input("Enter decade between 1950 and 2020: "))




# @widgets.interact( x = ["United States", "India", "Russia", "China", "United Kingdom"], y = ["1950", "1960", "1970", "1980", "1990", "2000", "2010", "2020"])


def f(x, y):

    # print(x + " " + str(y))
    url = "https://www.populationpyramid.net/api/pp/" + str(all_data[x]) + "/" + str(y) + "/?csv=true"
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
            row.append(str(y))

            y_age.append(row[0])
            x_M.append(int(row[1]))
            x_F.append(int(row[2]) * 1)
    graph_data = {'Age': y_age, "Male": x_M, "Female": x_F, "Year": str(y)}

    print(graph_data)

    # create dataframe
    # df = pd.DataFrame({'Age': ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+'],
    #                    'Male': [9000, 14000, 22000, 26000, 34000, 32000, 29000, 22000, 14000, 3000],
    #                    'Female': [8000, 15000, 19000, 28000, 35000, 34000, 28000, 24000, 17000, 5000]})



    df = pd.DataFrame(graph_data)



    # view dataframe
    y = range(0, len(df))
    x_male = df['Male']
    x_female = df['Female']

    # define plot parameters
    fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))

    # specify background color and plot title
    fig.patch.set_facecolor('xkcd:light grey')
    plt.figtext(.5, .9, "Population Pyramid ", fontsize=15, ha='center')

    # define male and female bars
    axes[0].barh(y, x_male, align='center', color='royalblue')
    axes[0].set(title='Males')
    axes[1].barh(y, x_female, align='center', color='lightpink')
    axes[1].set(title='Females')

    # adjust grid parameters and specify labels for y-axis
    axes[1].grid()
    axes[0].set(yticks=y, yticklabels=df['Age'])
    axes[0].invert_xaxis()
    axes[0].grid()

    # display plot
    plt.show()


f(country, year)