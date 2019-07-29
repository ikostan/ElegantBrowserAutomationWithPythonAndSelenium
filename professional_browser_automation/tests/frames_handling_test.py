import unittest
import selenium
from selenium.common.exceptions import TimeoutException
from professional_browser_automation.elements.base_element import BaseElement
from professional_browser_automation.page_locators.training_ground_locator import TrainingGroundLocator
from professional_browser_automation.page_models.iframe_training_model import IFrameTrainingModel
from professional_browser_automation.page_context.iframe_training_context import IFrameTrainingContext
from professional_browser_automation.page_context.training_ground_context import TrainingGroundContext


class FramesHandlingTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.page = IFrameTrainingModel(selenium.webdriver.Chrome())
		cls.page.go()

	def test_url(self):
		self.assertEqual(IFrameTrainingContext.URL, self.page.page_url)

	def test_title(self):
		self.assertEqual(IFrameTrainingContext.TITLE, self.page.title)

	def test_switch_to_frame(self):
		# 1
		self.assertEqual(IFrameTrainingContext.PARAGRAPH, self.page.paragraph)

		# 2
		self.page.switch_to_iframe()
		with self.assertRaises(TimeoutException):
			self.page.paragraph

		# 3
		button = BaseElement(self.page.driver, TrainingGroundLocator.BUTTON_1)
		self.assertEqual(TrainingGroundContext.BUTTON_1, button.text)

		# 4
		self.page.switch_to_main_frame()
		self.assertEqual(IFrameTrainingContext.PARAGRAPH, self.page.paragraph)

		# 5
		with self.assertRaises(TimeoutException):
			button = BaseElement(self.page.driver, TrainingGroundLocator.BUTTON_1)

	@classmethod
	def tearDownClass(cls):
		cls.page.quit()


if __name__ == '__main__':
	unittest.main()
