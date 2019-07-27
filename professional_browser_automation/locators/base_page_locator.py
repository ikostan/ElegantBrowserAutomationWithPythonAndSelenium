from selenium.webdriver.common.by import By


class BasePageLocator:

	TITLE = (By.TAG_NAME, 'title')
	LOGO = (By.XPATH, '//*[@id="lower-logo"]/h1/a')
