import pytest
from .pages.product_page import ProductPage
import time


# def test_guest_can_add_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     time.sleep(1)
#     page.should_be_message_about_product_added_basket()
#     page.should_be_name_product_equal_real_product()
#     page.should_be_message_about_price_added_basket()
#     page.should_be_price_product_equal_real_product()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail(reason='some bug')),
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/"
                                  "catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_product_added_basket()
    page.should_be_name_product_equal_real_product()
    page.should_be_message_about_price_added_basket()
    page.should_be_price_product_equal_real_product()




# @pytest.mark.parametrize(
#     ("n", "expected"),
#     [
#         (1, 2),
#         pytest.param(1, 0, marks=pytest.mark.xfail),
#         pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
#         (2, 3),
#         (3, 4),
#         (4, 5),
#         pytest.param(
#             10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")
#         ),
#     ],
# )
# def test_increment(n, expected):
#     assert n + 1 == expected