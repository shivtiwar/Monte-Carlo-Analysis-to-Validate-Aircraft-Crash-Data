import pandas as pd
import matplotlib.pyplot as plt

# Made a dataframe to plot the cumulative average casualties per accident to the cumulative probability, the data that we got from Corrected_Cumulative_Average_Casualties_Per_Accident_CDF.csv
cdf_data = pd.DataFrame({
    'Flight': ['Airbus A380', 'Airbus A321N', 'Airbus A320N', 'Embraer jet', 'Boeing 737 NG', 'Airbus A321', 
               'Airbus A320', 'Boeing 777', 'DM80', 'Boeing 737 MAX', 'Boeing 737', 'DC9', 'Boeing 747', 
               'Boeing 767', 'DC8'],
    'Average casualties per accident': [0.0, 0.0, 0.02450980392, 0.2342857143, 0.4783950617, 0.8855140187, 
                                        0.887675507, 0.9801084991, 2.713157895, 2.724409449, 2.98094028, 
                                        3.986975398, 5.33744856, 6.222634508, 12.24137931],
    'Cumulative Average Casualties per Accident': [0.0, 0.0, 0.02450980392, 0.25879551822, 0.73719057992, 
                                                   1.62270459862, 2.51038010562, 3.49048860472, 6.20364649972, 
                                                   8.928055948719999, 11.90899622872, 15.89597162672, 
                                                   21.23342018672, 27.45605469472, 39.697434004719995],
    'Cumulative Probability': [0.0, 0.0, 0.000617415320020075, 0.006519200162640976, 0.018570232520125827, 
                               0.04087681330806071, 0.06323784316441002, 0.08792731047314, 0.15627323667777596, 
                               0.2249025956604263, 0.299994106100259, 0.40042818951043485, 0.5348814279581738, 
                               0.691632982914097, 1.0]
})

# Making the CDF plot
plt.figure(figsize=(12, 8))
for i in range(len(cdf_data)):
    plt.step(
        [cdf_data['Cumulative Probability'][i-1] if i > 0 else 0, cdf_data['Cumulative Probability'][i]],
        [cdf_data['Cumulative Average Casualties per Accident'][i]] * 2,
        where='post',
        linewidth=3,  
        label=cdf_data['Flight'][i]
    )

# Labels and title of the plot
plt.xlabel('Cumulative Probability')
plt.ylabel('Cumulative Average Casualties per Accident')
plt.title('Cumulative Distribution Function (CDF) of Average Casualties per Accident by Flight')
plt.grid(True)

# Legend added using the dataframe
plt.legend(title="Aircraft Type", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)

plt.tight_layout()
plt.show()