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
sys.path.append('..')


# Logging setup
timestr = time.strftime("%Y-%m-%d_%H%M%S")
log = logging.getLogger(__name__)
logging.basicConfig(filename=timestr, encoding='utf-8',
                    level=logging.DEBUG, format='%(asctime)s %(message)s')

#-----Config-----#
url = 'http://localhost:3000'


#-----Input Data-----#
# Organization Data
new_organization_name = 'Test Organization'
# Board Data
new_board_name = 'Test Board 1'
changed_board_name = 'changed board name'
new_board_prefix = 'TB1'
changed_board_prefix = 'TB1x'
# Column Data
new_col_names = ['New Column 1', 'New Column 2', 'New Column 3']


#-----Selectors-----#
# LoginPage selectors
username_id = "username-field"
password_id = "password-field"
login_btn_id = 'login-btn'
logout_btn_id = 'logout-btn'

# Navigation selectors
navbar_id = 'navbar'
navbar_profile_id = 'nav-profile'

# Organization selectors
nav_organizations_id = 'nav-organizations'
nav_organizations_new_text = 'New Organization'
nav_organizations_create_text = 'Create new'
create_organization_input_id = 'formName'
create_organization_save_btn_xpath = '/html/body/div[3]/div/div/div[3]/div[1]/button'
org_list_btn_class = 'org-list-btn'
error_text_class = 'error-text'

# Board selectors
nav_boards_id = 'nav-boards'
nav_new_board_text = 'New board'
create_board_title_input_id = 'formName'
create_board_prefix_input_id = 'formPrefix'
create_board_save_btn_xpath = '/html/body/div[3]/div/div/div[3]/div[1]/button'
nav_boards_item_class = 'nav-board-item'
board_settings_btn_xpath = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div/div[1]/button'
board_setting_modal_title_class = 'modal title'
edit_board_title_xpath = '//*[@id="formName"]'
edit_board_prefix_xpath = '//*[@id="formPrefix"]'
edit_board_save_btn_xpath = '/html/body/div[3]/div/div/div[3]/div/div/div[1]/button'
board_title_header_id = 'board-title'

# Columns
edit_board_columns_btn_xpath = '/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/button'
add_column_btn_xpath = '/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/div/button'
new_column_name_input_xpath = '//*[@id="addColumnForm"]/div/input'
save_new_column_btn_xpath = '/html/body/div[5]/div/div/div[3]/div[1]/button'
edit_columns_close_btn_xpath = '/html/body/div[3]/div/div/div[3]/div/div/button'
col_header_class = 'column-name'
close_btn_class = 'cancel-btn'

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


class LoginPage():
    def goTo(self, driver, wait):
        try:
            driver.get(url)
            wait.until(EC.presence_of_element_located((By.ID, login_btn_id)))
            return True
        except:
            return False

    def login(self, wait, username, password):
        try:
            # Find login form components
            username_field = wait.until(
                EC.presence_of_element_located((By.ID, username_id)))
            password_field = wait.until(
                EC.presence_of_element_located((By.ID, password_id)))
            login_btn = wait.until(
                EC.presence_of_element_located((By.ID, login_btn_id)))

            # Fill out login form and submit
            username_field.send_keys(username)
            password_field.send_keys(password)
            login_btn.click()

            home = wait.until(
                EC.presence_of_element_located((By.ID, navbar_id)))
            return True
        except:
            return False


class Navigation():
    def logout(self, wait):
        try:
            navbar_profile_button = wait.until(
                EC.presence_of_element_located((By.ID, navbar_profile_id)))
            navbar_profile_button.click()
            logout_btn = wait.until(
                EC.presence_of_element_located((By.ID, logout_btn_id)))
            logout_btn.click()
            login_btn = wait.until(
                EC.presence_of_element_located((By.ID, login_btn_id)))
            return True
        except:
            return False


class Organization():
    def create_organization_via_nav(self, wait):
        try:
            nav_organizations_link = wait.until(
                EC.presence_of_element_located((By.ID, nav_organizations_id)))
            nav_organizations_link.click()

            nav_organizations_new_btn = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, nav_organizations_new_text)))
            nav_organizations_new_btn.click()

            create_organization_input = wait.until(
                EC.presence_of_element_located((By.ID, create_organization_input_id)))
            create_organization_input.send_keys(new_organization_name)

            create_organization_save_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, create_organization_save_btn_xpath)))
            create_organization_save_btn.click()

            try:  # check for errors, return if any are found
                error = wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, error_text_class)))
                return error.text
            except:
                pass

            org_list = wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, org_list_btn_class)))

            for ele in org_list:
                if ele.text.lower() == new_organization_name.lower():
                    return ele.text.lower()
        except:
            return False


