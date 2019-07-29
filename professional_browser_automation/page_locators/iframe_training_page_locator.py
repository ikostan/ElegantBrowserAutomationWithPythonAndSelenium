from selenium.webdriver.common.by import By


class IFrameTrainingPageLocator:

    TITLE = (By.TAG_NAME, 'title')
    IFRAME = (By.XPATH, '//*[@id="block-yui_3_17_2_1_1564338258424_5429"]/div/iframe')
    PARAGRAPH = (By.XPATH, '//*[@id="block-5d3de848045889000188d389"]/div/p')
