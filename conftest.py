import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from datas.login_datas import exact_params
from selenium.webdriver import ChromeOptions


@pytest.fixture(scope="class")
def login_web():
    chrome_options = ChromeOptions()
    chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    yield driver, login_page
    driver.quit()


@pytest.fixture()
def login_func(login_web):
    yield
    driver, login_page = login_web
    driver.refresh()


@pytest.fixture(scope="class")
def bid_web():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    data = exact_params[0]
    login_page.login(data['phone'], data['pwd'])
    yield driver, login_page
    driver.quit()


@pytest.fixture()
def bid_func(bid_web):
    yield
    driver, login_page = bid_web
    driver.refresh()
