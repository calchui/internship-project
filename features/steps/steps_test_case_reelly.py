# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# EMAIL = (By.CSS_SELECTOR, "[type='email']")
# PASSWORD = (By.CSS_SELECTOR, "[type='password']")
# CLICK_CONTINUE = (By.CSS_SELECTOR, "[class='login-button w-button']")
# SETTINGS = (By.CSS_SELECTOR, "a[href='/settings'][class*='menu-button-block']")
# CONNECT_THE_COMPANY = (By.CSS_SELECTOR, "a[href='/book-presentation'][class*='button-link-menu w-in']")
# LINKS = (By.CSS_SELECTOR, "[class='page-setting-block w-inline-block']")
#
#
# @given('Open Reelly webpage')
# def open_reelly(context):
#     context.driver.get('https://soft.reelly.io/')
#     sleep(2)
#
#
# @when('Log into page')
# def login(context):
#     context.driver.find_element(*EMAIL).send_keys('cal_chui@yahoo.com')
#     context.driver.find_element(*PASSWORD).send_keys('Careerist1234')
#     context.driver.find_element(*CLICK_CONTINUE).click()
#     sleep(5)
#
# @then('Click on settings option')
# def click_settings(context):
#     context.driver.find_element(*SETTINGS).click()
#     sleep(2)
#
#
# @then('Verify Connect the company')
# def verify_connect(context):
#     expected_value = 'Connect the company'
#     actual_value = context.driver.find_element(*CONNECT_THE_COMPANY).text
#
#     assert expected_value == actual_value, f'{expected_value} is not equal to {actual_value}'
#
#
# @then('Verify 11 options')
# def verify_11_links(context):
#     context.driver.find_elements(*LINKS)
#     links = context.driver.find_elements(*LINKS)
#
#     assert len(links) == 11, f'Expected links should be 11, but found {len(links)}'