# Module 3 Assignment
# Question 3
# Author: Ralph Godkin

# IMPORTS
import pandas as pd

# Create the DataFrame
nba = pd.read_csv("nbaallelo_slr.csv")

# Create a new column
nba['y']= nba['pts'] - nba['opp_pts']

# Subset the data 1
nba_stats_1 = nba[['elo_i', 'pts', 'opp_pts']]

# Calculate and display 3 way correlation
correlation_3x_matrix = nba_stats_1.corr()
print(correlation_3x_matrix, '\n')

# Subset the data 2
nba_stats_2 = nba[['elo_i','y']]

# Calculate and display 2 way correlation
correlation_2x_matrix = nba_stats_2.corr()
print(correlation_2x_matrix, '\n')