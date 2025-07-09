# from selenium import webdriver
# from bs4 import BeautifulSoup
# import csv
# import time

# # Define the URL
# url = 'https://asn.flightsafety.org/asndb/type/A320'

# # Set up Selenium WebDriver
# driver = webdriver.Chrome()  # Make sure to have ChromeDriver installed and in PATH
# driver.get(url)

# # Wait for the page to fully load
# time.sleep(5)

# # Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # Close the Selenium WebDriver
# driver.quit()

# # Initialize an empty list to store incident details
# incidents = []

# # Extracting each row with the class "list"
# for row in soup.find_all('tr', class_='list'):
#     # Extract each column within the row
#     columns = row.find_all('td')
    
#     # Check if the row has the expected columns for Date and Fatalities
#     if len(columns) >= 5:  # Ensure there are enough columns
#         date = columns[0].get_text(strip=True)
#         fatalities = columns[4].get_text(strip=True)
        
#         # Store the data in a dictionary
#         incident_data = {
#             'Date': date,
#             'Fatalities': fatalities
#         }
#         incidents.append(incident_data)

# # Check if incidents list is populated (for debugging)
# if incidents:
#     print("Incidents found:", incidents)
# else:
#     print("No incidents found. Please check the class names and HTML structure.")

# # Save the data to a CSV file if incidents are found
# if incidents:
#     with open('A320_incidents.csv', 'w', newline='') as csvfile:
#         fieldnames = ['Date', 'Fatalities']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(incidents)
#     print("Data saved to A320_incidents.csv")
# else:
#     print("No data to save.")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

# Base URL pattern
base_url = 'https://asn.flightsafety.org/asndb/type/_B787'

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Initialize an empty list to store incident details
incidents = []

try:
    # Loop through all 13 pages
    for page in range(1, 4):
        # Construct the URL for each page
        url = f'{base_url}/{page}' if page > 1 else base_url
        driver.get(url)
        
        # Wait until at least one row with the class 'list' is present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'list'))
        )

        # Parse the HTML with BeautifulSoup after confirming content load
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extracting each row with the class "list"
        for row in soup.find_all('tr', class_='list'):
            # Extract each column within the row
            columns = row.find_all('td')
            
            # Check if the row has the expected columns for Date and Fatalities
            if len(columns) >= 5:  # Ensure there are enough columns
                date = columns[0].get_text(strip=True)
                fatalities = columns[4].get_text(strip=True)
                
                # Store the data in a dictionary
                incident_data = {
                    'Date': date,
                    'Fatalities': fatalities
                }
                incidents.append(incident_data)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the Selenium WebDriver
    driver.quit()

# Save the data to a CSV file if incidents are found
if incidents:
    with open('787.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Fatalities']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(incidents)
    print("Data saved to A320_incidents.csv")
else:
    print("No data to save.")