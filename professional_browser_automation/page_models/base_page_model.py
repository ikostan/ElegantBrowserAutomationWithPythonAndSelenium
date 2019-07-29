import selenium
from selenium.webdriver.support.wait import WebDriverWait
from professional_browser_automation.page_context.base_page_context import BasePageContext
from selenium.webdriver.support import expected_conditions as EC


class BasePageModel:

	_url = BasePageContext.URL
	expected_title = BasePageContext.TITLE

	def __init__(self, driver: selenium.webdriver):
		self._driver = driver

	@property
	def driver(self):
		'''
		Returns web driver
		:return:
		'''
		return self._driver

	@property
	def page_url(self):
		'''
		Returns page current url
		:return:
		'''
		return self._driver.current_url

	@property
	def title(self):
		'''
		Return web page title
		:return:
		'''
		return self._driver.title

	def go(self):
		'''
		Open test web page
		:return:
		'''
		self._driver.get(self._url)
		WebDriverWait(self._driver, 10).until(EC.title_contains(self.expected_title))
		return None

	def quit(self):
		'''
		Close webdriver
		:return:
		'''
		if self._driver:
			self._driver.quit()
		return None
