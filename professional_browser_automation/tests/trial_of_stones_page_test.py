import unittest
import selenium
from professional_browser_automation.page_models.trial_stones_model import TrialStonesModel
from professional_browser_automation.page_context.trial_stones_context import TrialStonesContext


class TrainingGroundTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.page = TrialStonesModel(selenium.webdriver.Chrome())
		cls.page.go()

	def test_url(self):
		self.assertEqual(TrialStonesContext.URL, self.page.url)

	def test_title(self):
		self.assertEqual(TrialStonesContext.TITLE, self.page.title)

	def test_riddle_stone(self):
		# 1
		self.assertFalse(self.page.is_password_visible)
		self.page.type_into_riddle_stone_field(TrialStonesContext.ANOTHER_WORD_FOR_STONE)
		self.assertEqual(TrialStonesContext.ANOTHER_WORD_FOR_STONE, self.page.get_riddle_stone_field_text)
		self.assertFalse(self.page.is_password_visible)
		# 2
		self.page.riddle_stone_button.click()
		# 3
		self.assertTrue(self.page.is_password_visible)
		self.assertEqual(TrialStonesContext.PASSWORD, self.page.password)

	def test_buttons_label(self):
		self.assertEqual(TrialStonesContext.BUTTON, self.page.riddle_stone_button.text)
		self.assertEqual(TrialStonesContext.BUTTON, self.page.riddle_secrets_button.text)
		self.assertEqual(TrialStonesContext.BUTTON, self.page.riddle_merchants_button.text)

	@classmethod
	def tearDownClass(cls):
		cls.page.quit()


if __name__ == '__main__':
	unittest.main()
