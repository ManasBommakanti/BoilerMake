import csv
import requests
import plotly.graph_objects as gp
import plotly.express as px
import pandas as pi
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def stage_classifier(summary):
    total_pop = 0
    summary_prop = [0, 0, 0, 0, 0]
    for i in summary:
        total_pop += i
    for i in range(len(summary)):
        summary_prop[i] = summary[i] / total_pop
    slopes = [0, 0, 0, 0]
    for i in range(len(slopes)):
        slopes[i] = summary_prop[i + 1] - summary_prop[i]
    slope_of_slopes = [0, 0, 0]
    for j in range(len(slope_of_slopes)):
        slope_of_slopes[j] = slopes[j + 1] - slopes[j]

    threshold = 0.075
    if summary_prop[0] >= .5:
        return 1
    if abs(slope_of_slopes[0]) < threshold:
        if abs(slope_of_slopes[1]) < threshold:
            if abs(slope_of_slopes[2]) < threshold:
                return 2
    for i in slope_of_slopes:
        if i - threshold > 0:
            return 3
    return 4

def stage(graph_data_dict):
    five_num_summary = [0, 0, 0, 0, 0]
    males = graph_data_dict["Male"]
    females = graph_data_dict["Female"]

    for i in range(len(males)):
        sum = males[i] + females[i]
        if 0 <= i <= 3:
            five_num_summary[0] += sum
        elif 4 <= i <= 7:
            five_num_summary[1] += sum
        elif 8 <= i <= 11:
            five_num_summary[2] += sum
        elif 12 <= i <= 15:
            five_num_summary[3] += sum
        else:
            five_num_summary[4] += sum

    return stage_classifier(five_num_summary)


# all_data = {'United States': 840, 'China': 156, 'United Kingdom': 826, 'India': 356, 'Russia': 643}
# countries = ["United States", "China", "United Kingdom", "India", "Russia"]
# year = list(range(1950, 2021, 10))

# Creating instance of the figure
# fig = gp.FigureWidget()
# graph_data = []
# for x in year:
#     for country in all_data:
#         url = "https://www.populationpyramid.net/api/pp/" + str(all_data[country]) + "/" + str(x) + "/?csv=true"
#         # Send HTTP GET request via requests
#         data = requests.get(url)
#         # Convert to iterator by splitting on \n chars
#         lines = data.text.splitlines()
#         # Parse as CSV object
#         reader = csv.reader(lines)
#         y_age, x_M, x_F = [], [], []
#         # View Result
#         for row in reader:
#             if row[1] != "M" and row[2] != "F":
#                 row[1] = int(row[1])
#                 row[2] = int(row[2])
#                 row.append(x)
#
#                 y_age.append(row[0])
#                 x_M.append(int(row[1]))
#                 x_F.append(int(row[2]) * -1)
#         graph_data.append([y_age, x_M, x_F, x, country])
#
# print("Would you like to begin the program? (y/n)")
# response = input().lower()
#
# while response == "y":
#     print("Enter a country: ")
#     country = input().title()
#     print("Enter a year: ")
#     year_selected = int(input())
#     country_index = countries.index(country)
#     year_index = year.index(year_selected)
#
#     # Adding Male data to the figure
#
#     five_num_summary = [0, 0, 0, 0, 0]
#     for i in range(len(graph_data[year_index * 5 + country_index][0])):
#         sum = graph_data[year_index * 5 + country_index][1][i] - graph_data[year_index * 5 + country_index][2][i]
#         if 0 <= i <= 3:
#             five_num_summary[0] += sum
#         elif 4 <= i <= 7:
#             five_num_summary[1] += sum
#         elif 8 <= i <= 11:
#             five_num_summary[2] += sum
#         elif 12 <= i <= 15:
#             five_num_summary[3] += sum
#         else:
#             five_num_summary[4] += sum
#     print(stage_classifier(five_num_summary))
#     # Updating the layout for our graph
#
#     print("Would you like to continue?(y/n)")
#     response = input().lower()
