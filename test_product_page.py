import pytest
from .pages.product_page import ProductPage
from.pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time




#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_product_to_basket()
#     time.sleep(1)
#     page.should_disappeared()
#
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     page.should_be_login_page()
#
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_link()
#     basket = BasketPage(browser, link)
#     basket.should_be_basket_empty()
#     basket.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser=browser, url=link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "password"
        login_page.register_new_user(email, password)
        time.sleep(1)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_product_added_basket()
        page.should_be_name_product_equal_real_product()
        page.should_be_message_about_price_added_basket()
        page.should_be_price_product_equal_real_product()