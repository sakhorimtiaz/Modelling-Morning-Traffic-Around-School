# we will calculate a flow rate summary

import pandas as pd

# Load the files
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency_cleaned.csv', encoding='utf-8')
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\velocity_cleaned.csv', encoding='utf-8')

# Calculate hourly flow rate (q)

# Multiply Frequency with PCU row-wise to get Total PCU per row
df['Total_PCU'] = df['Frequency'] * df['PCU']

# Group by Node and TimeSlot, then sum up the PCUs
flow_summary = df.groupby(['Node', 'TimeSlot'])['Total_PCU'].sum().reset_index()

# Convert 15-minute counts to an hourly rate (q) by multiplying by 4
flow_summary['q (PCU/hr)'] = flow_summary['Total_PCU'] * 4

# Display the summary table
print(flow_summary[['Node', 'TimeSlot', 'Total_PCU', 'q (PCU/hr)']].to_string(index=False))

# Save this summary table to your computer
flow_summary.to_csv(r'C:\Users\THINKPAD\Downloads\flow_rate_summary.csv', index=False, encoding='utf-8')
