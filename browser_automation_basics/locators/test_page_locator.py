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
    INPUT_FIELD_1 = (By.CSS_SELECTOR, 'input[id=\'ipt1\']')
    INPUT_FIELD_2 = (By.ID, 'ipt2')

    # Drop down list
    DROP_DOWN = (By.ID, 'sel1')
