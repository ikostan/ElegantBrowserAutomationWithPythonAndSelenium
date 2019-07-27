import time
import unittest
from selenium import webdriver
from browser_automation_basics.page_model.test_page_model import TestPage
from browser_automation_basics.locators.test_page_locator import TestPageLocator
from selenium.webdriver.support.select import Select


def first_automation():

    # Open web page
    driver = webdriver.Chrome()
    wrong_url = 'https://google.com'
    page = TestPage(driver)
    page.driver.get(TestPageLocator.URL)

    # using the JavaScriptExecutor to scroll down to bottom of window
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Working with drop down
    drop_down_menu_selector = Select(page.drop_down_menu)
    unittest.TestCase().assertEqual(3,
                                    len(drop_down_menu_selector.options))
    unittest.TestCase().assertListEqual(['Bears', 'Beets', 'Battlestar Galactica'],
                                        [element.text for element in drop_down_menu_selector.options])

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
    time.sleep(1)
    page.driver.close()
    if page.driver:
        page.driver.quit()


if __name__ == '__main__':
    first_automation()
