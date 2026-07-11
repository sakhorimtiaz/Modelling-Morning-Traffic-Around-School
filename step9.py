# we want to show out bar diagram

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- STEP 1: LOAD THE DENSITY CSV ---
file_path = r'C:\Users\THINKPAD\Downloads\traffic_flow_density.csv'
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
