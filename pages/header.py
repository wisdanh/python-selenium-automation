from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    orders_link = (By.ID, 'nav-orders')
    continue_button = (By.ID, 'continue-announce')
    expected_text = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    cart_icon = (By.ID, 'nav-cart-text-container')
    emptycart_text = (By.XPATH,"//h2[contains(text(),'Your Amazon Cart is empty')]")

    def click_orderlink(self):
        self.click(*self.orders_link)

    def click_carticon(self):
        self.click(*self.cart_icon)

    def SigninPage_link(self, end_url):

        self.verify_url_contains_query(end_url)

    def verifyShopcart_text(self, expected_result):
        self.verify_text(expected_result, *self.emptycart_text)


