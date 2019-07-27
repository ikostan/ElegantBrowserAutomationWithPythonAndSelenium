from selenium.webdriver.common.by import By


class BasePageLocator:
	# Main url
	URL = 'https://techstepacademy.com'

	# Main title
	TITLE = (By.TAG_NAME, 'title')
	TITLE_CONTEXT = 'TechStep Academy'
