from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_url = 'http://120.78.128.25:8765/Index/login.html'
    # 页面元素定位表达式
    login_button_locator = (By.XPATH, "//button[@class='btn btn-special']")
    phone_elem_locator = (By.NAME, "phone")
    pwd_elem_locator = (By.NAME, "password")
    error_msg_locator = (By.CSS_SELECTOR, ".form-error-info")
    invalidate_msg_locator = (By.CSS_SELECTOR, ".layui-layer-content")

    def login(self, phone, password):
        """登录"""
        self.driver.get(self.login_url)
        login_button = self.driver.find_element(*self.login_button_locator)  # 解包
        self.phone_elem.send_keys(phone)
        self.pwd_elem.send_keys(password)
        login_button.click()

    @property
    def phone_elem(self) -> WebElement:
        return self.wait_presence_element(self.phone_elem_locator)

    @property
    def pwd_elem(self) -> WebElement:
        return self.wait_presence_element(self.pwd_elem_locator)

    def get_actual_result(self):
        """报错位置定位"""
        return self.wait_presence_element(self.error_msg_locator)

    def get_invalidate_result(self):
        """没有通过授权的弹框位置定位，必须等待"""
        return self.wait_visible_element(self.invalidate_msg_locator)
