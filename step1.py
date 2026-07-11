# we have two files. At first we will cross check the vehicle names. 
# We also need to check the PCU

import pandas as pd

# 1. Load the files
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency.csv', encoding='utf-8')
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\velocity.csv', encoding='utf-8')
freq_vehicles = set(df['Vehicle'].dropna().unique())
vel_vehicles = set(dv['Vehicle_Type'].dropna().unique())  # Updated to 'Vehicle'

print("Frequency Vehicles:", freq_vehicles)
print("Velocity Vehicles:", vel_vehicles)

#we will see that there are some mismatches in the variable names.
