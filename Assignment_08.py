# -*- coding: utf-8 -*-
"""
Created on Sun May  4 02:10:10 2025

@author: Asadaduzzaman
"""
'''
For Assignment 8, I am using the car_crashes dataset, which provides detailed statistics
on motor vehicle crashes and related insurance data across all 50 U.S. states.

This dataset includes several key variables:
total: Total number of fatal car crashes per 100,000 people
speeding: Fatal crashes involving speeding
alcohol: Fatal crashes involving alcohol
not_distracted: Crashes not involving distracted driving
no_previous: Drivers with no previous accidents
ins_premium: Average annual car insurance premium (USD)
ins_losses: Insurance losses incurred per insured driver (USD)
abbrev: State abbreviation
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the data file and create dataframe
data = pd.read_csv('car_crashes.csv')
 
df = pd.DataFrame(data)



# Display first 5 rows(head)
print(df.head())

# Summary statistics: count, mean, std, min, 25%, 50%, 75%, max
df.describe()

# Median values of each column
df.median(numeric_only=True)


# Quartiles can be found via quantile function
df.quantile([0.25, 0.5, 0.75], numeric_only=True)

# Check how many missing values
df.isnull().sum()

plt.figure(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()


# Check missing values
print("Missing values before:")
print(df.isnull().sum())

# Drop rows with any missing data
df = df.dropna()

# Confirm removal
print("Missing values after:")
print(df.isnull().sum())

 


# Group by state abbreviation and calculate mean of all numeric columns
grouped_by_state = df.groupby("abbrev").mean(numeric_only=True)
print(grouped_by_state.head())
 

# Display grouped data
 

# rename the column name
df.rename(columns={
    "abbrev": "state",
    "ins_premium": "insurance_premium",
    "ins_losses": "insurance_losses"
}, inplace=True)

# Check dtypes
df.dtypes

#reset the index.
df.reset_index(drop=True, inplace=True)


'''
I will use the following properties for the plot.
title and axis labels
line color and width
Legend position and font size
Annotations for extreme values
tick label rotation
'''

#plot1-line plot
# Customize title and labels
# Sort by insurance_premium
# Tick formatting
# Legend formatting
# Annotation
df_sorted = df.sort_values('insurance_premium')
plt.figure(figsize=(12, 6))
plt.plot(df_sorted['state'], df_sorted['total'], label='Total Accidents', color='teal', linewidth=2.5)
plt.plot(df_sorted['state'], df_sorted['insurance_premium'], label='Insurance Premium', color='orange', linewidth=2)
plt.title("Total Accidents vs. Insurance Premium by State", fontsize=16)
plt.xlabel("State", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.xticks(rotation=45, fontsize=9)
plt.yticks(fontsize=10)
plt.legend(loc='upper left', fontsize='medium')
max_acc_idx = df_sorted['total'].idxmax()
plt.annotate('Highest Accident Rate',
             xy=(df_sorted.loc[max_acc_idx, 'state'], df_sorted.loc[max_acc_idx, 'total']),
             xytext=(df_sorted.loc[max_acc_idx, 'state'], df_sorted.loc[max_acc_idx, 'total'] + 3),
             arrowprops=dict(arrowstyle="->", color='red'),
             fontsize=10)

plt.tight_layout()
plt.show()

#Plot2-scatter plot
'''
I have used:
marker style, color, and size.
Title and axis customization.
Annotations for outliers.
Legend outside the plot.
Axis label font size change.
'''
# Scatter plot
# Titles and labels
# Custom ticks
# Place legend outside
# Annotate highest loss

plt.figure(figsize=(10, 6))
plt.scatter(df['insurance_premium'], df['insurance_losses'], c='green', s=100, alpha=0.6, label='State')
plt.title("Insurance Premium vs. Insurance Losses", fontsize=16)
plt.xlabel("Insurance Premium ($)", fontsize=12)
plt.ylabel("Insurance Losses ($)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')
max_loss_idx = df['insurance_losses'].idxmax()
plt.annotate(df.loc[max_loss_idx, 'state'],
             (df.loc[max_loss_idx, 'insurance_premium'], df.loc[max_loss_idx, 'insurance_losses']),
             textcoords="offset points", xytext=(0,10),
             ha='center', fontsize=9, color='darkblue')

plt.tight_layout()
plt.show()

'''
Part 2:
Recreate the visualizations above using the Seaborn library as best as possible.
You are required to explain what each of your plots is representing. 
Plots without comments will not be accepted. In addition, please explain the properties you are showcasing.

