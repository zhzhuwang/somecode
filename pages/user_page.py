from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserPage(BasePage):
    balance_locator = (By.CSS_SELECTOR, ".color_sub")

    @property
    def balance_element(self):
        return self.wait_visible_element(self.balance_locator)

    def get_balance(self):
        return self.balance_element.text.strip("元")

