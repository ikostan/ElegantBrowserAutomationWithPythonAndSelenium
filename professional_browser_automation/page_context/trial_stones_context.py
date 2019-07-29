from professional_browser_automation.page_context.base_page_context import BasePageContext


class TrialStonesContext(BasePageContext):

	TITLE = 'Ninja Trials: Trial of the Stones — ' + BasePageContext.TITLE
	URL = BasePageContext.URL + '/trial-of-the-stones'
	BUTTON = "Answer"
	ANOTHER_WORD_FOR_STONE = 'rock'
	PASSWORD = 'bamboo'
	SUCCESS = 'Success!'
	JESSICA_TOTAL_WEALTH = 3000
	BERNARD_TOTAL_WEALTH = 2000
	JESSICA = 'Jessica'
	BERNARD = 'Bernard'
	CHECK_ANSWERS = 'Trial Complete'

