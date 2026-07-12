# now we will solve the equation found in the scatter chart.
# then create a new file

import os
import numpy as np
import pandas as pd

# 1. Define input and output file paths
df = pd.read_csv(r'C:\Users\THINKPAD\Downloads\traffic_flow_density_updated.csv', encoding='utf-8')


# Clean up common column name space variations from the input file if present
df.columns = df.columns.str.replace("Time Slot", "TimeSlot")
df.columns = df.columns.str.replace("Average Velocity", "Average_Velocity")

# 2. Define the model coefficients
A = 0.00352
B = 2.94
C_INTERCEPT = 283.0


# 3. Row-by-row mathematical solver matching your exact output design
def analyze_traffic_row(row):
    q = row["q (PCU/hr)"]

    # Calculate discriminant: B^2 - 4AC'
    C_prime = C_INTERCEPT - q
    discriminant = (B ** 2) - (4 * A * C_prime)

    if discriminant < 0:
        return round(discriminant, 2), np.nan, "No Real Solution"

    # Calculate the x1 root
    x1 = (-B + np.sqrt(discriminant)) / (2 * A)

    # Determine classification status based on your physical constraints
    if x1 > 0:
        status = "Valid Physical Density"
    else:
        status = "Negative Root (Non-Physical)"

    return round(discriminant, 2), round(x1, 2), status


print("--> Executing quadratic transformations...")
results = df.apply(analyze_traffic_row, axis=1)

# 4. Map outputs directly to your exact column architecture
df["Discriminant"] = [res[0] for res in results]
df["Solved_Model_Density_x1 (PCU/km)"] = [res[1] for res in results]
df["Model_Interpretation_Status"] = [res[2] for res in results]

# 5. Enforce strict column ordering to match your requested format
final_column_structure = [
    "Node",
    "TimeSlot",
    "Average_Velocity",
    "q (PCU/hr)",
    "k (PCU/km)",
    "Discriminant",
    "Solved_Model_Density_x1 (PCU/km)",
    "Model_Interpretation_Status"
]

# Ensure everything matches up perfectly
df = df[final_column_structure]

# 6. Export to CSV
new_path = r'C:\Users\THINKPAD\Downloads\traffic_flow_analysis_results.csv'
df.to_csv(new_path, index=False, encoding='utf-8')
