from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from selenium.webdriver.common.by import By

Add_to_Cart_Btn = (By.ID, "add-to-cart-button")
COLOR_OPTIONS = (By.CSS_SELECTOR,'#variation_color_name li')
CURRENT_COLORS = (By.CSS_SELECTOR,'#variation_color_name .selection')

@given('Open Amazon product {product_id}')
def open_amazon_product(context, product_id):
    context.driver.get(f"https://www.amazon.com/gp/product/{product_id}/")

@then('Verify users can click through colors')
def verify_color_click(context):
    expected_color = ['Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black', 'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive', 'Sage Green', 'Blue, Over Dye', 'Blue, Dip Dye']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    actual_color = []
    for color in color_options:
        color.click()
        current_color_name = context.driver.find_element(*CURRENT_COLORS).text
        actual_color += [current_color_name]

    assert expected_color == actual_color, f'Actual {actual_color} do not match {expected_color}'



