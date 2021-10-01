from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART
        )
        add_to_cart_button.click()

    def get_product_title(self):
        product_title = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE
        )
        return product_title.text

    def get_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        return product_price.text

    def should_be_product_title_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.TITLE_IN_MESSAGE),\
            "Product title in message is not presented"

    def shoul_match_product_title_with_title_in_cart(self, product_title):
        title_in_message = self.browser.find_element(
            *ProductPageLocators.TITLE_IN_MESSAGE
        ).text
        assert product_title == title_in_message, "Product title doesn't match"

    def should_be_product_price_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE),\
            "Product price in message is not presented"

    def shoul_match_product_price_with_price_in_cart(self, product_price):
        price_in_message = self.browser.find_element(
            *ProductPageLocators.PRICE_IN_MESSAGE
        ).text
        assert product_price == price_in_message, "Product price doesn't match"
