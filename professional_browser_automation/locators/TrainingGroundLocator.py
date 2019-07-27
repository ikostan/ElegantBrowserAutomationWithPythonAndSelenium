from professional_browser_automation.locators.base_page_locator import BasePageLocator
from selenium.webdriver.common.by import By


class TrainingGroundLocator(BasePageLocator):

	URL = BasePageLocator.URL + '/training-ground'
	TITLE_CONTEXT = 'Training Ground — ' + BasePageLocator.TITLE_CONTEXT
	
