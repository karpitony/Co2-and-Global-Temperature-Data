import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import pandas as pd
import csv


"""csv files to dictionary"""
e = open('./asset/annual-co2-emissions-per-country.csv', 'r')
data = csv.DictReader(e)


"""Make Year and Annual CO2 emissions List"""
years1 = list(range(1750, 2022))
co2 = [0]*len(years1)


for row in data:
    co2[int(row.get('Year'))-years1[0]] += float(row.get('Annual CO2 Emissions', 0))


"""Plot"""
fig = plt.figure(figsize=(6,6))
fig.set_facecolor('white')
ax1 = fig.add_subplot()
 
"""co2 emissions plot - blue"""
color1 = 'b'
ax1.plot(years1, co2, color=color1)
ax1.set_xlabel('Year')
ax1.set_ylabel('Annual CO2 Emissions (billion t)', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

plt.show()