from professional_browser_automation.elements.base_element import BaseElement
from professional_browser_automation.page_models.base_page_model import BasePageModel
from professional_browser_automation.page_context.trial_stones_context import TrialStonesContext
from professional_browser_automation.page_locators.trial_stones_page_locator import TrialStonesPageLocator


class TrialStonesModel(BasePageModel):

	_url = TrialStonesContext.URL
	expected_title = TrialStonesContext.TITLE

	@property
	def riddle_stone_button(self):
		'''
		Returns Button #1 object: Riddle of Stone
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.RIDDLE_ANSWER_BUTTON)

	@property
	def get_riddle_stone_field_text(self):
		'''
		Returns text from input field #1: Riddle of Stone
		:return:
		'''
		element = BaseElement(super().driver, TrialStonesPageLocator.RIDDLE_INPUT_FIELD).element
		return element.get_attribute('value')

	def type_into_riddle_stone_field(self, text):
		'''
		Type text into input field #1
		:param text:
		:return:
		'''
		element = BaseElement(super().driver, TrialStonesPageLocator.RIDDLE_INPUT_FIELD).element
		element.clear()
		element.send_keys(text)
		return None

	@property
	def is_password_visible(self):
		'''
		Returns is password value visible
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.PASSWORD).is_visible

	@property
	def password(self):
		'''
		Returns password value
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.PASSWORD).element.text

	@property
	def riddle_secrets_button(self):
		'''
		Returns Button #2 object: Riddle of Secrets
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.PASSWORD_ANSWER_BUTTON)

	@property
	def get_riddle_secrets_field_text(self):
		'''
		Returns text from input field #2: Riddle of Secrets
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.PASSWORD_INPUT_FIELD).value

	def type_into_riddle_secrets_field(self, text):
		'''
		Type text into input field #2: Riddle of Secrets
		:param text:
		:return:
		'''
		element = BaseElement(super().driver, TrialStonesPageLocator.PASSWORD_INPUT_FIELD).element
		element.clear()
		element.send_keys(text)
		return None

	@property
	def riddle_secrets_success(self):
		return BaseElement(super().driver, TrialStonesPageLocator.PASSWORD_SUCCESS).is_visible

	@property
	def riddle_merchants_button(self):
		'''
		Returns Button #3 object: The Two Merchants
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.RICHEST_MERCHANT_BUTTON)

	@property
	def get_riddle_merchants_field_text(self):
		'''
		Returns text from input field #3: The name of the richest merchant
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.RICHEST_MERCHANT_FIELD).value

	def type_into_riddle_merchants_field(self, text):
		'''
		Type text into input field #3: The name of the richest merchant
		:param text:
		:return:
		'''
		element = BaseElement(super().driver, TrialStonesPageLocator.RICHEST_MERCHANT_FIELD).element
		element.clear()
		element.send_keys(text)
		return None

	@property
	def jessica_wealth(self):
		'''
		Returns Jessica's total wealth
		:return:
		'''
		return int(BaseElement(super().driver, TrialStonesPageLocator.JESSICA_TOTAL_WEALTH).element.text)

	@property
	def bernard_wealth(self):
		'''
		Returns Bernard's total wealth
		:return:
		'''
		return int(BaseElement(super().driver, TrialStonesPageLocator.BERNARD_TOTAL_WEALTH).element.text)

	@property
	def jessica(self):
		'''
		Returns Jessica's name
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.JESSICA).element.text

	@property
	def bernard(self):
		'''
		Returns Bernard'sname
		:return:
		'''
		return BaseElement(super().driver, TrialStonesPageLocator.BERNARD).element.text

	@property
	def riddle_merchants_success(self):
		return BaseElement(super().driver, TrialStonesPageLocator.RICHEST_MERCHANT_SUCCESS).is_visible

	@property
	def is_trial_complete(self):
		return BaseElement(super().driver, TrialStonesPageLocator.TRIAL_COMPLETE).is_visible
