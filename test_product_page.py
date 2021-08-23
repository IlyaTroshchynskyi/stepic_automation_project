from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_message_about_product_added_basket()
    page.should_be_name_product_equal_real_product()
    page.should_be_message_about_price_added_basket()
    page.should_be_price_product_equal_real_product()
