import pandas as pd
import matplotlib.pyplot as plt

Load data
file_path = r'C:\Users\THINKPAD\Downloads\frequency_cleaned_pie_chart.csv'
df = pd.read_csv(file_path, encoding='utf-8')

Aggregate data for the first pie chart (Motorized vs Non-Motorized)
type_counts = df.groupby('VehicleType')['Frequency'].sum()

Aggregate data for the second pie chart (Each Vehicle)
vehicle_counts = df.groupby('Vehicle')['Frequency'].sum()

# Optional: Filter out vehicles with 0 total frequency (like Bicycle in some nodes) to keep the chart clean
vehicle_counts = vehicle_counts[vehicle_counts > 0]

# Create the figure and subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Chart 1: Motorized vs. Non-Motorized
ax1.pie(type_counts,
        labels=type_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=['#66b3ff', '#ff9999'])
ax1.set_title('Motorized vs. Non-Motorized Vehicles', fontsize=14, pad=20)

# Chart 2: Individual Vehicle Breakdown
# Using a colormap to automatically generate distinct colors for the multiple vehicle categories
colors = plt.cm.Set3(range(len(vehicle_counts)))

ax2.pie(vehicle_counts,
        labels=vehicle_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors)
ax2.set_title('Percentage of Each Vehicle', fontsize=14, pad=20)

# Adjust layout to prevent overlap and display the charts
plt.tight_layout()
plt.show()
