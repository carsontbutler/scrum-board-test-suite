import time
import logging
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import sys
from TestSuite.selectors import *
from TestSuite.Pages.login_page import *
sys.path.append('..')


class Ticket():
    def create_ticket():
        pass

    def edit_ticket():
        pass

    def delete_ticket():
        pass


class JoinRequest():
    def send_request():
        pass

    def approve_request():
        pass

    def deny_request():
        pass

# class TestUI():
#     def test_goto_login(self, driver, wait):
#         log.info('Starting test_goto_login')
#         assert LoginPage.goTo(self, driver, wait) == True

    # def test_login(self, wait, username, password):
    #     log.info('Starting test_login')
    #     assert LoginPage.login(self, wait, username, password) == True

#     def test_create_org_via_nav(self, wait):
#         log.info('Starting test_create_org_via_nav')
#         assert Organization.create_organization_via_nav(
#             self, wait) == new_organization_name.lower()

#     def test_create_board_via_nav(self, wait):
#         log.info('Starting test_create_board_via_nav')
#         assert Board.create_board_via_nav(self, wait) == new_board_name.lower()

#     def test_edit_board_title(self, wait):
#         log.info('Starting edit_board_title')
#         assert Board.edit_board_title(
#             self, wait) == changed_board_name.lower()

#     def test_create_columns(self, wait):
#         log.info('Starting test_create_columns')
#         assert Column.create_columns(self, wait) == new_col_names

#     def test_logout(self, wait):
#         log.info('Starting test_logout')
#         assert Navigation.logout(self, wait) == True

class TestUI():
    def test_goto_login(self, driver, wait):
        log.info('Starting test_goto_login')
        assert LoginPage.goTo(self, driver, wait) == True