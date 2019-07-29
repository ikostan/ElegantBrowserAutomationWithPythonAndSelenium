from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from professional_browser_automation.elements.element import Element


class BaseElement(Element):

	def click(self):
		'''
		Wait until element becomes to be clickable and then click on it
		:return:
		'''
		WebDriverWait(super().driver, 10).until(EC.element_to_be_clickable(super().locator))
		super().element.click()
		return None

	@property
	def text(self):
		'''
		Return text from web element
		:return:
		'''
		return super().element.text

	@property
	def value(self):
		'''
		Return text from web element
		:return:
		'''
		return super().element.get_attribute('value')

	@property
	def is_visible(self):
		'''
		Returns 'is element visible' property value
		:return:
		'''
		return super().element.is_displayed()
