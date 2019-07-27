import time
import unittest
from selenium.webdriver.support.select import Select
from browser_automation_basics.utils.utils import open_web_page, close_web_page
from browser_automation_basics.locators.test_page_locator import TestPageLocator


def first_automation():

    # Open web page
    page = open_web_page(TestPageLocator.URL)

    # using the JavaScriptExecutor to scroll down to bottom of window
    page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

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
    close_web_page(page)


if __name__ == '__main__':
    first_automation()
