from selenium import webdriver
import time
import unittest
from browser_automation_basics.page_model.test_page_model import TestPage
from browser_automation_basics.locators.test_page_locator import TestPageLocator


def first_automation():

    driver = webdriver.Chrome()
    wrong_url = 'https://google.com'
    page = TestPage(driver)
    page.driver.get(TestPageLocator.URL)

    unittest.TestCase().assertNotEqual(page.url, wrong_url)
    unittest.TestCase().assertEqual(page.url, TestPageLocator.URL)
    unittest.TestCase().assertEqual(page.title, TestPageLocator.TITLE)

    test_text = "some text"
    input_element = page.get_input_field_1()
    input_element.send_keys(test_text)
    unittest.TestCase().assertEqual(test_text, input_element.get_property('value'))

    price_1 = page.get_price_product_1()
    expected_price_1 = 'Price: $200'
    unittest.TestCase().assertEqual(expected_price_1,
                                    price_1.text,
                                    "\nError: price value is wrong\nExpected: {}\nActual: {}".format(expected_price_1,
                                                                                                     price_1.text))

    time.sleep(2)

    page.driver.close()
    if page.driver:
        page.driver.quit()


if __name__ == '__main__':
    first_automation()