This plot represents the distribution of the insurance premiums across all states.
I will use a boxplot to show the minimum, first quartile (Q1), median (Q2), third quartile (Q3), 
and maximum values for each state.
'''
#plot1
# Create a Seaborn boxplot
# Add title and labels
# Rotate the x-axis labels for better readability
# Show the plot
# Set the style of the plot

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.boxplot(x="state", y="insurance_premium", data=df, palette="muted")
plt.title("Distribution of Insurance Premium by State", fontsize=16)
plt.xlabel("State", fontsize=12)
plt.ylabel("Insurance Premium ($)", fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

'''
This plot represents the relationship between insurance premium and insurance losses across different states.
I will create Scatterplot to show relationships between two continuous variables.
This annotations to highlight specific points highest insurance loss.
Styling with colors, labels, and title.
'''
#plot2
# Create scatter plot with Seaborn
# Add title and labels
# Highlight the state with the highest insurance loss
# Annotate the state with the highest insurance loss
# Set the figure size

plt.figure(figsize=(10, 6)) 
sns.scatterplot(x="insurance_premium", y="insurance_losses", data=df, 
                hue="state", palette="Set2", s=100, edgecolor="black")
plt.title("Insurance Premium vs. Insurance Losses", fontsize=16)
plt.xlabel("Insurance Premium ($)", fontsize=12)
plt.ylabel("Insurance Losses ($)", fontsize=12)
max_loss_idx = df['insurance_losses'].idxmax()
max_state = df.loc[max_loss_idx, 'state']
max_premium = df.loc[max_loss_idx, 'insurance_premium']
max_loss = df.loc[max_loss_idx, 'insurance_losses']
plt.annotate(f'Highest Loss: {max_state}',
             xy=(max_premium, max_loss),
             xytext=(max_premium + 50, max_loss + 5),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=10, color='darkred')

# Show the plot
plt.tight_layout()
plt.show()

#Part 3:
'''
Matplotlib offers complete control and flexibility but requires more lines of code for customization. 
It is a powerful tool for creating custom, 
complex plots, but it requires more code and effort to achieve aesthetic plots.
'''
'''
Seaborn is built on top of the high-level interface Matplotlib, which makes it easy to create complex plots using fewer lines of code. 
It automatically handles many aspects such as color palettes, axis labels, and legends, which can be tedious in Matplotlib. 
It is ideal for statistical plots such as boxplots, pair plots, heatmaps, and regression plots.
Seaborn simplifies the process of creating statistical plots and comes with built-in aesthetics
which makes it ideal for quickly visualizing data in a clean, attractive way.
'''
#Conclusions

'''
In this dataset reveals that there is no clear linear relationship between average insurance 
premiums and insurance losses across states in the United States. Some states with higher premiums
do not necessarily experience higher losses, suggesting that other influences, such as traffic safety laws, 
population density, or local accident trends, may play a more important role in determining insurance costs. 
In addition, speeding and alcohol-related incidents appear to be major contributors to total traffic fatalities in many states, 
with states such as South Carolina and Montana showing particularly high numbers in these areas. 
There is considerable variation in both insurance and mortality statistics across states. 
For example, Massachusetts and the District of Columbia report low mortality rates but relatively high insurance premiums,
likely due to urban congestion and associated risks. Interestingly, states with higher average mortality rates do not always have the highest premiums,
suggesting that broader economic, legal, or demographic factors may have a stronger impact on insurance pricing than mortality alone.
Overall, the dataset provides valuable insights into how driving behavior and regional 
characteristics affect both nationwide traffic fatalities and insurance-related metrics.
'''