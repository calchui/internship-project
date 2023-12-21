from time import sleep
from pages.base_page import Page

class MainPage(Page):
    def open_reelly(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(2)
        self.driver.refresh()
