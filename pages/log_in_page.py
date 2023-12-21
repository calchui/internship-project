from selenium.webdriver.common.by import By
from pages.base_page import Page


class LogIn(Page):

    EMAIL = (By.CSS_SELECTOR, "[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "[type='password']")
    CLICK_CONTINUE = (By.CSS_SELECTOR, "[class='login-button w-button']")
    SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'][class*='menu-button-block']")

    def input_info(self):
        self.input_text('cal_chui@yahoo.com', *self.EMAIL)
        self.input_text('Careerist1234', *self.PASSWORD)
        self.click(*self.CLICK_CONTINUE)


    def click_settings(self):
        self.click(*self.SETTINGS)