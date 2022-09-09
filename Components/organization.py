from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestSuite.configuration import *
from TestSuite.selectors import *


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