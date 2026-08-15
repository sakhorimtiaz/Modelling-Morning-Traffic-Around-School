"""
We we will calculate the weighted velocity.
We will select a Node > TimeSlot > Vehicle > Speed from the speed_averaged_organized file.
Then multiply the speed with the Total_PCU from the frequency_pcu_combined file.
Repeat the process for other vehicles for speed_averaged_organized file.
Loop until all the vehicles for a particular Node and TimeSlot is done.
Then sum the values and at last divide by to total PCUs in a particular node and time.
"""

import pandas as pd

# Load the files
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\speed_averaged_organized.csv', encoding='utf-8')
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency_pcu_combined.csv', encoding='utf-8')

# Match exact vehicles
# using how='inner' strictly enforces your rule: "only for the vehicles found match"
# It automatically drops any vehicle in df that doesn't exist in dv for that specific Node & TimeSlot.
matched_data = pd.merge(df, dv, on=['Node', 'TimeSlot', 'Vehicle'], how='inner')

# Multiply speed by PCU
# Collect the Speed and Total_PCU, then multiply them together
matched_data['Speed_x_PCU'] = matched_data['Speed'] * matched_data['Total_PCU']

# Add the results per node and timeslot
# Group by Node and TimeSlot, then sum the multiplied products and the matched PCUs
summary = matched_data.groupby(['Node', 'TimeSlot']).agg(
    Sum_Speed_x_PCU=('Speed_x_PCU', 'sum'),
    Sum_Matched_PCU=('Total_PCU', 'sum')
).reset_index()

# Divide by total PCU
# Divide the summed products by the total of Total_PCUs for only the matched vehicles
summary['Average_Velocity'] = summary['Sum_Speed_x_PCU'] / summary['Sum_Matched_PCU']

# Prepare a new file with 3 columns
final_output = summary[['Node', 'TimeSlot', 'Average_Velocity']]

# Verify

print(final_output.to_string(index=False))

# Save to your PC
final_output.to_csv(r'C:\Users\THINKPAD\Downloads\macroscopic_velocity.csv', index=False, encoding='utf-8')
