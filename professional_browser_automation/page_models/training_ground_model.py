from professional_browser_automation.elements.base_element import BaseElement
from professional_browser_automation.elements.alert_element import AlertElement
from professional_browser_automation.page_models.base_page_model import BasePageModel
from professional_browser_automation.page_locators.training_ground_locator import TrainingGroundLocator
from professional_browser_automation.page_context.training_ground_context import TrainingGroundContext


class TrainingGroundModel(BasePageModel):

	_url = TrainingGroundContext.URL
	expected_title = TrainingGroundContext.TITLE

	@property
	def button_1(self):
		'''
		Returns Button #1 object
		:return:
		'''
		return BaseElement(self.driver, TrainingGroundLocator.Button_1)

	@property
	def alert_1_text(self):
		'''
		Return text from Alert #1
		:return:
		'''
		alert = AlertElement(self.driver).element
		return alert.text

	def accept_alert_1(self):
		'''
		Accept Alert #1
		:return:
		'''
		alert = AlertElement(self.driver).element
		alert.accept()
		return None

	@property
	def get_input_field_1_text(self):
		'''
		Returns text from input field #1
		:return:
		'''
		return BaseElement(self.driver, TrainingGroundLocator.INPUT_1).value

	def type_into_input_field_1(self, text):
		'''
		Type text into input field #1
		:param text:
		:return:
		'''
		element = BaseElement(self.driver, TrainingGroundLocator.INPUT_1).element
		element.clear()
		element.send_keys(text)
		return None

