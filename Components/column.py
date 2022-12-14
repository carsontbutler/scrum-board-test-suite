from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TestSuite.configuration import *
from TestSuite.selectors import * 

import time

class Column():
    def create_columns(self, wait):
        col_header_text = []
        try:
            board_settings_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, board_settings_btn_xpath)))
            board_settings_btn.click()

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
                time.sleep(0.5)

            close_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_columns_close_btn_xpath)))
            close_btn.click()

            col_headers = wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, col_header_class)))

            for i in range(len(col_headers)):
                col_header_text.append(col_headers[i].text)

            return col_header_text

        except:
            return col_header_text

    def edit_columns(self, wait):
        try:
            board_settings_btn = wait.until(
                EC.presence_of_element_located((By.XPATH, board_settings_btn_xpath)))
            board_settings_btn.click()

            columns_btn = wait.until(EC.presence_of_element_located(
                (By.XPATH, edit_board_columns_btn_xpath)))
            columns_btn.click()

            edit_btns = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, edit_col_btn_class)))
            col_names = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, edit_col_name_input_class)))

            for i in range(len(edit_btns)):
                edit_btns[i].click()
                col_names[i].clear()
                col_names[i].send_keys(changed_col_names[i])

        except:
            time.sleep(5)
            return col_names[i].text

    def delete_column():
        pass
