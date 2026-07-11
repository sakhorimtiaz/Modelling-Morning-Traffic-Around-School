# we need to organize data and create a new CSV file

import pandas as pd

# 1. Load the files
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency_cleaned.csv', encoding='utf-8')
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\velocity_cleaned.csv', encoding='utf-8')

df_organized = df.sort_values(by=['Node', 'TimeSlot', 'VehicleType', 'Vehicle'])
df_organized = df_organized[['Node', 'TimeSlot', 'VehicleType', 'Vehicle','Total_PCU']]

df_organized.to_csv(r'C:\Users\THINKPAD\Downloads\frequency_cleaned_organized.csv', index=False, encoding='utf-8')

