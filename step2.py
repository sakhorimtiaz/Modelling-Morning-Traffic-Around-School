#now we will create two cleaned files 
#CNG and AutoRickshaw have almost same PCU, 
import pandas as pd

# Load the files
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency.csv', encoding='utf-8')
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\velocity.csv', encoding='utf-8')

# Rename 'Vehicle_Type' to 'Vehicle' to match the frequency file column name
dv = dv.rename(columns={'Vehicle_Type': 'Vehicle','Time_slot':'TimeSlot','Speed (kmph)':'Speed'})

# Standardize 'Rickshaw' to 'ManualRickshaw' in velocity data (now using 'Vehicle')
# Treat CNG and AutoRickshaw as the exact same vehicle mode

dv['Vehicle'] = dv['Vehicle'].replace({'Rickshaw': 'ManualRickshaw',
                                       'CNG': 'AutoRickshaw',
                                       'Scooter':'MotorBike',
                                       'Pickup': 'Leguna'})
df['Vehicle'] = df['Vehicle'].replace({'CNG': 'AutoRickshaw'})

# Standardize 'Afternoon' to 'Evening' in velocity data to match frequency file
dv['TimeSlot'] = dv['TimeSlot'].replace({'Afternoon': 'Evening'})

# calculate the total PCU by using formula
df['Total_PCU'] = df['Frequency'] * df['PCU']

df_organized = df.sort_values(by=['Node', 'TimeSlot', 'VehicleType', 'Vehicle'])
df_organized = df_organized[['Node', 'TimeSlot', 'VehicleType', 'Vehicle', 'Frequency', 'PCU','Total_PCU']]

dv_organized = dv.sort_values(by=['Node', 'TimeSlot', 'Vehicle'])
dv_organized = dv_organized[['Node', 'TimeSlot', 'Vehicle', 'Speed']]

# Let's verify the alignment
"""freq_vehicles = set(df['Vehicle'].dropna().unique())
vel_vehicles = set(dv['Vehicle'].dropna().unique())  # Updated to 'Vehicle'

print("Frequency Vehicles:", freq_vehicles)
print("Velocity Vehicles (Updated):", vel_vehicles)
"""
# Save the corrected version to your PC
df_organized.to_csv(r'C:\Users\THINKPAD\Downloads\frequency_cleaned.csv', index=False, encoding='utf-8')
dv_organized.to_csv(r'C:\Users\THINKPAD\Downloads\velocity_cleaned.csv', index=False, encoding='utf-8')
