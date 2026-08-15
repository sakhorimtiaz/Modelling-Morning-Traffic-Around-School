# After chnaging the names CNG to AutoRickshaw we had two rows having same vehicle name but different values.
# We need to combine them.

import pandas as pd

# Load your organized file
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency_cleaned_organized.csv', encoding='utf-8')

# Sum of TOTAL_PCU for duplicate vehicles
# This groups by Node, TimeSlot, and Vehicle, combining rows 0 & 1, 9 & 10, etc.
df_combined = df.groupby(
    ['Node', 'TimeSlot', 'VehicleType', 'Vehicle']
)['Total_PCU'].sum().reset_index()

# Keep it perfectly stored hierarchially
df_combined = df_combined.sort_values(by=['Node', 'TimeSlot', 'VehicleType', 'Vehicle'])

# Verify
#print(df_combined.head(15).to_string(index=False))

# Save to your computer as a fresh file
df_combined.to_csv(r'C:\Users\THINKPAD\Downloads\frequency_pcu_combined.csv', index=False, encoding='utf-8')
