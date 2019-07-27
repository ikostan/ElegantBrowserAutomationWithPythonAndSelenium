from professional_browser_automation.page_models.base_page_model import BasePageModel
from professional_browser_automation.page_locators.training_ground_locator import TrainingGroundLocator
from professional_browser_automation.page_context.training_ground_context import TrainingGroundContext
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrainingGroundModel(BasePageModel):

	def __init__(self, driver):
		super().__init__(driver)
		self.url = TrainingGroundContext.URL

	def go(self):
		'''
		Open test web page
		:return:
		'''
		self.driver.get(self.url)
		WebDriverWait(self.driver, 10).until(EC.title_contains(TrainingGroundContext.TITLE))
		return None

	def quit(self):
		'''
		Close webdriver
		:return:
		'''
		if self.driver:
			self.driver.quit()

	@property
	def title(self):
		'''
		Return web page title
		:return:
		'''
		return self.driver.title

	@property
	def get_input_field_1_text(self):
		'''
		Returns text from input field #1
		:return:
		'''
		return self.driver.find_element(*TrainingGroundLocator.INPUT_1).get_attribute('value')

	def type_into_input_field_1(self, text):
		'''
		Type text into input field #1
		:param text:
		:return:
		'''
		input_field_1 = self.driver.find_element(*TrainingGroundLocator.INPUT_1)
		input_field_1.clear()
		input_field_1.send_keys(text)
		return None

	def click_button_1(self):
		'''
		Click on Button #1
		:return:
		'''
		self.driver.find_element(*TrainingGroundLocator.Button_1).click()
		return None

