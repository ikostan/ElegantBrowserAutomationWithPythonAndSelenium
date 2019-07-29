import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element:

	def __init__(self, driver: selenium.webdriver, locator: tuple):

		self.driver = driver
		self.locator = locator
		self.element = self._find()

	def _find(self):
		'''
		Returns element if located else raises TimeOut exception
		:return:
		'''
		return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locator))

