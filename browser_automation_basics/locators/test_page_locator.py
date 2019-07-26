from selenium.webdriver.common.by import By


class TestPageLocator:

    URL = 'https://techstepacademy.com/training-ground'
    TITLE = 'Training Ground — TechStep Academy'

    PAGE_TITLE = (By.XPATH, '//*[@id="lower-logo"]/h1/a')
    PARAGRAPH = (By.XPATH, '//*[@id="block-ec928cee802cf918d26c"]/div/p')

    # Buttons
    BUTTON_1 = (By.ID, 'b1')
    BUTTON_2 = (By.ID, 'b2')
    BUTTON_3 = (By.ID, 'b3')
    BUTTON_4 = (By.ID, 'b4')

    # Input Fields
    # There are situation when you can’t use a single attribute value to select a web element.
    # In such situations, we can use a combination of  attributes to find the web element like:
    INPUT_FIELD_1 = (By.CSS_SELECTOR, 'input[id=\'ipt1\'][name=\'Input 1\']')
    INPUT_FIELD_2 = (By.ID, 'ipt2')

    # Drop down list
    DROP_DOWN = (By.ID, 'sel1')

    # Price List
    PRICE_PRODUCT_1 = (By.XPATH, '//b[text()="Product 1"]/../../p')

