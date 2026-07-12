# In the frequency_pcu_combined file we have two or more values of same vehicles.
# We will calculate the average.



import pandas as pd

# 1. Load your cleaned velocity file
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\velocity_cleaned.csv', encoding='utf-8')

# --- STEP 1: COMPUTE AVERAGE SPEED PER COHORT ---
# Group by Node, TimeSlot, and Vehicle, then compute the arithmetic mean of Speed
dv_averaged = dv.groupby(['Node', 'TimeSlot', 'Vehicle'])['Speed'].mean().reset_index()

# --- STEP 2: KEEP IT PERFECTLY SORTED HIERARCHICALLY ---
dv_averaged = dv_averaged.sort_values(by=['Node', 'TimeSlot', 'Vehicle'])

# --- STEP 3: PRINT VERIFICATION AND SAVE ---
print("\n=== CONSOLIDATED VEHICLE SPEEDS (AVERAGED) ===")
print(dv_averaged.head(15).to_string(index=False))

# Save to your computer as a fresh, organized velocity profile
dv_averaged.to_csv(r'C:\Users\THINKPAD\Downloads\speed_averaged_organized.csv', index=False, encoding='utf-8')
