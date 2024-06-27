import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    platformVersion= 14,
    automationName='uiautomator2',
    deviceName='Pixel 7a',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://127.0.0.1:4723/'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


def setUp(funcion) -> None:
    global driver
    driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)

def test():
    driver.find_element(AppiumBy,'//android.widget.TextView[@content-desc="Chrome"]').click()

def tearDown() -> None:
    if driver:
        driver.quit()