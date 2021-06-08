import pytest
from selenium import webdriver
import inspect
import logging


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")



@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    elif browser == 'edge':
        driver = webdriver.Chrome(executable_path="drivers/msedgedriver.exe")

    driver.get("https://swms.prozo.com/auth/login")
    driver.maximize_window()
    # log = getlogger()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    request.cls.webdriver = webdriver
    yield
    driver.close()