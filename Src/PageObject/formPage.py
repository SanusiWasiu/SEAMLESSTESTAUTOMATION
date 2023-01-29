# import sys
# import os
# sys.path.append(sys.path[0] + "/...")
# sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locator

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        # Url launch
        self.driver.get("https://the-internet.herokuapp.com/")
        # load form authentication page
        self.driver.find_element(By.LINK_TEXT, Locator.formLink).click()

    def login(self, username, password):
        # Enter username and password
        self.driver.find_element(By.ID, Locator.username).send_keys(username)
        self.driver.find_element(By.ID, Locator.password).send_keys(password)
        # Click "Log in" button
        self.driver.find_element(By.XPATH, Locator.button).click()

    def get_alert(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, Locator.alert))
        )