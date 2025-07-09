import pandas as pd

# Loading the data including the average casualties per accident without the DC 8
data = pd.read_csv('withoutlier/Flight Data - Sheet2.csv')

data['Average casualties per accident'] = pd.to_numeric(data['Average casualties per accident'], errors='coerce')

# Sorting data in ascending order
data = data.sort_values(by='Average casualties per accident').reset_index(drop=True)

# Calculating the cumulative average of all flights
data['Cumulative Average Casualties per Accident'] = data['Average casualties per accident'].cumsum()

cumulative_data = data[['Flight', 'Average casualties per accident', 'Cumulative Average Casualties per Accident']]

# Saving to a new CSV file
cumulative_file_name = 'Cumulative_Average_Casualties_Per_Accident2.csv'
cumulative_data.to_csv(cumulative_file_name, index=False)

print(f"Cumulative average casualties file created and saved as '{cumulative_file_name}'.")