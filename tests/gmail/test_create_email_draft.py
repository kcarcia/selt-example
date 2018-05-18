from views.google_login import GoogleLogin
from views.google_search import GoogleSearch
from views.gmail_dashboard import GmailDashboard
from base_test import BaseTest


class TestCreateEmailDraft(BaseTest):
    def __init__(self, browser):
        self.name = "TestCreateEmailDraft"
        super(TestCreateEmailDraft, self).__init__(browser)

    def test_create_email_draft(self):
        """
        Polarion ID #: Verify the user create an email draft.
        :return:
        """
        login_view = GoogleLogin(self.driver)
        google_search_view = GoogleSearch(self.driver)
        gmail_dashboard = GmailDashboard(self.driver)

        login_view.google_login()
        google_search_view.open_google_app("gmail")
        gmail_dashboard.compose_email()
