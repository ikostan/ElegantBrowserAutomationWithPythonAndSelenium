import unittest
import selenium
from professional_browser_automation.page_models.training_ground_model import TrainingGroundModel
from professional_browser_automation.page_context.training_ground_context import TrainingGroundContext


class TrainingGroundTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.page = TrainingGroundModel(selenium.webdriver.Chrome())
		cls.page.go()

	def test_url(self):
		self.assertEqual(TrainingGroundContext.URL, self.page.url)

	def test_title(self):
		self.assertEqual(TrainingGroundContext.TITLE, self.page.title)

	def test_input_field_1(self):
		expected_text = 'something here'
		self.page.type_into_input_field_1(expected_text)
		self.assertEqual(expected_text, self.page.get_input_field_1_text)

	def test_button_1(self):
		self.assertEqual(TrainingGroundContext.BUTTON_1, self.page.button_1.text)

	def test_alert_1(self):
		self.page.button_1.click()
		self.assertEqual(TrainingGroundContext.ALERT_1, self.page.alert_1_text)
		self.page.accept_alert_1()

	@classmethod
	def tearDownClass(cls):
		cls.page.quit()


if __name__ == '__main__':
	unittest.main()
