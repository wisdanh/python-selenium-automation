from selenium.webdriver.common.by import By
from behave import given, when, then





@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Cart icon')
def cart_icon(context):
    icon = context.driver.find_element(By.ID, 'nav-cart-count')
    icon.click()

@then('Your Amazon cart is empty')
def cart_emtpy(context):
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text
    expected_result = 'Your Amazon Cart is empty'
    assert actual_result == expected_result, f"Expected text {expected_result} did not match actual {actual_result}"
