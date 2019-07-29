import selenium
from selenium.webdriver.support.wait import WebDriverWait
from professional_browser_automation.page_context.base_page_context import BasePageContext
from selenium.webdriver.support import expected_conditions as EC


class BasePageModel:

	url = BasePageContext.URL
	expected_title = BasePageContext.TITLE

	def __init__(self, driver: selenium.webdriver):
		self.driver = driver

	@property
	def title(self):
		'''
		Return web page title
		:return:
		'''
		return self.driver.title

	def go(self):
		'''
		Open test web page
		:return:
		'''
		self.driver.get(self.url)
		WebDriverWait(self.driver, 10).until(EC.title_contains(self.expected_title))
		return None

	def quit(self):
		'''
		Close webdriver
		:return:
		'''
		if self.driver:
			self.driver.quit()
		return None
