from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'][class*='menu-button-block']")
# CONNECT_THE_COMPANY = (By.CSS_SELECTOR, "[href='/book-presentation'][class*='button-link-menu w-in']")
# LINKS = (By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']")

@given('Open Reelly webpage')
def open_reelly(context):
    #context.driver.get('https://soft.reelly.io/')
    context.app.main_page.open_reelly()
    sleep(2)


@when('Log into page')
def login(context):
    # context.driver.find_element(*EMAIL).send_keys('cal_chui@yahoo.com')
    # context.driver.find_element(*PASSWORD).send_keys('Careerist1234')
    # context.driver.find_element(*CLICK_CONTINUE).click()
    context.app.log_in_page.input_info()
    # login = WebDriverWait(context.driver, 20).until(
    #     EC.element_to_be_clickable(CLICK_CONTINUE)
    # )
    # login.click()


@then('Click on settings option')
def click_settings(context):
    # context.driver.find_element(*SETTINGS).click()
    # context.app.log_in_page.click_settings()
    # sleep(3)
    setting = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable(SETTINGS)
    )
    setting.click()

# @then('Verify Connect the company')
# def verify_connect(context):
#     # expected_value = 'Connect the company'
#     # actual_value = context.driver.find_element(*CONNECT_THE_COMPANY).text
#     #
#     # assert expected_value == actual_value, f'{expected_value} is not equal to {actual_value}'
#     context.app.search_result_page.verify_connect()
#
# @then('Verify 11 options')
# def verify_11_links(context):
#     # context.driver.find_elements(*LINKS)
#     # links = context.driver.find_elements(*LINKS)
#     #
#     # assert len(links) == 11, f'Expected links should be 11, but found {len(links)}'
#     context.app.search_result_page.verify_11_links()
