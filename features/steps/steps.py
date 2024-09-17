from behave import given, when, then
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os


#first run this command python setup_env.py for installation
#2nd ryn behave command

# Use apk_path in your setup when launching the app
# Dynamically get APK path from the apk directory
apk_path = os.path.join(os.getcwd(), "apk", "smmr1.apk")


@given('the app is launched')
def launch_app(context):
    try:
        options = UiAutomator2Options()
        options.platformName = "Android"
        options.platformVersion = "11.0"
        options.deviceName = "Redmi 9"
        options.noReset = True
        # options.app = "C:\\Users\\HK\\Downloads\\smmr1.apk"
        options.appPackage = "homeworkout.homeworkouts.noequipment"
        options.appActivity = "homeworkout.homeworkouts.noequipment.SplashActivity"
        options.udid = "97a606d80406"
        options.automationName = "UiAutomator2"
        options.newCommandTimeout = 120000

        context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    except Exception as e:
        print(f"Error launching app: {e}")
        raise

def click_next_button(context, button_text="NEXT", timeout=40): 
    try:
        next_button = WebDriverWait(context.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{button_text}"]'))
        )
        sleep(2)
        next_button.click()
        sleep(3)
    except Exception as e:
        print(f"Error clicking on '{button_text}' button: {e}")
        raise


@when('I navigate to the main page')
def navigate_to_main_page(context):
    try:
        element = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="I\'m Ready"]'))
        )
        element.click()
    except Exception as e:
        print(f"Error navigating to main page: {e}")
        raise

@when('I click on the Male button')
def click_male_button(context):
    try:
        male = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Male"]'))
        )
        male.click()
    except Exception as e:
        print(f"Error clicking on 'Male' button: {e}")
        raise

@then('I click on the next button')
def click_next_button(context):
    try:
        next_button = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button: {e}")
        raise

@when('I click on the Build Muscle button')
def click_build_muscle(context):
    try:
        muscle = WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                                     'android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/'
                                                     'android.view.View/android.view.View/android.view.View[1]/'
                                                     'android.widget.ScrollView/android.view.View[2]'))
        )
        sleep(2)
        muscle.click()
    except Exception as e:
        print(f"Error clicking on 'Build Muscle' button: {e}")
        raise

@then('I click the next button after Lose Weight')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@when('I select the body area')
def select_body_area(context):
    try:
        arm_button = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Arm"]'))
        )
        arm_button.click()
    except Exception as e:
        print(f"Error selecting 'Arm' button: {e}")
        raise

@then('I click the next button after selecting arm')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@when('I click on the next button after selecting Look more attractive')
def click_next_after_body_area(context):
    try:
        next_button = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Look more attractive"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after selecting body area: {e}")
        raise

@then('I click the next button after selecting Look more attractive')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@when('I click the button selecting DOB')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="2002"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@then('I click the next button after selecting DOB')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@then('I click the next button after selecting height')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@then('I click the next button after selecting current weight')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@then('I click the next button after selecting target weight')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        sleep(2)
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise
# @then('I click the next button after selecting target weight one')
# def click_next_after_lose_weight(context):
#     try:
#         next_button = WebDriverWait(context.driver, 40).until(
#             EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
#         )
#         # sleep(2)
#         next_button.click()
#         # sleep(5)
#     except Exception as e:
#         print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
#         raise


@then('I click the next button after selecting goal')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        # sleep(7)
        next_button.click()
        sleep(3)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@then('I click the next button after selecting body shape')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        # sleep(3)
        next_button.click()
        sleep(3)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@then('I click the next button after selecting target bodyshape')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        # sleep(1)
        next_button.click()
        sleep(4)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise

@then('I click the next button great start')
def tap_on_button(context):
    click_next_button(context)

@when('I click the button selecting workout')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="On the yoga mat"]'))
        )
        # sleep(5)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise   

@then('I click the next button after selecting workout')
def click_next_after_lose_weight(context):
    click_next_button(context)  

@when('I click the button excercise do you prefer')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="No Jumping"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise   

@then('I click the next button after selecting excercise')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise   

@when('I click the button Easy to start')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Easy to start"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise   

@then('I click the next button after selecting easy to start')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise  

@when('I click the button excercise Knee')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Knee"]'))
        )
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise   

@then('I click the next button after selecting Knee')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        next_button.click()
        sleep(3)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise   

# @when('I click the next button after selecting Kneeone')
# def click_next_after_lose_weight(context):
#     try:
#         next_button = WebDriverWait(context.driver, 40).until(
#             EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
#         )
#         next_button.click()
#     except Exception as e:
#         print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
#         raise  

@then('I click the next button after selecting Kneetwo')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        sleep(2)
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise    

@when('I click the button Beginner')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Beginner"]'))
        )
        sleep(2)
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise 

@then('I click the next button after selecting Beginner')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise 

@then('I click the next button after selecting Beginner1')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise     

@then('I click the next button after selecting Beginner2')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="NEXT"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise     

@when('I click the next button after selecting Beginner3')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Far from feet"]'))
        )
        sleep(2)
        next_button.click()
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise  

@then('I click the next button after selecting Beginner4')
def click_next_after_lose_weight(context):
    click_next_button(context)   

@when('I click the button Breathless')
def click_next_after_lose_weight(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Breathless"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise       
@then('I click the next button after selecting Beginner5')
def click_next_after_breathless(context):
    click_next_button(context)

@then('I click the next button after selecting Beginner6')
def click_one_more_next_after_selecting_begginner(context):
    click_next_button(context)

@when('I click the button Go travel')
def click_on_gotravel(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Go travel"]'))
        )
        # sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise  

@then('I click the next button after selecting go travel')
def click_nextbutton_on_go_travel(context):
    click_next_button(context)  

@when('I click the button full of energy')
def click_button_full_of_energy(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Full of energy"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise       

@then('I click the next button after selecting energy')
def click_next_after_selecting_energy(context):
    click_next_button(context) 

@then('I click the next button before get my plan') 
def click_next_before_get_my_plan(context):
    click_next_button(context)

@then('I click the button Get my plan')
def click_button_full_of_energy(context):
    try:
        next_button = WebDriverWait(context.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Get my plan"]'))
        )
        sleep(2)
        next_button.click()
        sleep(2)
    except Exception as e:
        print(f"Error clicking on 'NEXT' button after Lose Weight: {e}")
        raise  

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
