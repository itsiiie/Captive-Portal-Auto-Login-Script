from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'Enter your Username'
PASSWORD = 'Enter your Password'

# Initialize the WebDriver (for example, using Chrome)
driver = webdriver.Chrome()  # Specify the path to chromedriver if necessary

try:
    # Open the login page
    driver.get('http://192.168.10.1:8090/httpclient.html')

    # Wait for the username input field to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )

    # Find the username and password input fields
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    # Enter the username and password
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    # Submit the login form
    password_input.send_keys(Keys.RETURN)

    # Wait for the main page to load after login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'some_element_on_main_page'))  # Change to an actual element on the main page
    )

    # Print success message
    print("Login successful")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()
