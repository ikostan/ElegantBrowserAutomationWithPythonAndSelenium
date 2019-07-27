from selenium import webdriver
from browser_automation_basics.page_model.test_page_model import TestPage


def open_web_page(url):
    # Open web page
    driver = webdriver.Chrome()
    page = TestPage(driver)
    page.driver.get(url)
    return page


def close_web_page(page):
    # Close web browser
    page.driver.close()
    if page.driver:
        page.driver.quit()

