# Module 3 Assignment
# Question 1
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm

# Create the DataFrame
nba = pd.read_csv("nbaallelo_slr.csv")

# Create a new column
nba['y']= nba['pts'] - nba['opp_pts']

# Subset the data
nba_stats = nba[['y', 'elo_i']]

# Fit the OLS model
results = ols('y ~ elo_i', data = nba_stats).fit()

# Create an analysis of variance table
aov_table = sm.stats.anova_lm(results, typ=2)

# Print the analysis of variance table
print(aov_table, '\n')