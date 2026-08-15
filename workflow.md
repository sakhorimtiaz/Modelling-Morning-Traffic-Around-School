# Traffic Modeling Pipeline: Step-by-Step Workflow

This document outlines the sequential data processing pipeline used to analyze school-hour traffic congestion in Luxmibazar, Dhaka, Bangladesh.

---

## 📊 Initial Datasets
We began our analysis with four raw CSV files:
* `Vehicle_units.csv` — Standard Passenger Car Unit (PCU) values per vehicle type.
* `queue_length.csv` — Physical field measurements of traffic queue lengths.
* `frequency.csv` — Raw vehicle counts over time.
* `velocity.csv` — Raw vehicle speed measurements.

### 📅 Research Timeline & Academic Defence
* **The Situation:** Speed data was collected on April 19 and 21. Because we arrived slightly late on those mornings, we recollected the frequency (volume) data on June 6 to ensure we captured the full morning school peak starting at 7:15 AM.
* **Reviewer Critique:** How can you combine dry April data with wet June data, when weather, school attendance, and traffic patterns change?
* **Our Defence:** While absolute traffic volumes shift across months, the speed-to-volume ratio per vehicle class remains structurally constant within the narrow 7:15 AM drop-off window. Our weighted velocity method acts as a mathematical stabilizer against these baseline shifts.

---

## 🚀 The 15-Step Data Pipeline

### Step 1: Align Vehicle Names and Time Slots
* **Goal:** Cross-check the vehicle names and time slots between our datasets to ensure they match.
* **Code File:** `step1.py`
* **Input Files:** `frequency.csv`, `velocity.csv`
* **Finding:** Identified slight differences in vehicle names (e.g., "Rickshaw" vs "ManualRickshaw") that needed normalization.

---

### Step 2: Clean and Normalize Data
* **Goal:** Rename mismatched columns and map unmeasured vehicles to standard PCU categories.
* **Code File:** `step2.py`
* **Actions Taken:**
  * Renamed columns to standard formats (`Vehicle`, `TimeSlot`, `Speed`).
  * Mapped unknown vehicles to matching sizes (e.g., `Pickup` = `Leguna` and `CNG` = `AutoRickshaw`).
  * Multiplied vehicle counts by their respective PCU values.
* **Output Files:** `frequency_cleaned.csv`, `velocity_cleaned.csv`

---

### Step 3: Organize Cleaning Output
* **Goal:** Group and structure the cleaned frequency data hierarchically.
* **Code File:** `step3.py`
* **Hierarchy:** Organized by `Node` ➔ `TimeSlot` ➔ `VehicleType` ➔ `Vehicle` ➔ `Total_PCU`.
* **Output File:** `frequency_cleaned_organized.csv`

---

### Step 4: Merge Duplicate Vehicle Categories
* **Goal:** Combine duplicate entries created by renaming (such as merging the CNG and AutoRickshaw rows).
* **Code File:** `step4.py`
* **Output File:** `frequency_pcu_combined.csv`

---

### Step 5: Calculate Hourly Flow Rate
* **Goal:** Convert raw vehicle counts into an hourly flow rate (PCU per hour).
* **Code File:** `step5.py`
* **Output File:** `flow_rate_summary.csv`

---

### Step 6: Average Multiple Speed Entries
* **Goal:** Calculate the average speed for instances where a vehicle has multiple speed records.
* **Code File:** `step6.py`
* **Output File:** `speed_averaged_organized.csv`

---

### Step 7: Calculate Macroscopic Weighted Velocity
* **Goal:** Calculate the true average traffic speed by weighting speed against volume (PCU).
* **Code File:** `step7.py`
* **Mathematical Note:** If a vehicle has speed data but zero volume (like Bicycles in Node A Morning due to multi-day collection offsets), its weight is 0. This mathematically drops it from the final calculation without breaking the model.
* **Output File:** `macroscopic_velocity.csv`

---

### Step 8: Calculate Traffic Density
* **Goal:** Find the initial traffic density ($k$) using the basic traffic equation: $k = \text{Flow} / \text{Speed}$.
* **Code File:** `step8.py`
* **Output File:** `traffic_flow_density.csv`

### Visual Quality Check
* **Goal:** Plot a bar chart of the density output to verify data completeness.
* **Code File:** `step8_Check.py`
* **Finding:** Spotted a missing velocity data point for Node B Morning, which left its density value empty.

---

### Step 9: Handle Missing Node B Morning Data
* **Goal:** Fill the missing Node B Morning velocity data point using a logical baseline.
* **Code File:** `step9_a.py`
* **Logic:** Node B Evening operates at a very low flow ($275.36\text{ PCU/hr}$) and low density ($26.93\text{ PCU/km}$). We substituted this uncongested evening velocity as a conservative baseline for the morning model.
* **Output File:** `macroscopic_velocity_updated.csv`

### Recalculate Final Densities and Plot an Updated Bar Chart
* **Goal:** Run the density calculations again with the complete velocity dataset.
* **Code File:** `step9_b.py`
* **Output File:** `traffic_flow_density_updated.csv` (along with an updated bar chart).

---

### Step 10: Generate Traffic Scatter Plots
* **Goal:** Plot flow-density-speed relationships to observe real-world trends.
* **Code File:** `step10.py`
* **Output Visual:** Scatter chart showing how traffic behaves at different congestion levels.
* **Reference Files:**
  * We recommend to check the `Scatter_Chart_diagram.xlsx` file (https://docs.google.com/spreadsheets/d/1pTX6XNRvtXkueE_QyKv9kRD7zYeLrwZujpLalzx4ag4/edit?usp=sharing) to view the scatter plot in spreadsheet/Google Doc format. The xlsx file is better to understand the charracteristics of the Scatter Plot rather than using the python code.
  * Check the `Scatter_chart_concepts.pdf` file to understand how we drew this chart.

---

### Step 11: Solve Traffic State Equations
* **Goal:** Solve the mathematical equations generated from our scatter plot trendlines.
* **Code File:** `step11.py`
* **Output File:** `traffic_flow_analysis_results.csv`

---

### Step 12: Assign Level of Service (LOS) Grades
* **Goal:** Classify the traffic quality from A (free-moving) to F (gridlock) based on density thresholds.
* **Output File:** `level_of_service_LOS.csv`
* **Reference File:** Read the `LOS_ground_truth` file to understand ground truth behind the results in `level_of_service_LOS.csv`.

---

### Step 15: Calculate Road Space Occupancy Percentage
* **Goal:** Determine what percentage of the physical road length is occupied by vehicles.
* **Code File:** `step15.py`
* **Formula:** Based on a baseline vehicle length of 4.6 meters per PCU:
  $$\text{Occupancy \%} = \frac{k \times 4.6\text{ m}}{1000\text{ m}} \times 100$$
* **Output File:** `percent_of_road_occupied.csv`
