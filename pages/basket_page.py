from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS), \
            "Basket isn't empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*MainPageLocators.EMPTY_BASKET_MESSAGE), \
            "There should be empty basket message but it absent."