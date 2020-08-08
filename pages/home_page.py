from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    home_url = "http://120.78.128.25:8765/Index/index"
    # 页面元素定位表达式
    user_element_locator = (By.XPATH, "//a[@href='/Member/index.html']")
    bid_locator = (By.CSS_SELECTOR, ".btn-special")
    # bid_locator = (By.XPATH, "//div[@class='b-unit-list clearfix']//div[1]//div[1]//div[3]//div[1]//a[1]")


    @property
    def user_element(self):
        """定位主页用户名所在的位置"""
        return self.wait_presence_element(self.user_element_locator)

    @property
    def bid_button(self):
        """首页投标按钮（三个随便选一个都可以）"""
        return  self.wait_click_element(self.bid_locator)

    def click_bid_button(self):
        """点击首页投标"""
        return self.bid_button.click()

    def get(self):
        return self.driver.get(self.home_url)
