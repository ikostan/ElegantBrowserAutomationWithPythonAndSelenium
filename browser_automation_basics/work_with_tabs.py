import time
import unittest
from selenium import webdriver
from browser_automation_basics.locators.test_page_locator import TestPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def first_automation():

    # Open web page
    opts = webdriver.ChromeOptions()
    opts.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=opts)

    driver.get(TestPageLocator.URL)
    WebDriverWait(driver, 10).until(EC.title_is(TestPageLocator.TITLE))
    driver.execute_script('window.open(\'https://techstepacademy.com/workshops\', \'_blank\');')
    driver.execute_script('window.open(\'https://techstepacademy.com\', \'_blank\');')
    driver.execute_script('window.open(\'https://techstepacademy.com/about\', \'_blank\');')
    driver.execute_script('window.open(\'https://techstepacademy.com/news\', \'_blank\');')

    unittest.TestCase().assertEqual(5, len(driver.window_handles))
    for i in range(len(driver.window_handles)):
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(2)

    time.sleep(1)
    driver.close()


if __name__ == '__main__':
    first_automation()
