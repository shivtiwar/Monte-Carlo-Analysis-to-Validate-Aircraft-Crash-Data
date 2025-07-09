import pandas as pd

#This is the code used to load each of the scraped data and calculate the total number of fatalities
df = pd.read_csv('Data/747_incidents.csv') #Loads the file

df['Fatalities'] = pd.to_numeric(df['Fatalities'], errors='coerce') #Took values from the Fatalities column

# Calculate the sum of all fatalities
total_fatalities = df['Fatalities'].sum()

# Display the total
print("Total fatalities:", total_fatalities)