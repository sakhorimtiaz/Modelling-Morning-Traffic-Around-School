# now we will calculate the traffic flow density (k)
# by dividing PCU/hr by Average_Velocity.
import pandas as pd

# Load macroscopic_velocity.csv and flow_rate_summary.csv files
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\macroscopic_velocity.csv', encoding='utf-8')
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\flow_rate_summary.csv', encoding='utf-8')

# Merge flow and velocity
# We use a 'left' merge on the flow data (df) so we don't lose Node B Morning,
# even if its speed is missing in dv.
master_df = pd.merge(df, dv, on=['Node', 'TimeSlot'], how='left')

# Calculate traffic flow density (k)
# k = q / v
master_df['k (PCU/km)'] = master_df['q (PCU/hr)'] / master_df['Average_Velocity']

# Organize and format the new file
final_density_df = master_df[['Node', 'TimeSlot', 'q (PCU/hr)', 'Average_Velocity', 'k (PCU/km)']]

# Verify
print(final_density_df.to_string(index=False))

# Save the final file
final_density_df.to_csv(r'C:\Users\THINKPAD\Downloads\traffic_flow_density.csv', index=False, encoding='utf-8')
