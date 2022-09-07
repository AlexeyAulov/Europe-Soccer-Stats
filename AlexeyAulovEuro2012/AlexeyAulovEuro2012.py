# -*- coding: utf-8 -*-
"""
 Good, Load data from the csv file
 Good, Select only the Goal column.
 Good, Show the number of teams in the dataset
 Good, Show only the columns Team, Yellow Cards and Red Cards
 Good, Sort the teams by Red Cards, then by Yellow Cards
 Good, Calculate the mean number of Yellow Cards in the tournament
 Find teams that scored more than 6 goals
 DK,Select the teams whose name start with a G
 Good,Select the first 7 columns
 Good, Select all columns except the last 3
 Present only the Shooting Accuracy from England, Italy and Russia
"""

import pandas as pd
import numpy as np

#Load data from the csv file
EuroStat=pd.read_csv('Euro_2012_stats_TEAM.csv')

print("Print dataframe loaded from CSV")
print(EuroStat)
print("")
#Select only the Goal column.
print("Showing only the goal column")
print(EuroStat['Goals'])
print("")
#Show the number of teams in the dataset
print("The number of Teams")
print(len(EuroStat['Team']))
print("")
#Show only the columns Team,Yellow Cards and Red Cards
print("Showing Columns Team,Yellow Cards and Red Cards")
print(EuroStat[['Team','Yellow Cards','Red Cards']])
print("")
#Sort the teams by Red Cards, Then by Yellow Cards
print("Sorting the teams by Red Cards, then by Yellow Cards")
print("Red Cards")
print(EuroStat.sort_values(by=['Red Cards'], ascending=True))
print("")
print("Yellow Cards")
print(EuroStat.sort_values(by=['Yellow Cards'], ascending=True))

#Calculate the mean number of Yellow Cards in the tournament
print("Calculate the mean value of Yellow Cards in the tournament")
print("Mean: ",EuroStat['Yellow Cards'].mean())
print("")

#Find teams whose teams that scored more than 6 goals
print("Find team whose teams that scored more than 6 goals")
print("Teams with Goals greater than 6", EuroStat['Goals']>6)
print("")

#Select first 7 columns
print("Select First 7 Columns")
print("Printing First 7 Columns",EuroStat.iloc[:,:8])
print("")

#Select all columns except the last 3
print("Selecting all columns except the last 3 ")
print("Printing all columns",EuroStat.iloc[:,:-3])
print("")

#Present only the Shooting Accuracy from England, Italy and Russia
print("Presenting only the shooting accuracy from England,Italy, and Russia")
print("England\n Italy\nRussia\n",EuroStat.iloc[[3,7,12],5:6])
print("")