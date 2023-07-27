# Module 3 Assignment
# Question 4
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as sms

# Create the DataFrame
df = pd.read_csv("nbaallelo_slr.csv")

# Subset the data
nba = df[['pts', 'opp_pts', 'elo_i']]

# Define the response variable
response = nba['pts']

# Create an analysis of variance table
aov_table = sms.ols('response ~ elo_i + opp_pts', nba).fit()

# Print the analysis of variance table
print(sm.stats.anova_lm(aov_table, typ=2), '\n')