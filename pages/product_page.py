from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        btn.click()

    def should_be_message_about_product_added_basket(self):
        assert self.is_element_present(*ProductPageLocators.PROD_MESSAGE), \
            "Alert message about product isn't exist"

    def should_be_name_product_equal_real_product(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        prod_message = self.browser.find_element(*ProductPageLocators.PROD_MESSAGE).text
        assert prod_name == prod_message, "Real prod name dosn't equal prod name in basket"

    def should_be_message_about_price_added_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), \
            "Alert message about price doesn't exist"

    def should_be_price_product_equal_real_product(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert price == price_message, "Real price dosn't equal price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PROD_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PROD_MESSAGE), \
            "Element isn't disappeared"