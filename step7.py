# now we will calculate the weighted velocity

import pandas as pd

# 1. Load the files
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\speed_averaged_organized.csv', encoding='utf-8')
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\frequency_pcu_combined.csv', encoding='utf-8')

# --- STEP 1: MATCH EXACT VEHICLES ---
# using how='inner' strictly enforces your rule: "only for the vehicles found match"
# It automatically drops any vehicle in df that doesn't exist in dv for that specific Node & TimeSlot.
matched_data = pd.merge(df, dv, on=['Node', 'TimeSlot', 'Vehicle'], how='inner')

# --- STEP 2: MULTIPLY SPEED BY PCU ---
# Collect the Speed and Total_PCU, then multiply them together
matched_data['Speed_x_PCU'] = matched_data['Speed'] * matched_data['Total_PCU']

# --- STEP 3: ADD THE RESULTS PER NODE AND TIMESLOT ---
# Group by Node and TimeSlot, then sum the multiplied products and the matched PCUs
summary = matched_data.groupby(['Node', 'TimeSlot']).agg(
    Sum_Speed_x_PCU=('Speed_x_PCU', 'sum'),
    Sum_Matched_PCU=('Total_PCU', 'sum')
).reset_index()

# --- STEP 4: DIVIDE BY TOTAL PCU ---
# Divide the summed products by the total of Total_PCUs for only the matched vehicles
summary['Average_Velocity'] = summary['Sum_Speed_x_PCU'] / summary['Sum_Matched_PCU']

# --- STEP 5: PREPARE NEW FILE WITH 3 COLUMNS ---
final_output = summary[['Node', 'TimeSlot', 'Average_Velocity']]

print("\n=== MACROSCOPIC STREAM VELOCITY (NODE & TIME SLOT) ===")
print(final_output.to_string(index=False))

# Save the final 9-row dataframe to your PC
final_output.to_csv(r'C:\Users\THINKPAD\Downloads\macroscopic_velocity.csv', index=False, encoding='utf-8')
print("\nFile successfully processed and saved as 'macroscopic_velocity.csv'!")
