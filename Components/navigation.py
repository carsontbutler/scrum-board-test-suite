from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestSuite.configuration import *
from TestSuite.selectors import *

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