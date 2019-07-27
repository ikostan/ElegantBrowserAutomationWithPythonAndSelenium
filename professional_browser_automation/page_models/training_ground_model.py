from professional_browser_automation.page_models.base_page_model import BasePageModel
from professional_browser_automation.page_locators.training_ground_locator import TrainingGroundLocator


class TrainingGroundModel(BasePageModel):

	def __init__(self, driver):
		super().__init__(driver)

	def type_input_field_1(self, text):
		'''
		Type text inside input field #1
		:param text:
		:return:
		'''
		self.driver.find_element(*TrainingGroundLocator.INPUT_1).send_keys(text)

	def click_button_1(self):
		'''
		Click on Button 1
		:return:
		'''
		self.driver.find_element(*TrainingGroundLocator.Button_1).click()

