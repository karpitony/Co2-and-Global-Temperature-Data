import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import pandas as pd
import csv


"""csv files to dictionary"""
g = open('./asset/temperature-anomaly.csv', 'r')
temperature_data = csv.DictReader(g)

"""Make Year and Annual Make Gobal Temperature List List"""
years2 = list(range(1850, 2020))
temperature = [0]*len(years2)

for row in temperature_data:
    temperature[int(row.get('Year'))-years2[0]] += float(row.get('Median temperature anomaly from 1961-1990 average', 0))

"""Plot"""
fig = plt.figure(figsize=(6,6))
fig.set_facecolor('white')
ax2 = fig.add_subplot()

"""global temperuature plot - red"""
color2 = 'r'
ax2.plot(years2, temperature, color=color2)
ax2.set_ylabel('Global Temperature', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%i ℃'))
plt.show()