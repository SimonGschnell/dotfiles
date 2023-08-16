from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to the ChromeDriver executable
chromedriver_path="/home/simon/.config/i3/scripts/chromedriver-linux64/chromedriver"

# Create a ChromeService instance with the executable path
chrome_service = ChromeService(executable_path=chromedriver_path)

# Initialize the Chrome WebDriver with the ChromeService
driver = webdriver.Chrome(service=chrome_service)

try:
    # URL to scrape
    url = "https://account.lenovo.com/at/de/account/login/index.html?returnUrl=https%3A%2F%2Faccount.lenovo.com%2Fat%2Fde%2Faccount%2Fhome.html"

    # Open the URL
    driver.get(url)
   
    time.sleep(6)
    # email
    email_input = driver.find_element(By.ID,'emailAddress')
    

    # password 
    password_input = driver.find_element(By.ID,'password')

    username = "io23m005@technikum-wien.at"
    password = "Passwort5!"

    email_input.send_keys(username)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)
    anmelden_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@data-tkey="signIn" and contains(text(), "Anmelden")]'))
    )
    anmelden_button.click()

    time.sleep(9)
    # Wait for a few seconds to ensure the login is complete

    # Navigate back to the target URL
    time.sleep(5)
    #order_status_button = driver.find_element(By.XPATH, '//*[@aria-label="Bestellstatus anzeigen"]')
    #order_status_button.click()

    # Wait for a few seconds to ensure the page is loaded
    time.sleep(4)

    # Find and print the tag content
    tag_element = driver.find_elements(By.CSS_SELECTOR, 'div.order-status')[1]
    tag_content = tag_element.text.strip()

    print("Tag content:", tag_content)

except Exception as e:
    print("Error:", str(e))

finally:
    # Close the browser
    driver.quit()

