from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

Product_Price = (By.XPATH,"//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
@Given("Open Amazon")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when("Search for {search_word}")
def search_product(context, search_word):
    search = context.driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
    search.send_keys(search_word)
    search.send_keys(Keys.RETURN)

@when("Click on first product")
def click_first_product(context):
    context.driver.find_element(*Product_Price).click()


@when("Click on Add to Cart button")
def click_addToCart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

@when("Open cart page")
def open_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()

@Then("Verify cart has {expected_amount} item(s)")
def verify_cart(context, expected_amount):
    actual_result = context.driver.find_element(By.ID,'nav-cart-count').text
    assert actual_result == expected_amount, f'Expected {expected_amount}, but got {actual_result}'









