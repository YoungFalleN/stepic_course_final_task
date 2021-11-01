from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_empty_basket_text()
        self.should_be_no_products_in_basket()

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
            "Basket is not empty"

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PRODUCTS_LIST),\
            "There are products in basket"
