# In the velocity_cleaned.csv file we have two or more speed values of same vehicles.
# We will calculate the average.

import pandas as pd

# Load your cleaned velocity file
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\velocity_cleaned.csv', encoding='utf-8')

# Compute average speed for a vehicle under each node, in a time slot
# Group by Node, TimeSlot, and Vehicle, then compute the arithmetic mean of Speed
dv_averaged = dv.groupby(['Node', 'TimeSlot', 'Vehicle'])['Speed'].mean().reset_index()

# Keep it perfectly stored hierarchically 
dv_averaged = dv_averaged.sort_values(by=['Node', 'TimeSlot', 'Vehicle'])

# Verify
print(dv_averaged.head(15).to_string(index=False))

# Save to your computer
dv_averaged.to_csv(r'C:\Users\THINKPAD\Downloads\speed_averaged_organized.csv', index=False, encoding='utf-8')
