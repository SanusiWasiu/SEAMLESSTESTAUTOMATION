import unittest
import sys
sys.path.append(sys.path[0] + "/....")

from Src.TestBase.webDriverSetUp import WebDriverSetup
from Src.PageObject.formPage import FormPage

class TestLogin(WebDriverSetup):
    def test_valid_login(self):
        super().setUp()
        driver = self.driver
        form_page = FormPage(driver)
        form_page.load_page()
        form_page.login("tomsmith", "SuperSecretPassword!")
        success_message = form_page.get_alert()
        # Assert success message is displayed
        self.assertIn("You logged into a secure area!", success_message.text)
        self.assertEqual(1, 1)
        # assert "You logged into a secure area!" in success_message.text
        super().tearDown()

    def test_invalid_login(self):
        super().setUp()
        driver = self.driver
        form_page = FormPage(driver)
        form_page.load_page()
        form_page.login("thomas", "SecretPassword!")
        error_message = form_page.get_alert()
        # Assert error message is displayed
        assert "Your username is invalid!" in error_message.text
        super().tearDown()
    
if __name__ == '__main__':
    unittest.main()