class Board():
    def create_board_via_nav(self, wait):
        try:
            nav_organizations_link = wait.until(
                EC.presence_of_element_located((By.ID, nav_organizations_id)))
            nav_organizations_link.click()

            target_organization = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, new_organization_name)))
            target_organization.click()

            nav_boards_link = wait.until(
                EC.presence_of_element_located((By.ID, nav_boards_id)))
            nav_boards_link.click()

            nav_new_board_link = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, nav_new_board_text)))
            nav_new_board_link.click()

            create_board_title_input = wait.until(
                EC.presence_of_element_located((By.ID, create_board_title_input_id)))
            create_board_prefix_input = wait.until(
                EC.presence_of_element_located((By.ID, create_board_prefix_input_id)))

            create_board_title_input.send_keys(new_board_name)
            create_board_prefix_input.send_keys(new_board_prefix)

            create_board_save_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, create_board_save_btn_xpath)))
            create_board_save_btn.click()

            nav_boards_link.click()

            nav_board_items = wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, nav_boards_item_class)))
            for ele in nav_board_items:
                if ele.text.lower() == new_board_name.lower():
                    return ele.text.lower()
        except:
            return False

    def edit_board_title(self, wait):
        try:
            nav_board_items = wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, nav_boards_item_class)))
            for ele in nav_board_items:
                if ele.text.lower() == new_board_name.lower():
                    target_board = ele
            target_board.click()

            board_settings_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, board_settings_btn_xpath)))
            board_settings_btn.click()

            title_input = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_title_xpath)))
            title_input.clear()
            title_input.send_keys(changed_board_name)

            save_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_save_btn_xpath)))
            save_btn.click()
            time.sleep(1)
            board_settings_btn.click()

            new_title = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_title_xpath))).get_attribute('value')

            return new_title
        except:
            return False

    def edit_board_prefix(self, wait):
        nav_board_items = wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, nav_boards_item_class)))
        for ele in nav_board_items:
            if ele.text.lower() == new_board_name.lower():
                target_board = ele
        target_board.click()

        board_settings_btn = wait.until(
            EC.presence_of_element_located((By.XPATH, board_settings_btn_xpath)))
        board_settings_btn.click()

        prefix_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_prefix_xpath)))
        prefix_input.clear()
        prefix_input.send_keys(changed_board_prefix)

        save_btn = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_save_btn_xpath)))
        save_btn.click()
        time.sleep(1)
        board_settings_btn.click()

        new_prefix = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_prefix_xpath))).get_attribute('value')

        return new_prefix

    def edit_board_title_and_prefix(self, wait):
        nav_board_items = wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, nav_boards_item_class)))
        for ele in nav_board_items:
            if ele.text.lower() == new_board_name.lower():
                target_board = ele
        target_board.click()

        board_settings_btn = wait.until(
            EC.presence_of_element_located((By.XPATH, board_settings_btn_xpath)))
        board_settings_btn.click()

        title_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_title_xpath)))
        title_input.clear()
        title_input.send_keys(changed_board_name)

        prefix_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_prefix_xpath)))
        prefix_input.clear()
        prefix_input.send_keys(changed_board_prefix)

        save_btn = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_save_btn_xpath)))
        save_btn.click()
        time.sleep(1)
        board_settings_btn.click()

        new_title = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_title_xpath))).get_attribute('value')
        new_prefix = wait.until(EC.presence_of_element_located(
            (By.XPATH, edit_board_prefix_xpath))).get_attribute('value')
        return new_title, new_prefix


class Column():
    def create_columns(self, wait):
        col_header_text = []
        try:
            columns_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_columns_btn_xpath)))
            columns_btn.click()

            for col in new_col_names:
                add_column_btn = wait.until(
                    EC.presence_of_element_located((By.XPATH, add_column_btn_xpath)))
                add_column_btn.click()

                new_column_name_input = wait.until(
                    EC.presence_of_element_located((By.XPATH, new_column_name_input_xpath)))
                new_column_name_input.send_keys(col)

                save_new_column_btn = wait.until(
                    EC.presence_of_element_located((By.XPATH, save_new_column_btn_xpath)))
                save_new_column_btn.click()

            close_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_columns_close_btn_xpath)))
            close_btn.click()

            close_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, close_btn_class)))
            close_btn.click()

            col_headers = wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, col_header_class)))

            
            for i in range(len(col_headers)):
                col_header_text.append(col_headers[i].text)
            return col_header_text

        except:
            return col_header_text

    def edit_column():
        pass

    def delete_column():
        pass


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

class TestUI():
    def test_goto_login(self, driver, wait):
        log.info('Starting test_goto_login')
        assert LoginPage.goTo(self, driver, wait) == True

    def test_login(self, wait, username, password):
        log.info('Starting test_login')
        assert LoginPage.login(self, wait, username, password) == True

    def test_create_org_via_nav(self, wait):
        log.info('Starting test_create_org_via_nav')
        assert Organization.create_organization_via_nav(
            self, wait) == new_organization_name.lower()

    def test_create_board_via_nav(self, wait):
        log.info('Starting test_create_board_via_nav')
        assert Board.create_board_via_nav(self, wait) == new_board_name.lower()

    def test_edit_board_title(self, wait):
        log.info('Starting edit_board_title')
        assert Board.edit_board_title(
            self, wait) == changed_board_name.lower()

    def test_create_columns(self, wait):
        log.info('Starting test_create_columns')
        assert Column.create_columns(self, wait) == new_col_names

    def test_logout(self, wait):
        log.info('Starting test_logout')
        assert Navigation.logout(self, wait) == True
