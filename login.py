from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialization of web driver
driver = webdriver.Chrome()

# Navigate to website
driver.get("https://the-internet.herokuapp.com/")

# Click "Form Authentication"
driver.find_element_by_link_text("Form Authentication").click()

# Enter username and password
driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_id("password").send_keys("SuperSecretPassword!")

# Click "Log in" button
driver.find_element_by_css_selector("button[type='submit']").click()

# Wait for success message to be displayed
success_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "flash"))
)

# Assert success message is displayed
assert "You logged into a secure area!" in success_message.text

# Close the browser
driver.quit()
