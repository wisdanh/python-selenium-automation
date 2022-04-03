from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultPage(Page):
    DEPARTMENT = (By.CSS_SELECTOR, "#nav-subnav[data-category='{department_cat}']")

    def get_department_locator(self, department: str):
        return [self.DEPARTMENT[0], self.DEPARTMENT[1].replace('{department_cat}', department)]

    def verify_correct_department(self, department):
        department_locator = self.get_department_locator(department)
        self.wait_for_element_appear(*department_locator)