import pandas as pd
import numpy as np

# Loading the CDF data that we got from running the trial file
cdf_data = pd.read_csv('withall/Corrected_Cumulative_Average_Casualties_Per_Accident_CDF.csv')  

# Monte Carlo Method
num_trials = 5000  # Number of trials per simulation
num_simulations = 10  # Number of simulations

# Store the random number and casualties mapping for each simulation
all_trials_data = []

# Running the Monte Carlo simulations
for sim in range(1, num_simulations + 1):
    casualties_simulation = []
    # Generating a random number for each trial
    random_numbers = np.random.uniform(0, 1, num_trials)

    # Store each random number and its corresponding mapped value
    for rnd in random_numbers:
        for i in range(len(cdf_data)):
            if rnd <= cdf_data['Cumulative Probability'][i]:
                casualty_value = cdf_data['Average casualties per accident'][i]
                casualties_simulation.append(casualty_value)
                # Saving each random number with its mapped value and simulation number
                all_trials_data.append({
                    'Simulation': sim,
                    'Random Number': rnd,
                    'Mapped Casualty Value': casualty_value
                })
                break

# Convert all trial data to a DataFrame for saving
all_trials_df = pd.DataFrame(all_trials_data)

# Save the detailed trial data to the CSV file
detailed_results_file_name = 'Monte_Carlo_Detailed_Trial_Data.csv'
all_trials_df.to_csv(detailed_results_file_name, index=False)

# Calculating the mean casualty rate per accident for each simulation
simulation_means = [np.mean(all_trials_df[all_trials_df['Simulation'] == sim]['Mapped Casualty Value']) for sim in range(1, num_simulations + 1)]

# Convert the means to a DataFrame for saving
simulation_means_df = pd.DataFrame({
    'Simulation': range(1, num_simulations + 1),
    'Simulation Mean': simulation_means
})

# Calculating overall statistics across the simulations
overall_mean = np.mean(simulation_means)
overall_std_dev = np.std(simulation_means, ddof=1)
overall_upper_bound = overall_mean + overall_std_dev
overall_lower_bound = overall_mean - overall_std_dev

# Create a DataFrame for summary statistics
summary_stats_df = pd.DataFrame({
    'Metric': ['Overall Mean', 'Standard Deviation', 'Upper Bound', 'Lower Bound'],
    'Value': [overall_mean, overall_std_dev, overall_upper_bound, overall_lower_bound]
})

# Save the simulation means and summary statistics to a CSV file
summary_results_file_name = 'Monte_Carlo_Simulation_Means_and_Summary.csv'
simulation_means_df.to_csv(summary_results_file_name, index=False)

# Append summary statistics to the same CSV file
with open(summary_results_file_name, 'a') as f:
    f.write("\n")  # Add a blank line for separation
    summary_stats_df.to_csv(f, index=False)

print(f"Detailed trial data saved as '{detailed_results_file_name}'.")
print(f"Simulation means and summary statistics saved as '{summary_results_file_name}'.")