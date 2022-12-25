import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import pandas as pd
import csv


"""csv files to dictionary"""
e = open('./asset/annual-co2-emissions-per-country.csv', 'r')
co2_data = csv.DictReader(e)

g = open('./asset/temperature-anomaly.csv', 'r')
temperature_data = csv.DictReader(g)


"""Make Year and Annual CO2 emissions List"""
years1 = list(range(1750, 2022))
co2 = [0]*len(years1)

for row in co2_data:
    co2[int(row.get('Year'))-years1[0]] += float(row.get('Annual CO2 emissions', 0))


"""Make Year and Annual Make Gobal Temperature List List"""
years2 = list(range(1850, 2020))
temperature = [0]*len(years2)

for row in temperature_data:
    temperature[int(row.get('Year'))-years2[0]] += float(row.get('Median temperature anomaly from 1961-1990 average', 0))


"""Plot"""
fig = plt.figure(figsize=(6,6))
fig.set_facecolor('white')
ax1 = fig.add_subplot()
 
"""co2 emissions plot - blue"""
color1 = 'b'
ax1.plot(years1, co2, color=color1)
ax1.set_xlabel('Year')
ax1.set_ylabel('Annual CO2 emissions (billion t)', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

"""global temperuature plot - red"""
color2 = 'r'
ax2 = ax1.twinx()
ax2.plot(years2, temperature, color=color2)
ax2.set_ylabel('Global Temperature', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%i ℃'))
plt.show()