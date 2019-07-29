from professional_browser_automation.elements.frame_element import FrameElement
from professional_browser_automation.page_models.base_page_model import BasePageModel
from professional_browser_automation.page_locators.iframe_training_page_locator import IFrameTrainingPageLocator
from professional_browser_automation.page_context.iframe_training_context import IFrameTrainingContext


class TrainingGroundModel(BasePageModel):

	url = IFrameTrainingContext.URL
	expected_title = IFrameTrainingContext.TITLE

	@property
	def switch_to_iframe(self):
		self.driver.switch_to(FrameElement(self.driver, IFrameTrainingPageLocator.IFRAME).element)

