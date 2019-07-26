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
        '''
        Returns input field #1
        :return:
        '''
        return self.driver.find_element(*TestPageLocator.INPUT_FIELD_1)

    def get_button_1(self):
        '''
        Returns Button1 object
        :return:
        '''
        return self.driver.find_element(*TestPageLocator.BUTTON_1)

    @property
    def price_product_1(self):
        '''
        Returns price product #1
        :return:
        '''
        return self.driver.find_element(*TestPageLocator.PRICE_PRODUCT_1)

