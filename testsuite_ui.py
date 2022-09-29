from TestSuite.selectors import *
from TestSuite.conftest import *
from TestSuite.Components.login_page import *
from TestSuite.Components.organization import *
from TestSuite.Components.board import *
from TestSuite.Components.column import *

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
    _password = 'pword321'
    yield _password

class TestUI():
    #Login
    def test_goto_login(self, driver, wait):
        log.info('Starting test_goto_login')
        assert LoginPage.goTo(self, driver, wait) == True

    def test_login(self, wait, username, password):
        log.info('Starting test_login')
        assert LoginPage.login(self, wait, username, password) == True

    #Organizations
    def test_create_organization_via_nav(self, wait):
        log.info('Starting test_create_organization')
        assert Organization.create_organization_via_nav(self, wait) == new_organization_name.lower()

    #Boards
    def test_create_board(self, wait):
        log.info('Starting test_create_board_via_nav')
        assert Board.create_board_via_nav(self, wait) == new_board_name.lower()
    
    def test_edit_board_title(self, wait):
        log.info('Starting test_edit_board_title')
        assert Board.edit_board_title(self, wait) == changed_board_name.lower()

    def test_edit_board_prefix(self, wait):
        log.info('Starting test_edit_board_prefix')
        assert Board.edit_board_prefix(self, wait) == changed_board_prefix.lower()
    
    #Columns
    def test_create_columns(self, wait):
        log.info('Started test_create_columns')
        assert Column.create_columns(self, wait) == new_col_names

    # def test_edit_columns(self,wait):
    #     log.info('Started test_edit_columns')
    #     assert Column.edit_columns(self, wait) == changed_col_names

    #Tickets
    