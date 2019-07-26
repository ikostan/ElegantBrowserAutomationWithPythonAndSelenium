from trial_of_the_stones.locators.page_locator import PageLocator


class PageModel:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        return self.driver.get(PageLocator.URL)

    def close(self):
        self.driver.close()
        if self.driver:
            self.driver.quit()

    @property
    def riddle_of_stone_field(self):
        return self.driver.find_element(*PageLocator.RIDDLE_INPUT_FIELD)

    @property
    def password_field(self):
        return self.driver.find_element(*PageLocator.PASSWORD_INPUT_FIELD)

    @property
    def riddle_of_stone_button(self):
        return self.driver.find_element(*PageLocator.RIDDLE_ANSWER_BUTTON)

    @property
    def password_answer_button(self):
        return self.driver.find_element(*PageLocator.PASSWORD_ANSWER_BUTTON)

    @property
    def password(self):
        return self.driver.find_element(*PageLocator.PASSWORD)

    @property
    def password_success(self):
        return self.driver.find_element(*PageLocator.PASSWORD_SUCCESS)

    @property
    def jessica_wealth(self):
        return self.driver.find_element(*PageLocator.JESSICA_TOTAL_WEALTH).text.strip()

    @property
    def bernard_wealth(self):
        return self.driver.find_element(*PageLocator.BERNARD_TOTAL_WEALTH).text.strip()

    @property
    def jessica_name(self):
        return self.driver.find_element(*PageLocator.JESSICA).text.strip()

    @property
    def bernard_name(self):
        return self.driver.find_element(*PageLocator.BERNARD).text.strip()

    @property
    def richest_merchant_field(self):
        return self.driver.find_element(*PageLocator.RICHEST_MERCHANT_FIELD)

    @property
    def richest_merchant_button(self):
        return self.driver.find_element(*PageLocator.RICHEST_MERCHANT_BUTTON)

    @property
    def merchant_success(self):
        return self.driver.find_element(*PageLocator.RICHEST_MERCHANT_SUCCESS)

    @property
    def check_answers_button(self):
        return self.driver.find_element(*PageLocator.CHECK_ANSWERS_BUTTON)

    @property
    def trial_complete(self):
        return self.driver.find_element(*PageLocator.TRIAL_COMPLETE)

