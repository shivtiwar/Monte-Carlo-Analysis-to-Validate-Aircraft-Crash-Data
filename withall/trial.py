import pandas as pd

# Loading the data including all the 15 planes
data = pd.read_csv('withall/Flight Data - Sheet1.csv')

# Loading th Average casualties per accident column
data['Average casualties per accident'] = pd.to_numeric(data['Average casualties per accident'], errors='coerce')

# Sorting the data in ascending order
data = data.sort_values(by='Average casualties per accident').reset_index(drop=True)

# Cumulative average casualties per accident for each airplane
data['Cumulative Average Casualties per Accident'] = data['Average casualties per accident'].cumsum()

cumulative_data = data[['Flight', 'Average casualties per accident', 'Cumulative Average Casualties per Accident']]

# Save to a new CSV file
cumulative_file_name = 'Cumulative_Average_Casualties_Per_Accident.csv'
cumulative_data.to_csv(cumulative_file_name, index=False)

print(f"Cumulative average casualties file created and saved as '{cumulative_file_name}'.")