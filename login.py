"""Login Test"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialization of web driver
driver = webdriver.Chrome()

# Launch website
driver.get("https://the-internet.herokuapp.com/")

# Click on the "Form Authentication" link
driver.find_element(By.LINK_TEXT, "Form Authentication").click()

# Enter username and password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click "Log in" button
driver.find_element(By.XPATH, "//*[@id='login']/button").click()

# Wait for success message to be displayed
success_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "flash"))
)

# Assert success message is displayed
assert "You logged into a secure area!" in success_message.text

# Close the browser
driver.quit()
