from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TestSuite.configuration import *
from TestSuite.selectors import *

import time


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
        try:

            prefix_input = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_prefix_xpath)))
            prefix_input.clear()
            prefix_input.send_keys(changed_board_prefix)

            save_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_save_btn_xpath)))
            save_btn.click()
            time.sleep(1)

            board_settings_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, board_settings_btn_xpath)))
            board_settings_btn.click()

            new_prefix = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_prefix_xpath))).get_attribute('value')

            save_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_save_btn_xpath)))
            save_btn.click()

            return new_prefix.lower()

        except:
            return False

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
