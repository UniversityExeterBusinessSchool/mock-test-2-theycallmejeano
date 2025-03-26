#######################################################################################################################################################
# 
# Name:
# SID:
# Exam Date:
# Module:
# Github link for this assignment:  
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################
# %%
# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]
average_sales = sum(weekly_sales)/len(weekly_sales)

for sale in weekly_sales:
    if sale > average_sales:
        print('Sale of', sale, 'above average sale of ', average_sales)
    elif sale < average_sales:
        print('Sale of', sale, 'below average sale of ', average_sales)

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

# NOTE -> median
# get the sorted list
sorted_list = sorted(weekly_sales.copy())
len_sorted = len(sorted_list)
median_sales = sorted_list[len_sorted//2]
print(median_sales)

print('---Median sales---', median_sales)
for sale in weekly_sales:
    if sale > average_sales:
        print('Sale of', sale, 'above median sale of ', median_sales)
    elif sale < median_sales:
        print('Sale of', sale, 'below median sale of ', median_sales)


# NOTE: get first sale thats above median
for sale in weekly_sales:
    while True:
        if sale > median_sales:
            print('First sale above median', sale)
        break

#######################################################################################################################################################
# %%
# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.
# Find the positions of 'good'
good_start = customer_feedback.find("good")
good_end = good_start + len("good")

# Find the positions of 'improved'
improved_start = customer_feedback.find("improved")
improved_end = improved_start + len("improved")

# Store positions in a list of tuples
positions = [(good_start, good_end), (improved_start, improved_end)]

# Print the result
print(positions)
#######################################################################################################################################################
# %%
# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
def get_npm(net_profit, rev):

    npm = (net_profit/rev) * 100

    return npm

print('---demo npm', get_npm(500, 1000))

# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.

#######################################################################################################################################################
# %%
# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 
              'Sales': [200, 220, 210, 240, 250]}

df = pd.DataFrame(sales_data)
df['Cumulative Sales'] = df['Sales'].cumsum()

for _, row in df.iterrows():
    print(row['Month'], row['Cumulative Sales']) 

#######################################################################################################################################################
# %%
# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130
prices = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1, 1)
demand =  np.array([200, 180, 170, 160, 150, 140, 130])

model = LinearRegression()
model.fit(prices, demand)

predicted_demand = model.predict(np.array([[26]]))

price_range = np.linspace(15, 30, 100).reshape(-1, 1)
demand_predictions = model.predict(price_range)

# Plot scatter and regression line
plt.scatter(prices, demand, color='blue', label='Actual Data')
plt.plot(price_range, demand_predictions, color='red', label='Regression Line')
plt.scatter([26], predicted_demand, color='green', marker='x', s=100, label=f'Predicted Demand ({predicted_demand[0]:.2f})')
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.title("Price vs Demand Linear Regression")
plt.legend()
plt.grid()
plt.show()

# %%
### Using seaborn
import seaborn as sns

df_prices = pd.DataFrame(
    {
        'prices': [15, 18, 20, 22, 25, 27, 30],
        'demand': [200, 180, 170, 160, 150, 140, 130]
    }
)
model = LinearRegression()
model.fit(df_prices[['prices']], df_prices[['demand']])

# predicted
predicted_demand = model.predict(np.array([[26]]))

# 
# sns.regplot(data = df_prices, x='prices', y='demand')

sns.scatterplot(data=df_prices, x='prices', y='demand', color='blue', label='Actual Data')

# Regression Line
# sns.lineplot(data=df_line, x='Price', y='Demand', color='red', label='Regression Line')

# Predicted demand at £26
sns.scatterplot(x=[26], y=[predicted_demand[0]], color='green', marker='X', s=100, label=f'Predicted Demand ({predicted_demand[0]:.2f})')

# Labels and Title
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.title("Price vs Demand Linear Regression")
plt.legend()
plt.grid()
plt.show()

# %%
# NOTE predicted sales for previous question
sales_model = LinearRegression()
sales_model.fit(df[['Month']], df[['Sales']])
#######################################################################################################################################################
# %%
# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# def get_valid_prices(price_dict):
#     valid_prices = []
#     for _, val in price_dict.items():
#         if isinstance(val, float) or isinstance(val, int):
#             valid_prices.append(val)
#         else:
#             print(val, 'not a numeric value, skipping')

#     return sum(valid_prices)


def get_valid_prices(price_dict):
    valid_prices = []
    for _, val in price_dict.items():
        try:
            if isinstance(val, float) or isinstance(val, int):
                valid_prices.append(val)
        except:
            print(val, 'not a numeric value, skipping')

    return sum(valid_prices)

def get_valid_prices(prices_dict):
    total = 0  # Initialize total price
    
    for item, price in prices_dict.items():
        try:
            total += float(price)  # Convert to float in case it's a string number
        except ValueError:
            print(f"Warning: Skipping non-numeric value for item '{item}' ({price})")
    
    return total

print(get_valid_prices(prices))

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

#######################################################################################################################################################
# %%
# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random

#######################################################################################################################################################
# %%
# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.
new_list = []

for elem in quantities:
    if elem > 10:
        new_list.append(elem*2)

print('Old list',quantities)
print('New list',new_list)


#######################################################################################################################################################
# %%
# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 
           'product_B': 5, 
           'product_C': 3, 'product_D': 2, 'product_E': 5}

#######################################################################################################################################################
# %%
# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = total / len(values)
# print("The average is" + average)
print("The average is", average)

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

#######################################################################################################################################################

# %%
