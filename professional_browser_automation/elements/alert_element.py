import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertElement:

	def __init__(self, driver: selenium.webdriver):

		self.driver = driver
		self.element = self._find()

	def _find(self):
		'''
		Returns element if located else raises TimeOut exception
		:return:
		'''
		WebDriverWait(self.driver, 10).until(EC.alert_is_present())
		return self.driver.switch_to.alert
