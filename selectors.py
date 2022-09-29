#---Might want to split this into 2 files later (selectors.py and input_data.py)---#

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
edit_col_btn_class = 'edit-btn'
edit_col_name_input_class = 'column-name'


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
changed_col_names = ['Changed Col 1', 'Changed Col 2', 'Changed Col 3']