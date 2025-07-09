import pandas as pd

# Loading the Cumulative Average Casualties per accident without the DC8
data = pd.read_csv('withoutlier/Cumulative_Average_Casualties_Per_Accident2.csv')

# Calculate the corrected cumulative probability
total_cumulative_value = data['Cumulative Average Casualties per Accident'].iloc[-1]
data['Cumulative Probability'] = data['Cumulative Average Casualties per Accident'] / total_cumulative_value

# Save the corrected CDF to a new CSV file
new_cdf_file_name = 'withoutlier/Updated_Cumulative_Average_Casualties_Per_Accident.csv'
data.to_csv(new_cdf_file_name, index=False)

print(f"New CDF file created and saved as '{new_cdf_file_name}'.")