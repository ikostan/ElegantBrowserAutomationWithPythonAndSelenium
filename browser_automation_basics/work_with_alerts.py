import time
import unittest
from selenium import webdriver
from browser_automation_basics.page_model.test_page_model import TestPage
from browser_automation_basics.locators.test_page_locator import TestPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def first_automation():

    # Open web page
    driver = webdriver.Chrome()
    wrong_url = 'https://google.com'
    page = TestPage(driver)
    page.driver.get(TestPageLocator.URL)

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
    time.sleep(1)
    page.driver.close()
    if page.driver:
        page.driver.quit()


if __name__ == '__main__':
    first_automation()
