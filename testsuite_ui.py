from TestSuite.selectors import *
from TestSuite.conftest import *
from TestSuite.Components.login_page import *
from TestSuite.Components.organization import *

import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


# Setup
@pytest.fixture(scope="class")
def driver():
    _driver = webdriver.Chrome()
    log.info('fixture: driver initialized')
    yield _driver
    _driver.close()


@pytest.fixture(scope="class")
def wait(driver):
    _wait = WebDriverWait(driver, 4)
    log.info('fixture: wait initialized')
    yield _wait


@pytest.fixture(scope="class")
def username():
    _username = 'test_user'
    log.info('fixture: username initialized')
    yield _username


@pytest.fixture(scope="class")
def password():
    log.info('fixture: password initialized')
    _password = 'password321'
    yield _password

class TestUI():
    def test_goto_login(self, driver, wait):
        log.info('Starting test_goto_login')
        assert LoginPage.goTo(self, driver, wait) == True

    def test_login(self, wait, username, password):
        log.info('Starting test_login')
        assert LoginPage.login(self, wait, username, password) == True