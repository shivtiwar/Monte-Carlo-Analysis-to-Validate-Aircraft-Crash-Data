import pandas as pd

# Loading our cumulative average casualties data without the Boeing 737 MAX
data = pd.read_csv('withoutmax/Cumulative_Average_Casualties_Per_Accident3.csv')

total_cumulative_value = data['Cumulative Average Casualties per Accident'].iloc[-1]
data['Cumulative Probability'] = data['Cumulative Average Casualties per Accident'] / total_cumulative_value

# The CDF gets saved to a new file
new_cdf_file_name = 'withoutmax/Updated_Cumulative_Average_Casualties_Per_Accident3.csv'
data.to_csv(new_cdf_file_name, index=False)

print(f"CDF file created and saved as '{new_cdf_file_name}'.")