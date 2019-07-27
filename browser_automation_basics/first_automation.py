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

    # Click on Button1
    button_1 = page.get_button_1()
    button_1.click()

    # Working with alert
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions

    alert = WebDriverWait(page.driver, 10).until(expected_conditions.alert_is_present())
    unittest.TestCase().assertEqual('You clickedButton1.', alert.text)
    time.sleep(2)

    # Close alert and go back to main window
    alert.accept()

    # Working with drop down
    from selenium.webdriver.support.select import Select
    drop_down_menu_selector = Select(page.drop_down_menu)

    drop_down_menu_selector.select_by_value('third')
    unittest.TestCase().assertEqual(1, len(drop_down_menu_selector.all_selected_options))
    unittest.TestCase().assertEqual('third',
                                    drop_down_menu_selector.all_selected_options[0].get_property('value'))
    time.sleep(2)

    drop_down_menu_selector.select_by_value('second')
    unittest.TestCase().assertEqual(1, len(drop_down_menu_selector.all_selected_options))
    unittest.TestCase().assertEqual('second',
                                    drop_down_menu_selector.all_selected_options[0].get_property('value'))
    time.sleep(2)

    drop_down_menu_selector.select_by_value('first')
    unittest.TestCase().assertEqual(1, len(drop_down_menu_selector.all_selected_options))
    unittest.TestCase().assertEqual('first',
                                    drop_down_menu_selector.all_selected_options[0].get_property('value'))

    # Close web browser
    time.sleep(2)
    page.driver.close()
    if page.driver:
        page.driver.quit()


if __name__ == '__main__':
    first_automation()
