# School Traffic Study (Luxmibazar, Dhaka)

This is a joint research project by **St. Gregory’s High School and College (Dhaka, Bangladesh)** and **Bluebells School International (New Delhi, India)**. 

We collected traffic data near schools during busy pickup and drop-off times (7:00 AM, 11:00 AM, and 4:30 PM). We built this Python tool to clean the data, calculate traffic speeds, and map out where the biggest traffic jams happen in Old Dhaka.

---

## 🚀 What This Code Does

* **Standardizes Vehicles:** Converts different vehicles (like rickshaws, cars, and auto-rickshaws) into a single standard unit (Passenger Car Unit, or PCU) so we can compare them fairly.
* **Calculates True Speed:** Finds the average speed of traffic, making sure slow heavy vehicles and fast light vehicles are balanced correctly.
* **Measures Road Crowdedness:** Calculates what percentage of the road is physically filled with vehicles.
* **Grades Traffic Jams:** Gives the road a traffic grade from A (free-moving) to F (complete traffic jam).
* **Tracks Queue Lengths:** Uses real street distances to show exactly how far back a traffic jam stretches.

---

## 📂 Project Files

The Python scripts run in order from `step1.py` to `step15.py`:

```directory
├── data/
│   ├── Vehicle_units.csv         # Standard values for each vehicle type
│   ├── queue_length.csv          # Real measurements of traffic queue lengths
│   ├── frequency_cleaned.csv     # Raw vehicle count data
│   └── velocity_cleaned.csv      # Raw speed data
├── scripts/
│   ├── step1.py                  # Imports and checks the data files
│   ├── step2.py                  # Cleans the data and fixes vehicle names
│   ├── step7.py                  # Calculates average traffic speed
│   ├── step11.py                 # Calculates traffic density (vehicles per km)
│   ├── step14.py                 # Grades the traffic from A to F
│   └── step15.py                 # Calculates how much road space is occupied
└── README.md
```
🧮 Simple Traffic Formula
We use a standard formula to understand traffic flow:

Flow = Density * Speed

Flow: How many vehicles pass by per hour.

Density: How many vehicles are packed into 1 kilometer of road.

Speed: How fast the vehicles are moving.

👥 Our Team
Lead Researcher & Programmer: K. M. Imtiaz Hossain (Mathematics Teacher, St. Gregory’s)

Project Partner: Miss K (St. Gregory’s)

School Partner: Bluebells School International (New Delhi)

Data Collection Team: 12 Students & 8 Teachers from St. Gregory's

🔒 Rules and Privacy
Ownership: All data and Python scripts belong to St. Gregory’s High School and College and our research team.

Privacy: Do not share, copy, or use this data for other projects without asking us first.
