from selenium.webdriver.common.by import By


class PageLocator:

    URL = 'https://techstepacademy.com/trial-of-the-stones'
    TITLE = (By.TAG_NAME, 'title')

    RIDDLE_INPUT_FIELD = (By.ID, 'r1Input')
    RIDDLE_ANSWER_BUTTON = (By.ID, 'r1Btn')

    PASSWORD_INPUT_FIELD = (By.ID, 'r2Input')
    PASSWORD_ANSWER_BUTTON = (By.ID, 'r2Butn')
    PASSWORD = (By.XPATH, '//*[@id="passwordBanner"]/h4')
    PASSWORD_SUCCESS = (By.XPATH, '//*[@id="successBanner1"]/h4')

    JESSICA_TOTAL_WEALTH = (By.XPATH, '//b[text()=\'Jessica\']/../../p')
    JESSICA = (By.XPATH, '//b[text()=\'Jessica\']')

    BERNARD_TOTAL_WEALTH = (By.XPATH, '//b[text()=\'Bernard\']/../../p')
    BERNARD = (By.XPATH, '//b[text()=\'Bernard\']')

    RICHEST_MERCHANT_FIELD = (By.ID, 'r3Input')
    RICHEST_MERCHANT_BUTTON = (By.ID, 'r3Butn')
    RICHEST_MERCHANT_SUCCESS = (By.XPATH, '//*[@id="successBanner2"]/h4')

    CHECK_ANSWERS_BUTTON = (By.ID, 'checkButn')
    TRIAL_COMPLETE = (By.XPATH, '//*[@id="trialCompleteBanner"]/h4')

