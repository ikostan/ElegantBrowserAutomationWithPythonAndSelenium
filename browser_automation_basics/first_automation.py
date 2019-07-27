import time
import unittest
from selenium import webdriver
from browser_automation_basics.page_model.test_page_model import TestPage
from browser_automation_basics.locators.test_page_locator import TestPageLocator


def first_automation():

    # Open web page
    driver = webdriver.Chrome()
    wrong_url = 'https://google.com'
    page = TestPage(driver)
    page.driver.get(TestPageLocator.URL)

    # URL validation
    unittest.TestCase().assertNotEqual(page.url,
                                       wrong_url)

    # URL validation
    unittest.TestCase().assertEqual(page.url,
                                    TestPageLocator.URL)

    # Title validation
    unittest.TestCase().assertEqual(page.title,
                                    TestPageLocator.TITLE)

    # Test input field #1
    test_text = "some text"
    input_element = page.get_input_field_1()
    input_element.send_keys(test_text)
    unittest.TestCase().assertEqual(test_text,
                                    input_element.get_property('value'))

    # Test Product #1 price
    price_1 = page.price_product_1
    expected_price_1 = 'Price: $200'
    unittest.TestCase().assertEqual(expected_price_1,
                                    price_1.text,
                                    "\nError: price value is wrong\nExpected: {}\nActual: {}".format(expected_price_1,
                                                                                                     price_1.text))

    # Close web browser
    time.sleep(1)
    page.driver.close()
    if page.driver:
        page.driver.quit()


if __name__ == '__main__':
    first_automation()
