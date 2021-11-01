from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import random
import string

DOMAIN_URL = "http://selenium1py.pythonanywhere.com"
PRODUCT_CODERS_LINK = DOMAIN_URL + "/catalogue/coders-at-work_207/"
PRODUCT_CITY_LINK = DOMAIN_URL + "/en-gb/catalogue/the-city-and-the-stars_95/"
LOGIN_LINK = DOMAIN_URL + "/accounts/login/"


@pytest.mark.parametrize('link', [PRODUCT_CODERS_LINK + "?promo=offer0",
                                  PRODUCT_CODERS_LINK + "?promo=offer1",
                                  PRODUCT_CODERS_LINK + "?promo=offer2",
                                  PRODUCT_CODERS_LINK + "?promo=offer3",
                                  PRODUCT_CODERS_LINK + "?promo=offer4",
                                  PRODUCT_CODERS_LINK + "?promo=offer5",
                                  PRODUCT_CODERS_LINK + "?promo=offer6",
                                  pytest.param(PRODUCT_CODERS_LINK +
                                               "?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  PRODUCT_CODERS_LINK + "?promo=offer8",
                                  PRODUCT_CODERS_LINK + "?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_price_in_cart()
    page.should_be_product_title_in_cart()
    page.shoul_match_product_title_with_title_in_cart(page.get_product_title())
    page.shoul_match_product_price_with_price_in_cart(page.get_product_price())


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = PRODUCT_CODERS_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = PRODUCT_CODERS_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


# @pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = PRODUCT_CODERS_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = PRODUCT_CODERS_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_disappear_success_message()


# @pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = PRODUCT_CITY_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = PRODUCT_CITY_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        def generate_random_string(max_length: int = 10):
            return ''.join(
                    random.choice(string.ascii_letters + string.digits)
                    for i in range(max_length)
                )

        self.product_link = PRODUCT_CODERS_LINK

        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()

        email = f'{generate_random_string()}@fakemail.org'
        password = generate_random_string()

        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.add_product_to_cart()
        page.should_be_product_price_in_cart()
        page.should_be_product_title_in_cart()
        page.shoul_match_product_title_with_title_in_cart(
            page.get_product_title()
        )
        page.shoul_match_product_price_with_price_in_cart(
            page.get_product_price()
        )

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.product_link)
        page.open()
        page.should_not_be_success_message()
