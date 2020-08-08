from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome, ActionChains
from scripts import config
from datetime import datetime
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from scripts.handle_logger import do_logger


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait_presence_element(self, locator):
        """等待元素出现"""
        try:
            return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            do_logger.error("定位出错！")
            self.save_screenshot()

    def wait_click_element(self, locator):
        """等待元素可点击"""
        return WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable(locator))

    def wait_visible_element(self, locator):
        """等待元素可见"""
        return WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located(locator))

    def save_screenshot(self):
        """自动化保存截图"""
        img_name = config.LOG_IMG + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S" + ".png")
        # img_path = config.LOG_DIR + '\\' + img_name
        img_path = os.path.join(config.LOG_DIR, img_name)
        self.driver.get_screenshot_as_file(img_path)

    def get_url(self):
        return self.driver.current_url

    def get_cookies(self):
        return self.driver.get_cookies()

    def switch_window(self, window_name):
        pass

    def switch_iframe(self, iframe_reference):
        pass

    def switch_alert(self):
        pass

    # 鼠标操作, 移动，拖拽
    # 滚动条
    # 键盘操作
    # 上传文件
    def double_click(self, elem):
        """双击"""
        action_chains = ActionChains(self.driver)
        return action_chains.double_click(elem).perform()

    def context_click(self, elem):
        """右击"""
        action_chains = ActionChains(self.driver)
        return action_chains.context_click(elem).perform()

    def scroll_window(self, width, height):
        """滚动到对应窗口位置"""
        return self.driver.execute_script("window.scrollTo({}, {})".format(width, height))

    def upload_file(self, elem, file_path):
        # 判断是否input， 是的话elem.send_keys()
        # 不是的话pywin32
        pass
