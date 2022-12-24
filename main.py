import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import pandas as pd
import csv


"""csv files to dictionary"""
def read_csv() -> dict:
    e = open('./asset/annual-co2-emissions-per-country.csv', 'r')
    csv_to_dicttionary = csv.DictReader(e)
    
    return csv_to_dicttionary


"""Make Year and Annual CO2 emissions List"""
years = list(range(1750, 2022))
co2 = [0]*len(years)


for g in range(0,272,1):
    data = read_csv()
    for row in data:
        if int(row.get('Year', 0)) == years[g]:
            co2[g] += float(row.get('Annual CO2 emissions', 0))


"""Plot"""
plt.xlabel('Year')
plt.ylabel('Annual CO2 emissions(billion t)')
plt.plot(years, co2)
plt.show()