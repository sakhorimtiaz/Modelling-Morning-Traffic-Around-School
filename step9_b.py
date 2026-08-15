# calculate the traffic flow density again

import pandas as pd

# Load the finalized macroscopic files
dv = pd.read_csv(r'C:\Users\THINKPAD\Downloads\macroscopic_velocity_updated.csv', encoding='utf-8')
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\flow_rate_summary.csv', encoding='utf-8')

# Merge flow and velocity
# We use a 'left' merge on the flow data (df) so we don't lose Node B Morning,
# even if its speed is missing in dv.
master_df = pd.merge(df, dv, on=['Node', 'TimeSlot'], how='left')

# calculate taffic flow density (k)
# k = q / v
master_df['k (PCU/km)'] = master_df['q (PCU/hr)'] / master_df['Average_Velocity']

# Organize and format the new file
final_density_df = master_df[['Node', 'TimeSlot', 'q (PCU/hr)', 'Average_Velocity', 'k (PCU/km)']]

# Verify
print(final_density_df.to_string(index=False))

# Save the final file
final_density_df.to_csv(r'C:\Users\THINKPAD\Downloads\traffic_flow_density_updated.csv', index=False, encoding='utf-8')

# Now draw the bar chart again

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the file
file_path = r'C:\Users\THINKPAD\Downloads\traffic_flow_density_updated.csv'
df_density = pd.read_csv(file_path, encoding='utf-8')

# Set up plot style
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Grenerate grouped bar chart
# X-axis: Nodes | Y-axis: k (PCU/km) | Grouped (hue) by: TimeSlot
ax = sns.barplot(
    data=df_density,
    x='Node',
    y='k (PCU/km)',
    hue='TimeSlot',
    palette='Blues_d'
)

# Customize axes and labels
plt.title('Macroscopic Traffic Flow Density (k) Across Nodes and Time Slots', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Observation Nodes', fontsize=12, fontweight='bold')
plt.ylabel('Traffic Density (k) [PCU/km]', fontsize=12, fontweight='bold')
plt.legend(title='Time Slots', loc='upper right')

# Add exact numerical labels on bars
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

# Visualization
plt.tight_layout()
plt.show()
