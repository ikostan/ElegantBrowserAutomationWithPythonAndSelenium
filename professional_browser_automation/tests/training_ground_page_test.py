import unittest
from professional_browser_automation.page_context.training_ground_context import TrainingGroundContext
from professional_browser_automation.page_models.training_ground_model import TrainingGroundModel
import selenium


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

	def test_alert_1(self):
		expected_alert_text = 'You clickedButton1.'
		self.page.click_button_1()
		self.assertEqual(expected_alert_text, self.page.alert_1_text)
		self.page.accept_alert_1()

	@classmethod
	def tearDownClass(cls):
		cls.page.quit()


if __name__ == '__main__':
	unittest.main()
