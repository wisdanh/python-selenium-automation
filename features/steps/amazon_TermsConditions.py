
from selenium.webdriver.support import expected_conditions as ec
from behave import when, given, then
from selenium.webdriver.common.by import By



#wait = WebDriverWait(driver, 10)

@given('Open Amazon T&C page')
def open_amazon_product(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")

@given('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@when('Click on Amazon Privacy Notice link')
def privacy_link(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(ec.new_window_is_opened)
    current_window = context.driver.window_handles
    print(current_window)
    context.driver.switch_to.window(current_window[1])

@then('Verify Amazon Privacy Notice page is opened')
def verify_Privacy_openened(context):
    context.driver.wait.until(ec.url_contains('https://www.amazon.com/gp/help/'))

@then('User can close new window')
def close_window(context):
    context.driver.close()
    current_window = context.driver.window_handles
    print(current_window)

@then('User switch back to original')
def switch_original_window(context):
    context.driver.switch_to.window(context.original_window)