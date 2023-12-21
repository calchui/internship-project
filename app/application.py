from pages.main_page import MainPage
from pages.log_in_page import LogIn
from pages.search_results_page import SearchResult


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.log_in_page = LogIn(driver)
        self.search_results_page = SearchResult(driver)



