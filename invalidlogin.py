from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
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
driver.find_element(By.ID, "username").send_keys("thomas")
driver.find_element(By.ID, "password").send_keys("SecretPassword!")

# Click "Log in" button
driver.find_element(By.XPATH, "//*[@id='login']/button").click()


# Wait for error message to be displayed
error_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "flash"))
)

# Assert error message is displayed
assert "Your username is invalid!" in error_message.text

# Close the browser
driver.quit()
