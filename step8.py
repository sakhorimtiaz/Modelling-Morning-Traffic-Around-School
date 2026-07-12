# now we will calculate the traffic flow density (k)
# by dividing PCU/hr by Average_Velocity.
import pandas as pd

# 1. Load the finalized macroscopic files
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\macroscopic_velocity.csv', encoding='utf-8')
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\flow_rate_summary.csv', encoding='utf-8')

# --- STEP 1: MERGE FLOW AND VELOCITY ---
# We use a 'left' merge on the flow data (df) so we don't lose Node B Morning,
# even if its speed is missing in dv.
master_df = pd.merge(df, dv, on=['Node', 'TimeSlot'], how='left')

# --- STEP 2: CALCULATE TRAFFIC FLOW DENSITY (k) ---
# k = q / v
master_df['k (PCU/km)'] = master_df['q (PCU/hr)'] / master_df['Average_Velocity']

# --- STEP 3: ORGANIZE AND FORMAT THE NEW FILE ---
# Select only your requested columns in the exact order you specified
final_density_df = master_df[['Node', 'TimeSlot', 'q (PCU/hr)', 'Average_Velocity', 'k (PCU/km)']]

# --- STEP 4: PRINT VERIFICATION AND SAVE ---
print("\n=== MACROSCOPIC TRAFFIC DENSITY (k) ===")
print(final_density_df.to_string(index=False))

# Save the final file
final_density_df.to_csv(r'C:\Users\THINKPAD\Downloads\traffic_flow_density.csv', index=False, encoding='utf-8')
print("\nSuccess! Density file saved as 'traffic_flow_density.csv'.")
