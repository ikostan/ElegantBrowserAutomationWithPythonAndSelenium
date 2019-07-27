import time
import unittest
from browser_automation_basics.utils.utils import open_web_page, close_web_page
from browser_automation_basics.locators.test_page_locator import TestPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def first_automation():

    # Open web page
    page = open_web_page(TestPageLocator.URL)

    # Click on Button1
    button_1 = page.get_button_1()
    button_1.click()

    # Working with alert
    alert = WebDriverWait(page.driver, 10).until(expected_conditions.alert_is_present())
    unittest.TestCase().assertEqual('You clickedButton1.', alert.text)
    time.sleep(2)

    # Close alert and go back to main window
    alert.accept()

    # Close web browser
    close_web_page(page)


if __name__ == '__main__':
    first_automation()
