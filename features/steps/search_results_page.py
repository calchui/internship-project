from selenium.webdriver.common.by import By
from pages.base_page import Page
from behave import given, when, then


class SearchResult(Page):

    # CONNECT_THE_COMPANY = (By.CSS_SELECTOR, "a[href='/book-presentation'][class*='button-link-menu w-in']")
    # LINKS = (By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']")


    @then('Verify {expected_amount} options')
    def verify_11_links(context, expected_amount):
        expected_amount = int(expected_amount)
        links = context.driver.find_elements(By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']")
        assert len(links) == expected_amount, f'Expected {expected_amount} links, but got {len(links)}'


    @then('Verify Connect the company')
    def verify_connect(context):
        expected_value = 'Connect the company'
        # actual_value = context.driver.find_element(By.CSS_SELECTOR, "a[href='/book-presentation'][class*='button-link-menu w-in']").text
        actual_value = context.driver.find_element(By.LINK_TEXT, "Connect the company").text
        assert expected_value == actual_value, f'{expected_value} is not equal to {actual_value}'


    ##################  MOBILE TESTING  : LOCATORS used for CONNECT THE COMPANY             ##################
    #     actual_value = context.driver.find_element(By.CSS_SELECTOR, ".get-free-period.menu:contains('Connect the company')").text
    #
    #     # actual_value = context.driver.find_element(By.XPATH, "div[text()='Connect the company']").text
    #                                                  (By.XPATH, "//div[text()='Connect the company']")
    #                                                  (By.XPath, "//*[@class='button-link-menu w-inline-block'][1]")

    ###################################################

