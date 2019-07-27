import time
from selenium import webdriver
from browser_automation_basics.locators.test_page_locator import TestPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def first_automation():

    # Open web page
    opts = webdriver.ChromeOptions()
    opts.add_argument('--disable-gpu')
    driver_1 = webdriver.Chrome(options=opts)
    driver_2 = webdriver.Chrome(options=opts)

    driver_1.get(TestPageLocator.URL)
    WebDriverWait(driver_1, 10).until(EC.title_is(TestPageLocator.TITLE))
    time.sleep(1)

    driver_2.get('https://www.google.com/')
    WebDriverWait(driver_2, 10).until(EC.title_contains('Google'))
    time.sleep(1)

    driver_2.close()
    driver_1.close()


if __name__ == '__main__':
    first_automation()
