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

	def test_riddle_of_stone(self):
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

	def test_riddle_of_secret(self):
		# 1
		self.assertFalse(self.page.riddle_secrets_success)
		self.page.type_into_riddle_secrets_field(TrialStonesContext.PASSWORD)
		self.assertEqual(TrialStonesContext.PASSWORD, self.page.get_riddle_secrets_field_text)
		self.assertFalse(self.page.riddle_secrets_success)
		# 2
		self.page.riddle_secrets_button.click()
		# 3
		self.assertTrue(self.page.riddle_secrets_success)

	def test_riddle_of_merchants(self):
		# 1
		self.assertFalse(self.page.riddle_merchants_success)
		self.assertEqual(TrialStonesContext.JESSICA_TOTAL_WEALTH, self.page.jessica_wealth)
		self.assertEqual(TrialStonesContext.BERNARD_TOTAL_WEALTH, self.page.bernard_wealth)

		merchant = self.page.jessica \
			if self.page.jessica_wealth > self.page.bernard_wealth \
			else self.page.bernard

		self.page.type_into_riddle_merchants_field(merchant)
		self.assertEqual(TrialStonesContext.JESSICA, self.page.get_riddle_merchants_field_text)
		self.assertFalse(self.page.riddle_merchants_success)
		# 2
		self.page.riddle_merchants_button.click()
		# 3
		self.assertTrue(self.page.riddle_merchants_success)

	def test_buttons_label(self):
		self.assertEqual(TrialStonesContext.BUTTON, self.page.riddle_stone_button.text)
		self.assertEqual(TrialStonesContext.BUTTON, self.page.riddle_secrets_button.text)
		self.assertEqual(TrialStonesContext.BUTTON, self.page.riddle_merchants_button.text)

	@classmethod
	def tearDownClass(cls):
		cls.page.quit()


if __name__ == '__main__':
	unittest.main()
