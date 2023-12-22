from selenium.webdriver.common.by import By
from pages.base_page import Page
from behave import given, when, then


class SearchResult(Page):

    # CONNECT_THE_COMPANY = (By.CSS_SELECTOR, "a[href='/book-presentation'][class*='button-link-menu w-in']")
    # LINKS = (By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']")

    @then('Verify Connect the company')
    def verify_connect(context):
        expected_value = 'Connect the company'
        actual_value = context.driver.find_element(By.CSS_SELECTOR, "[href='/book-presentation'][class*='button-link-menu w-in']").text

        assert expected_value == actual_value, f'{expected_value} is not equal to {actual_value}'

    @then('Verify 11 options')
    def verify_11_links(context):
        context.driver.find_elements(By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']")
        links = context.driver.find_elements(By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']")

        assert len(links) == 11, f'Expected links should be 11, but found {len(links)}'