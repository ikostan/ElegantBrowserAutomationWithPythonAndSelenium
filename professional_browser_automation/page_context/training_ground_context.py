from professional_browser_automation.page_context.base_page_context import BasePageContext


class TrainingGroundContext(BasePageContext):

	TITLE = 'Training Ground — ' + BasePageContext.TITLE
	URL = BasePageContext.URL + '/training-ground'
	BUTTON_1 = "Button1"
	ALERT_1 = 'You clickedButton1.'

