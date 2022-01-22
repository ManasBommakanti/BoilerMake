import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#create dataframe
df = pd.DataFrame({'Age': ['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90+'],
                    'Male': [9000, 14000, 22000, 26000, 34000, 32000, 29000, 22000, 14000, 3000],
                    'Female': [8000, 15000, 19000, 28000, 35000, 34000, 28000, 24000, 17000, 5000]})
#view dataframe

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
