from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BidPage(BasePage):
    bid_input_locator = (By.CSS_SELECTOR, ".form-control")
    bid_confirm_locator = (By.CSS_SELECTOR, ".btn-special")
    bid_popup_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='capital_font1 note']")
    bid_active_button_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")
    bid_error_alert_locator = (By.CSS_SELECTOR, ".layui-layer-content div")

    @property
    def bid_input(self):
        """投资输入框"""
        return self.wait_visible_element(self.bid_input_locator)

    def bid_success(self, money):
        """投资成功"""
        ele = self.bid_input
        balance = ele.get_attribute("data-amount")
        ele.send_keys(money)
        self.bid_confirm_button.click()
        return balance

    @property
    def bid_confirm_button(self):
        """投资确认按钮"""
        return self.wait_visible_element(self.bid_confirm_locator)

    @property
    def bid_popup_msg_element(self):
        """找到投标成功的元素"""
        return self.wait_visible_element(self.bid_popup_msg_locator)

    @property
    def bid_error_alert_element(self):
        """提示：投标金额必须为100的倍数"""
        return self.wait_visible_element(self.bid_error_alert_locator)

    def click_bid_active_button(self):
        """点击投资成功弹框中的查看并激活按钮"""
        return self.wait_click_element(self.bid_active_button_locator).click()

