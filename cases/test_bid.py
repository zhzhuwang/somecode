import pytest
import unittest
from datas.bid_data import bid_error_data_1, bid_success_data, bid_error_data_2
from pages.bid_page import BidPage
from pages.home_page import HomePage
from pages.user_page import UserPage
from decimal import Decimal


@pytest.mark.usefixtures('bid_func')
@pytest.mark.bid
class TestBid:

    @pytest.mark.parametrize('error_data', bid_error_data_1)
    def test_bid_error(self, error_data, bid_web):
        """投资金额不是10的倍数的情况"""
        driver, login_page = bid_web
        home_page = HomePage(driver)
        home_page.get()  # 与上面的sleep作用一致
        home_page.click_bid_button()
        bid_page = BidPage(driver)
        bid_page.bid_input.send_keys(error_data['amount'])
        assert error_data['expect'] == bid_page.bid_confirm_button.text

    @pytest.mark.parametrize('error_data', bid_error_data_2)
    def test_bid_error_div(self, error_data, bid_web):
        """投资金额不是100的倍数的情况"""
        driver, login_page = bid_web
        home_page = HomePage(driver)
        home_page.get()
        home_page.click_bid_button()
        bid_page = BidPage(driver)
        bid_page.bid_input.send_keys(error_data['amount'])
        bid_page.bid_confirm_button.click()
        assert error_data['expect'] == bid_page.bid_error_alert_element.text

    @pytest.mark.parametrize('success_data', bid_success_data)
    def test_bid_success(self, success_data, bid_web):
        """投资成功的情况"""
        driver, login_page = bid_web
        home_page = HomePage(driver)
        home_page.get()
        home_page.click_bid_button()
        bid_page = BidPage(driver)
        # bid_page.bid_input.send_keys(success_data['amount'])
        # bid_page.bid_confirm_button.click()
        balance = bid_page.bid_success(success_data['amount'])
        assert success_data['expect'] == bid_page.bid_popup_msg_element.text
        # 验证余额
        bid_page.click_bid_active_button()
        actual_balance = UserPage(driver).get_balance()
        assert Decimal(balance) - Decimal(success_data['amount']) == Decimal(actual_balance)


if __name__ == '__main__':
    unittest.main()
