from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Header(Page):
    orders_link = (By.ID, 'nav-orders')
    continue_button = (By.ID, 'continue-announce')
    expected_text = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    cart_icon = (By.ID, 'nav-cart-text-container')
    emptycart_text = (By.XPATH,"//h2[contains(text(),'Your Amazon Cart is empty')]")
    NewArrivals = (By.CSS_SELECTOR, "a[href*='/New-Arrivals/b/']")
    GirlsFashion = (By.CSS_SELECTOR, "a[href*='/s?i=fashion-girls']")
    SELECT_DEPARTMENT = (By.ID, 'searchDropdownBox')

    def click_orderlink(self):
        self.click(*self.orders_link)

    def click_carticon(self):
        self.click(*self.cart_icon)

    def SigninPage_link(self, end_url):

        self.verify_url_contains_query(end_url)

    def verifyShopcart_text(self, expected_result):
        self.verify_text(expected_result, *self.emptycart_text, )

    def hover_over_newarrivals(self):
        newarrivals = self.find_element(*self.NewArrivals)
        actions = ActionChains(self.driver)
        actions.move_to_element(newarrivals)
        actions.perform()

    def verify_girldeals(self):
        self.wait_for_element_appear(*self.GirlsFashion)

    def select_department(self, alias: str):
        select_department = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department)
        select.select_by_value(f'search-alias={alias}')