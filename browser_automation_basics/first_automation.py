from selenium import webdriver
import time
from browser_automation_basics.page_model.test_page_model import TestPage
from browser_automation_basics.locators.test_page_locator import TestPageLocator


def first_automation():

    driver = webdriver.Chrome()
    wrong_url = 'https://google.com'
    page = TestPage(driver)
    page.driver.get(TestPageLocator.URL)

    assert page.url != wrong_url
    assert page.url == TestPageLocator.URL
    assert page.title == TestPageLocator.TITLE

    time.sleep(2)
    page.driver.quit()


if __name__ == '__main__':
    first_automation()
