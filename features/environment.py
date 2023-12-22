from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

def browser_init(context):
    """
    :param context: Behave context
    # """

                        #CHROME
    # driver_path = ChromeDriverManager().install()
    # service = Service(executable_path=r'C:\Users\edc_p\Downloads\internship-project\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)

    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)


                        #FIRE FOX
    # service = Service(executable_path=r'C:\Users\edc_p\Downloads\internship-project\geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)
    # context.driver.quit()


                    ## HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    service = Service(executable_path=r'C:\Users\edc_p\Downloads\internship-project\chromedriver.exe')
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )

    ############PUT BIGGER WINDOW SIZE WHEN RUNNING HEADLESS TO SEE ALL WEBPAGE TO SEARCH FOR ELEMENTS###########
    context.driver.set_window_size(1280, 1280)
    # context.driver.maximize_window()
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
