import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element:

	def __init__(self, driver: selenium.webdriver, locator: tuple):

		self._driver = driver
		self._locator = locator
		self._element = self._find()

	def _find(self):
		'''
		Returns element if located else raises TimeOut exception
		:return:
		'''
		return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(self._locator))

	@property
	def element(self):
		return self._element

	@property
	def driver(self):
		return self._driver

	@property
	def locator(self):
		return self._locator
