from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a Chrome driver instance
driver = webdriver.Chrome(ChromeDriverManager().install())

# Get Chrome driver version
driver_version = driver.capabilities['chrome']['chromedriverVersion']

# Print the version
print("Chrome Driver Version:", driver_version)

# Close the browser window
driver.quit()

