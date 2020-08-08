import pytest
from pages.home_page import HomePage
from datas.login_datas import error_phone_params, invalidate_params, exact_params


@pytest.mark.usefixtures('login_func')
@pytest.mark.login
class TestLogin:

    @pytest.mark.parametrize('error_phone', error_phone_params)
    def test_1_login_error(self, error_phone, login_web):
        driver, login_page = login_web
        login_page.login(error_phone['phone'], error_phone['pwd'])
        error_msg_element = login_page.get_actual_result()
        assert error_phone['expect'] == error_msg_element.text

    @pytest.mark.parametrize('invalidate', invalidate_params)
    def test_2_login_unvalidate(self, invalidate, login_web):
        driver, login_page = login_web
        login_page.login(invalidate['phone'], invalidate['pwd'])
        invalidate_msg_element = login_page.get_invalidate_result()
        assert invalidate['expect'] == invalidate_msg_element.text

    @pytest.mark.parametrize('exact', exact_params)
    def test_3_login_success(self, exact, login_web):
        driver, login_page = login_web
        login_page.login(exact['phone'], exact['pwd'])
        success_msg_element = HomePage(driver).user_element
        assert exact['expect'] == success_msg_element.text

