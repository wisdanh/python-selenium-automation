from selenium.webdriver.common.by import By
from behave import given, when, then

#orders_link = (By.ID,'nav-orders')
#continue_button = (By.ID,'continue-announce')
#expected_text = (By.CSS_SELECTOR, 'h1.a-spacing-small')

@given('Open Amazon main page')
def open_amazonpage(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@given('Open Amazon {product_code} product page')
def open_productpage(context, product_code):
    #end_url = 'gp/product/B074TBCSC8'
    product_code = 'B074TBCSC8'
    context.app.Product_page.open_product_page(product_code)

@when('Hover over New Arrivals')
def hover_over_newarrivals(context):
    context.app.header.hover_over_newarrivals()

@when('Select {alias} department')
def select_department(context, alias):
    context.app.header.select_department(alias)

@when('Click Amazon Orders link')
def click_orderlink(context):
    #context.driver.find_element(*orders_link).click()
    context.app.header.click_orderlink()

@then('Verify Sign In page is opened')
def opened_signin(context):
    #actual_text = context.driver.find_element(*expected_text).text
    end_url = '/ap/signin'
    context.app.header.SigninPage_link(end_url)

@when('CLick on Cart figure icon')
def click_carticon(context):
    context.app.header.click_carticon()

@then("Verify {expected_result} text present")
def text_present(context, expected_result):
    #keyword = 'Your Shopping Cart is empty'
    context.app.header.verifyShopcart_text(expected_result)

@then('Girl deals show up')
def girldeals_page(context):
    context.app.header.verify_girldeals()

@then('Verify {alias} department is selected')
def verify_department(context, alias):
    context.app.search_result_page.verify_correct_department(alias)
