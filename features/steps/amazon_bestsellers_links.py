from selenium.webdriver.common.by import By
from behave import given, when, then

links = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')

@Given("Open Amazon BestSellers page")
def open_amazon_BestSellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@Then('Verify there are 5 links')
def link_verify(context):
    No_link = context.driver.find_elements(*links)
    print(No_link)
    assert len(No_link) == 5, f"Expected 5 links but got {len(No_link)} "
