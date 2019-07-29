from professional_browser_automation.elements.frame_element import FrameElement
from professional_browser_automation.page_models.base_page_model import BasePageModel
from professional_browser_automation.page_locators.iframe_training_page_locator import IFrameTrainingPageLocator
from professional_browser_automation.page_context.iframe_training_context import IFrameTrainingContext


class IFrameTrainingModel(BasePageModel):

	_url = IFrameTrainingContext.URL
	expected_title = IFrameTrainingContext.TITLE

	def switch_to_iframe(self):
		super().driver.switch_to.frame(FrameElement(self.driver, IFrameTrainingPageLocator.IFRAME).iframe)
		return None

	def switch_to_main_frame(self):
		super().driver.switch_to.default_content()
		return None



