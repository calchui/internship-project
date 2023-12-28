from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


# def browser_init(context):
def browser_init(context, scenario_name="User can go to settings and see the right number of UI elements"):  # add scenario_name if you want to use it in Browserstack
    """
    :param context: Behave context
    # """

    # CHROME
    # driver_path = ChromeDriverManager().install()
    # service = Service(executable_path=r'C:\Users\edc_p\Downloads\internship-project\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)

    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    # FIRE FOX
    # service = Service(executable_path='./geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(executable_path=r'C:\Users\edc_p\Downloads\internship-project\chromedriver.exe')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )
    #
    # ############PUT BIGGER WINDOW SIZE WHEN RUNNING HEADLESS TO SEE ALL WEBPAGE TO SEARCH FOR ELEMENTS###########
    # context.driver.set_window_size(1280, 1280)
    # # context.driver.maximize_window()
    # context.app = Application(context.driver)


    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'calvinchui_KznApV'
    bs_key = 'jnsDt2A5reBRUdpQEGoX'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {

#######         WINDOWS               #############
        'os': 'windows',
        'osVersion': '11',
        'browserName': 'Chrome',
        'sessionName': scenario_name

#######         MAC                 #############
        # "os": "OS X",
        # "osVersion": "Sonoma",
        # "browserName": "Chrome",
        # "browserVersion": "latest",
        # "sessionName": scenario_name

        # "os": "OS X",
        # "osVersion": "Monterey",
        # "browserName": "Firefox",
        # "browserVersion": "latest",
        # "sessionName": scenario_name
        }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
