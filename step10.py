# As we can see that the Average velocity of Node B Morning is missing in the macroscopic_velocity file,
#the ouput for density (k) is missing. 
#We are condering the average velocity of evening in the node B as Free flow
# Lets put the value and create a new file

import pandas as pd

# 1. Load the original file
old_path = r'C:\Users\THINKPAD\Downloads\macroscopic_velocity.csv'
df = pd.read_csv(old_path, encoding='utf-8')

# 2. Extract the local free-flow velocity for Node B
v_baseline = df.loc[(df['Node'] == 'B') & (df['TimeSlot'] == 'Evening'), 'Average_Velocity'].values[0]

# 3. Directly append the missing Morning row using a clean dictionary entry
new_row = pd.DataFrame([{'Node': 'B', 'TimeSlot': 'Morning', 'Average_Velocity': v_baseline}])
df = pd.concat([df, new_row], ignore_index=True)

# 4. Sort it neatly and save to your NEW filename
df = df.sort_values(by=['Node', 'TimeSlot']).reset_index(drop=True)

new_path = r'C:\Users\THINKPAD\Downloads\macroscopic_velocity_updated.csv'
df.to_csv(new_path, index=False, encoding='utf-8')

print(f"Success! Cleaned data saved to a new file at: {new_path}")
print(df)
