from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and in PATH
url = 'https://asn.flightsafety.org/asndb/type/A320'
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the Selenium WebDriver
driver.quit()

# Print the pretty HTML structure
print(soup.prettify())