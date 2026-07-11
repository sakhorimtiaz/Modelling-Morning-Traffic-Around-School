# after chnaging the names CNG to AutoRickshaw we had two rows having same vehicle name
#but different values. We need to combine them.

import pandas as pd

# Load your organized file
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency_cleaned_organized.csv', encoding='utf-8')

# --- STEP 1: SUM TOTAL_PCU FOR DUPLICATE VEHICLES ---
# This groups by Node, TimeSlot, and Vehicle, combining rows 0 & 1, 9 & 10, etc.
df_combined = df.groupby(
    ['Node', 'TimeSlot', 'VehicleType', 'Vehicle']
)['Total_PCU'].sum().reset_index()

# --- STEP 2: KEEP IT PERFECTLY SORTED HIERARCHICALLY ---
df_combined = df_combined.sort_values(by=['Node', 'TimeSlot', 'VehicleType', 'Vehicle'])

# --- STEP 3: PRINT VERIFICATION AND SAVE ---
print("\n=== COMBINED PCU VALUES (DUPLICATES REMOVED) ===")
print(df_combined.head(15).to_string(index=False))

# Save to your computer as a fresh file
df_combined.to_csv(r'C:\Users\THINKPAD\Downloads\frequency_pcu_combined.csv', index=False, encoding='utf-8')
print("\nSuccess! Saved as 'frequency_pcu_combined.csv'.")
