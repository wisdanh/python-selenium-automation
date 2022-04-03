from pages.base_page import Page

class ProductPage(Page):
    def open_product_page(self, product_code: str):
        self.open_page(end_url=f'gp/product/{product_code}')
