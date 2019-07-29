import unittest
import selenium
from professional_browser_automation.page_models.iframe_training_model import IFrameTrainingModel
from professional_browser_automation.page_context.iframe_training_context import IFrameTrainingContext


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
		pass

	@classmethod
	def tearDownClass(cls):
		cls.page.quit()


if __name__ == '__main__':
	unittest.main()
