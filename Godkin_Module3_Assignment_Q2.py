# Module 3 Assignment
# Question 2
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import statsmodels.formula.api as sms


# Create the DataFrame
df = pd.read_csv("internetusage.csv")
internet = df[['internet_usage', 'bachelors_degree']]
# print(internet.head())

# fit a linear model using the sms.ols function and the internet dataframe
model = sms.ols('internet_usage ~ bachelors_degree', data = internet).fit()
# print(model.summary())

# Request the user to enter a value
bach_percent = float(input('\nEnter a percent of the population with bachelor\'s degrees: '))

# Create a new dataframe with the prediction
new = pd.DataFrame({'bachelors_degree' : [bach_percent]})

# Use the model to create a prediction
prediction = model.get_prediction(new, weights=1)
intervalSummary=prediction.summary_frame(alpha=0.1)

# Print the results
print(f'\nIn the USA, if there is an average of {bach_percent}% of the population with a bachelors degree, \none could expect the following percent of the population to use the Internet: ')
print(intervalSummary.iloc[:,0:1], '\n')