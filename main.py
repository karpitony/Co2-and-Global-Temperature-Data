import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import pandas as pd
import csv


"""csv files to dictionary"""
e = open('./asset/annual-co2-emissions-per-country.csv', 'r')
data = csv.DictReader(e)


"""Make Year and Annual CO2 emissions List"""
years = list(range(1750, 2022))
co2 = [0]*len(years)


for row in data:
    co2[int(row.get('Year'))-years[0]] += float(row.get('Annual CO2 emissions', 0))


"""Plot"""
plt.xlabel('Year')
plt.ylabel('Annual CO2 emissions(billion t)')
plt.plot(years, co2)
plt.show()