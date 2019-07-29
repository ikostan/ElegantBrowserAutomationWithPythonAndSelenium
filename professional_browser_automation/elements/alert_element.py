import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertElement:

	def __init__(self, driver: selenium.webdriver):

		self._driver = driver
		self._element = self._find()

	def _find(self):
		'''
		Returns element if located else raises TimeOut exception
		:return:
		'''
		WebDriverWait(self._driver, 10).until(EC.alert_is_present())
		return self._driver.switch_to.alert

	@property
	def text(self):
		'''
		Returns text
		:return:
		'''
		return self._element.text

	def accept(self):
		'''
		Close alert
		:return:
		'''
		self._element.accept()
		return None
