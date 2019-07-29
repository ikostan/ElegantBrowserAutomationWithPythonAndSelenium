from selenium.webdriver.common.by import By


class TrialStonesPageLocator:

    TITLE = (By.TAG_NAME, 'title')
    IFRAME = (By.XPATH, '//*[@id="block-yui_3_17_2_1_1564338258424_5429"]/div/iframe')
