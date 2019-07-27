import unittest
from professional_browser_automation.page_context.training_ground_context import TrainingGroundContext
from professional_browser_automation.page_models.training_ground_model import TrainingGroundModel
import selenium


class TrainingGroundTestCase(unittest.TestCase):

	def setUp(self):
		self.page = TrainingGroundModel(selenium.webdriver.Chrome())
		self.page.go()

	def test_basics(self):

		self.assertEqual(TrainingGroundContext.URL, self.page.url)
		self.assertEqual(TrainingGroundContext.TITLE, self.page.title)

	def tearDown(self):
		self.page.quit()


if __name__ == '__main__':
	unittest.main()
