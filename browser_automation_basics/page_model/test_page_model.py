from browser_automation_basics.locators.test_page_locator import TestPageLocator

class TestPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        '''
        Returns web page url
        :return:
        '''
        return self.driver.current_url

    @property
    def title(self):
        '''
        Returns <title> element
        :return:
        '''
        return self.driver.title

    def get_input_field_1(self):
        return self.driver.find_element(*TestPageLocator.INPUT_FIELD_1)

