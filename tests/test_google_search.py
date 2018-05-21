from views.google_search import GoogleSearch
from selt.base_test import BaseTest


class TestGoogleSearch(BaseTest):
    def __init__(self, browser):
        self.name = "TestGoogleSearch"
        super(TestGoogleSearch, self).__init__(browser)

    def test_google_search(self, search_term="cats"):
        """
        Polarion ID #: Verify the user can search on google.
        :return:
        """
        google_search_view = GoogleSearch(self.driver)
        self.driver.get(google_search_view.url)
        google_search_view.google_search(search_term)

