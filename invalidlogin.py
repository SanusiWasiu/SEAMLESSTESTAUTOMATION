from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize web driver
driver = webdriver.Chrome()

# Navigate to website
driver.get("https://the-internet.herokuapp.com/")

# Click "Form Authentication"
driver.find_element_by_link_text("Form Authentication").click()

# Enter username and password
driver.find_element_by_id("username").send_keys("thomas")
driver.find_element_by_id("password").send_keys("SecretPassword!")

# Click "Log in" button
driver.find_element_by_css_selector("button[type='submit']").click()

# Wait for error message to be displayed
error_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "flash"))
)

# Assert error message is displayed
assert "Your username is invalid!" in error_message.text

# Close the browser
driver.quit()
