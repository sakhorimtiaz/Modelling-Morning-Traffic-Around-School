# calculate the traffic flow density again

import pandas as pd

# 1. Load the finalized macroscopic files
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\macroscopic_velocity_updated.csv', encoding='utf-8')
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
final_density_df.to_csv(r'C:\Users\THINKPAD\Downloads\traffic_flow_density_updated.csv', index=False, encoding='utf-8')
print("\nSuccess! Density file saved as 'traffic_flow_density.csv'.")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- STEP 1: LOAD THE DENSITY CSV ---
file_path = r'C:\Users\THINKPAD\Downloads\traffic_flow_density_updated.csv'
df_density = pd.read_csv(file_path, encoding='utf-8')

# --- STEP 2: SET UP PLOT STYLE ---
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# --- STEP 3: GENERATE GROUPED BAR CHART ---
# X-axis: Nodes | Y-axis: k (PCU/km) | Grouped (hue) by: TimeSlot
ax = sns.barplot(
    data=df_density,
    x='Node',
    y='k (PCU/km)',
    hue='TimeSlot',
    palette='Blues_d'
)

# --- STEP 4: CUSTOMIZE AXES AND LABELS ---
plt.title('Macroscopic Traffic Flow Density (k) Across Nodes and Time Slots', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Observation Nodes', fontsize=12, fontweight='bold')
plt.ylabel('Traffic Density (k) [PCU/km]', fontsize=12, fontweight='bold')
plt.legend(title='Time Slots', loc='upper right')

# --- STEP 5: ADD EXACT NUMERICAL LABELS ON BARS ---
for p in ax.patches:
    height = p.get_height()
    # Safely skip missing values (like Node B Morning) without crashing
    if pd.notna(height) and height > 0:
        ax.annotate(
            f'{height:.1f}',
            (p.get_x() + p.get_width() / 2., height),
            ha='center',
            va='center',
            xytext=(0, 8),
            textcoords='offset points',
            fontsize=10,
            fontweight='bold',
            color='#2c3e50'
        )

# --- STEP 6: RENDER THE VISUAL ---
plt.tight_layout()
plt.show()
