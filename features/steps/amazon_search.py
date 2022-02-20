from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver
#from time import sleep

#SEARCH_INPUT = driver.find_element(By.ID,'helpsearch')

@given('Open Amazon help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} into Search Help Library field')
def search_input(context, search_word):
    search = context.driver.find_element(By.ID,'helpsearch')
    search.send_keys(search_word)
    search.send_keys(Keys.RETURN)



@then('Cancel items or Orders are present')
def verify_results(context):
    expected_result = "Cancel ItemS or Orders"
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']//h1[text()='Cancel Items or Orders']").text
    assert actual_result == expected_result, f"Expected text {expected_result} did not match actual {actual_result}"
