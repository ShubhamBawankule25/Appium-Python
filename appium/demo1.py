import pytest
import time
from appium.options.common import AppiumOptions
from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


capabilities = dict(
    platformName='Android',
    platformVersion='14',
    automationName='uiautomator2',
    deviceName='Pixel 7a',
    language='en',
    locale='US',
    unicodeKeyboard='false',
    resetKeyboard='false',
    unlockType='pin',
    unlockKey='1234'
)

appium_server_url= 'http://localhost:4723'




def setup_function(function):
    global driver
    driver = webdriver.Remote(appium_server_url,options=AppiumOptions().load_capabilities(caps=capabilities))
    driver.press_keycode(3)
    
    
    
def teardown_function(function):
    if driver:
    	driver.quit()



def test():
    el1 = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Chrome"]').click()
    driver.implicitly_wait(5)
    try:
        val = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="New tab"]').is_displayed()
        print ("value is:", val)
        if val: 
            driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="New tab"]').click()
            driver.implicitly_wait(2)
            driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]').click()
        else:
            driver.implicitly_wait(2)
            driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]').click()
            # driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.android.chrome:id/search_box"]').click()
    except NoSuchElementException: 
        print("element not found")
        
        
        
        
        
        
def test_gmail_app():
    # driver.flick(start_x=515, start_y=1207,end_x=515, end_y=723)
    driver.activate_app('com.google.android.gm')
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Compose"]').click()
    driver.implicitly_wait(2)
    # driver.keyevent(4)
    driver.implicitly_wait(2)
    driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.google.android.gm:id/peoplekit_autocomplete_chip_group"]/android.widget.EditText').send_keys('test')
    suggestions = list(driver.find_elements(AppiumBy.XPATH, '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.gm:id/peoplekit_autocomplete_results_recyclerview"]/android.widget.RelativeLayout'))
    print(suggestions)
    # driver.find_element(AppiumBy.LINK_TEXT, ("testng666@gmail.com")).click()
    # for _ in suggestions:
    #     assert _.get_attribute('text').__contains__('testng666@gmail.com')
    #     driver.find_element(AppiumBy.ANDROID_DATA_MATCHER('{text="has_text",args=["text", "testng666@gmail.com"]}'))
        

    
# def test2():
#     driver.flick(start_x=515, start_y=1207,end_x=515, end_y=723)
    
#     # driver.execute_script("mobile: scrollTo", {"element": destination})
    
#     # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable("true")).scrollintoview(new Uiselector().text("Gmail"))')
    
#     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ("new UiScrollable(new UiSelector()).scrollIntoView(text(\"Youtube\"))"))




def test_search_app():
    
    driver.flick(start_x=515, start_y=1207,end_x=515, end_y=723)
    el1 = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Search"]')
    el1.click()
    driver.implicitly_wait(2)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.google.android.apps.nexuslauncher:id/input"]').send_keys('Gmail')
    apps = list(driver.find_elements(AppiumBy.XPATH, "//android.widget.GridView[@resource-id='com.google.android.apps.nexuslauncher:id/search_results_list_view']/android.widget.TextView"))
    print(len(apps))
    for _ in apps:
        # if apps[i].
        assert _.get_attribute('content-desc').__contains__('Gmail')
        # driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Gmail"]').click()
    # driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Gmail"]').click()
    
    
    
    
    
def test_unlock_phone():
    if driver.is_locked():
        print("Device is locked")
        driver.implicitly_wait(2)
        driver.unlock()
        
        
        
    
def test_private_space_setup():
    
    try:
        driver.activate_app('com.android.settings')
        el1 = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout')
        while el1.is_displayed:
            driver.swipe(540, 2034, 540, 500, 800)
            driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/summary" and @text="App security, device lock, permissions"]').click()
            break
        
        el2 = driver.find_element(AppiumBy.XPATH, '	//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.permissioncontroller:id/recycler_view"]/android.widget.LinearLayout')
        while el2.is_displayed:
            driver.swipe(540, 2034, 540, 500, 800)
            driver.find_element(AppiumBy.XPATH, '	//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.permissioncontroller:id/recycler_view"]/android.widget.LinearLayout[9]').click()
            break
        
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.systemui:id/lockPassword"]').send_keys('1234')
        driver.press_keycode(66)
        
        # cancel = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Cancel"]')
        set_up = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Set up"]')
        
        set_up.click()
        time.sleep(5)
        
        
        use_screen_lock = driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.android.settings:id/sud_layout_template_content"]/android.widget.LinearLayout//android.widget.Button[@text="Use screen lock"]')
        # choose_new_lock = driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.android.settings:id/sud_layout_template_content"]/android.widget.LinearLayout//android.widget.Button[@text="Choose new lock"]')
        
        use_screen_lock.click()
        
        time.sleep(5)
        verify = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.settings:id/sud_layout_subtitle"]')
        assert verify.get_attribute('text').__contains__('To find your private space, go to your apps list then scroll down')
        
        
        done = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Done"]')
        done.click()
        
    except:
        NoSuchElementException
    
    
    
    
    
def test_close_recent_apps():
    
    driver.unlock()
    driver.implicitly_wait(2)
    driver.press_keycode(187)
    driver.implicitly_wait(2)

    try:
        
        el1 = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.google.android.apps.nexuslauncher:id/task"]')
    
        while el1.is_displayed():
            driver.flick(0, 1131, 1070, 1131)
            driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.apps.nexuslauncher:id/clear_all"]').click()            
            break
    except:
        NoSuchElementException
        
        
        

def test_private_space_from_search():
    time.sleep(3)
    driver.flick(start_x=515, start_y=1207,end_x=515, end_y=723)
    
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.google.android.apps.nexuslauncher:id/input"]').send_keys('private space')
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.google.android.apps.nexuslauncher:id/tile_label_group"]//android.widget.TextView').click()
    el1 = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.google.android.apps.nexuslauncher:id/ps_container_header"]')
    
    assert el1.get_attribute('text').__contains__('Private')
    print('On private space view')
    
    
    
    
    
def test_demo():
    driver.activate_app('com.android.settings')
    el1 = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout')
    while el1.is_displayed:
        driver.swipe(540, 2034, 540, 500, 800)
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/summary" and @text="App security, device lock, permissions"]').click()
        break
        
    el2 = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.permissioncontroller:id/recycler_view"]/android.widget.LinearLayout')
    while el2.is_displayed:
        driver.swipe(540, 2034, 540, 500, 800)
        driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.permissioncontroller:id/recycler_view"]/android.widget.LinearLayout[9]').click()
        break
        
    # driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.systemui:id/lockPassword"]').send_keys('1234')
    # driver.press_keycode(66)
    
    
    
    
def test_prvt():
    driver.activate_app('com.android.settings')
    # el1 = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView')
    # while True:
    #     driver.swipe(540, 2034, 540, 0, 800)
    #     if driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Security & privacy"]').is_displayed():
    #         driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Security & privacy"]').click()
    #         break            
            
    #     else: 
    #         driver.swipe(540, 2034, 540, 1034, 800)
            
    el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,("new UiScrollable(new UiSelector().scrollable(true)).setMaxSearchSwipes(10)" + ".scrollIntoView(new UiSelector().textContains(\"Security\"))"))
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Security & privacy"]').click()
    # el1.click()

