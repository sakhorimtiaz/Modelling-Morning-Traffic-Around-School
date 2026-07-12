# now we will draw the scatter chart

import numpy as np
import matplotlib.pyplot as plt

# 1. Define the empirical data points from your study
k_density = np.array([94.36, 39.60, 18.02, 26.93, 47.93, 51.76, 27.33, 119.13, 31.20])
q_flow = np.array([554.64, 425.48, 219.20, 275.36, 234.64, 529.20, 446.68, 708.32, 612.52])

# 2. Coefficients from your Google Sheets aggregate trendline
# Equation: q = 0.00352*x^2 + 2.94*x + 283
A = 0.00352
B = 2.94
C_intercept = 283.0

print(f"{'Empirical q':<12} | {'Discriminant':<14} | {'Physical Root (x1)':<20} | {'Status'}")
print("-" * 65)

# Calculate the exact roots for each empirical q value
for q in q_flow:
    # Rearranged to standard form: A*x^2 + B*x + (C_intercept - q) = 0
    C_prime = C_intercept - q
    discriminant = (B ** 2) - (4 * A * C_prime)
    
    if discriminant < 0:
        print(f"{q:<12.2f} | {discriminant:<14.2f} | {'None':<20} | No Real Solutions")
    else:
        x1 = (-B + np.sqrt(discriminant)) / (2 * A)
        x2 = (-B - np.sqrt(discriminant)) / (2 * A)
        
        # Determine if the root is physically meaningful for traffic density
        if x1 > 0:
            status = "Valid Physical Density"
            display_root = f"{x1:.2f} PCU/km"
        else:
            status = "Negative Root (Impossible)"
            display_root = f"{x1:.2f} PCU/km"
        print(f"{q:<12.2f} | {discriminant:<14.2f} | {display_root:<20} | {status}")

# 3. Generate the Academic Plot
plt.figure(figsize=(9, 6))

# Plot the raw empirical data points
plt.scatter(k_density, q_flow, color='darkorange', edgecolors='black', s=80, zorder=5, label='Empirical Node Data')

# Generate smooth line points for the trendline curve
k_smooth = np.linspace(0, 130, 300)
q_trend = A * (k_smooth ** 2) + B * k_smooth + C_intercept
plt.plot(k_smooth, q_trend, color='navy', linestyle='--', linewidth=2, label='Aggregate Polynomial Trendline')

# Define Variables clearly on the axes
plt.xlabel('INDEPENDENT VARIABLE: Traffic Density, k (PCU/km)', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('DEPENDENT VARIABLE: Traffic Flow, q (PCU/hr)', fontsize=11, fontweight='bold', labelpad=10)
plt.title('Macroscopic Traffic Flow Architecture (Aggregate Model)', fontsize=13, fontweight='bold', pad=15)

# Visual styling
plt.xlim(0, 130)
plt.ylim(0, 850)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', frameon=True, shadow=True)

# Annotate the anomalous upward-bending behavior
plt.annotate('Upward resilience tail\n(No flow collapse)', xy=(119.13, 708.32), xytext=(75, 780),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3))

plt.tight_layout()
plt.show()
