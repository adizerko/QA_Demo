import base64
import random
import os
import time
from os import write

import requests
from selenium.webdriver.common.by import By

from curl import TEXT_BOX_URL, CHECK_BOX_URL, RADIO_BUTTON_URL, WEB_TABLES_URL, BUTTONS_URL, LINKS_URL, \
    UPLOAD_AND_DOWNLOAD_URL
from data import CHECKBOX_ELEMENTS, RADIO_BUTTON_ELEMENTS
from generation import Generation
from pages.base_page import BasePage


class TextBox(BasePage):
    USER_NAME_INPUT = By.ID, "userName"
    USER_EMAIL_INPUT = By.ID, "userEmail"
    CURRENT_ADDRESS = By.ID, "currentAddress"
    PERMANENT_ADDRESS = By.ID, "permanentAddress"
    SUBMIT = By.ID, "submit"

    USER_NAME_RESULT = By.ID, "name"
    USER_EMAIL_RESULT = By.ID, "email"
    USER_CURRENT_ADDRESS_RESULT = By.XPATH, "//p[@id='currentAddress']"
    USER_PERMANENT_ADDRESS_RESULT = By.XPATH, "//p[@id='permanentAddress']"


    def open_text_box_page(self):
        self.open(TEXT_BOX_URL)

    def set_user_name(self, user_name):
        self.send_keys(self.USER_NAME_INPUT, user_name)

    def set_user_email(self, email):
        self.send_keys(self.USER_EMAIL_INPUT, email)

    def set_current_address(self, current_address):
        self.send_keys(self.CURRENT_ADDRESS, current_address)

    def set_permanent_address(self, permanent_address):
        self.send_keys(self.PERMANENT_ADDRESS, permanent_address)

    def click_submit_button(self):
        self.click(self.SUBMIT)

    def is_user_name_correct(self, user_name):
        user_name_result = self.get_text(self.USER_NAME_RESULT).split(":")[1]
        return user_name == user_name_result

    def is_user_email_correct(self, user_email):
        user_email_result = self.get_text(self.USER_EMAIL_RESULT).split(":")[1]
        return user_email == user_email_result

    def is_current_address_correct(self, user_current_address):
        user_current_address_result = self.get_text(self.USER_CURRENT_ADDRESS_RESULT).split(":")[1]
        return user_current_address == user_current_address_result

    def is_permanent_address_correct(self, user_permanent_address):
        user_permanent_address_result = self.get_text(self.USER_PERMANENT_ADDRESS_RESULT).split(":")[1]
        return user_permanent_address == user_permanent_address_result


class CheckBox(BasePage):
    ROOT_TOGGLE = By.CSS_SELECTOR, "button[aria-label='Toggle']"
    CHECKBOX_HOME = By.CSS_SELECTOR, "span.rct-checkbox > svg"

    DESKTOP_TOGGLE = By.XPATH, "//span[text()='Desktop']/parent::label/parent::span/button"
    DESKTOP_CHECKBOX = By.XPATH, "//span[text()='Desktop']/parent::label/span[1]"
    NOTES_CHECKBOX = By.XPATH, "//span[text()='Notes']/parent::label/span[1]"
    COMMANDS_CHECKBOX = By.XPATH, "//span[text()='Commands']/parent::label/span[1]"

    DOCUMENTS_TOGGLE = By.XPATH, "//span[text()='Documents']/parent::label/parent::span/button"
    DOCUMENTS_CHECKBOX = By.XPATH, "//span[text()='Documents']/parent::label/span[1]"

    DOWNLOADS_TOGGLE = By.XPATH, "//span[text()='Downloads']/parent::label/parent::span/button"
    DOWNLOADS_CHECKBOX = By.XPATH, "//span[text()='Downloads']/parent::label/span[1]"
    WORD_FILE_CHECKBOX = By.XPATH, "//span[text()='Word File.doc']/parent::label/span[1]"
    EXCEL_FILE_CHECKBOX = By.XPATH, "//span[text()='Excel File.doc']/parent::label/span[1]"

    WORKSPACE_TOGGLE = By.XPATH, "//span[text()='WorkSpace']/parent::label/parent::span/button"
    WORKSPACE_CHECKBOX = By.XPATH, "//span[text()='WorkSpace']/parent::label/span[1]"
    REACT_CHECKBOX = By.XPATH, "//span[text()='React']/parent::label/span[1]"
    ANGULAR_CHECKBOX = By.XPATH, "//span[text()='Angular']/parent::label/span[1]"
    VEU_CHECKBOX = By.XPATH, "//span[text()='Veu']/parent::label/span[1]"

    OFFICE_TOGGLE = By.XPATH, "//span[text()='Office']/parent::label/parent::span/button"
    OFFICE_CHECKBOX = By.XPATH, "//span[text()='Office']/parent::label/span[1]"
    PUBLIC_CHECKBOX = By.XPATH, "//span[text()='Public']/parent::label/span[1]"
    PRIVATE_CHECKBOX = By.XPATH, "//span[text()='Private']/parent::label/span[1]"
    CLASSIFIED_CHECKBOX = By.XPATH, "//span[text()='Classified']/parent::label/span[1]"
    GENERAL_CHECKBOX = By.XPATH, "//span[text()='General']/parent::label/span[1]"

    CHECKED_ITEMS = By.XPATH, "//span[@class='rct-checkbox']//*[contains(@class, 'rct-icon-check')]/ancestor::label/span[@class='rct-title']"
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = By.CSS_SELECTOR, "span[class='text-success']"


    def open_check_box_page(self):
        self.open(CHECK_BOX_URL)

    def click_root_toggle(self):
        element = self.wait_for_element(self.ROOT_TOGGLE)
        element.click()

    def click_desktop_toggle(self):
        self.click(self.DESKTOP_TOGGLE)

    def click_documents_toggle(self):
        self.click(self.DOCUMENTS_TOGGLE)

    def click_downloads_toggle(self):
        self.click(self.DOWNLOADS_TOGGLE)

    def click_workspace_toggle(self):
        self.click(self.WORKSPACE_TOGGLE)

    def click_office_toggle(self):
        self.click(self.OFFICE_TOGGLE)

    def click_all_toggle(self):
        self.click_root_toggle()
        self.click_desktop_toggle()
        self.click_documents_toggle()
        self.click_downloads_toggle()
        self.click_workspace_toggle()
        self.click_office_toggle()

    def click_choosing_random_checkboxes(self):
        random_list_element_checkbox = random.sample(
            CHECKBOX_ELEMENTS, random.randint(1, 16))

        for el in random_list_element_checkbox:
            check_box_element = By.XPATH, f"//span[text()='{el}']/parent::label/span[1]"
            self.click(check_box_element)

    def get_checked_checkbox_elements(self):
        items = self.find_elements(self.CHECKED_ITEMS)
        checked_elements = []

        for i in items:
            checked_elements.append(i.text.lower().split('.doc')[0].replace(' ', ''))

        return checked_elements

    def get_result_checked_checkbox_elements(self):
        items = self.find_elements(self.OUTPUT_RESULT)
        result_checked_elements = []

        for i in items:
            result_checked_elements.append(i.text.lower().replace(' ', ''))

        return result_checked_elements


class RadioButton(BasePage):
    YES_RADIO = By.XPATH, "//label[@for='yesRadio']"
    IMPRESSIVE_RADIO = By.XPATH, "//label[@for='impressiveRadio']"
    NO_RADIO = By.XPATH, "//label[@for='noRadio']"
    SELECTED = By.CLASS_NAME, "text-success"

    def open_radio_button_page(self):
        self.open(RADIO_BUTTON_URL)

    def select_radio_button_yes(self):
        self.click(self.YES_RADIO)

    def select_radio_button_impressive(self):
        self.click(self.IMPRESSIVE_RADIO)

    def select_radio_button_no(self):
        self.click(self.NO_RADIO)

    def get_radio_result(self):
        text_result = self.get_text(self.SELECTED)
        return text_result

class WebTables(BasePage):
    ADD_BUTTON = By.ID, "addNewRecordButton"
    SEARCH_INPUT = By.ID, "searchBox"
    PREVIOUS_BUTTON = By.XPATH, "//div[@class='-previous']/button"
    NEXT_BUTTON = By.XPATH, "//div[@class='-next']/button"
    PAGE_INPUT = By.XPATH, "//input[@aria-label='jump to page']"
    COLUMN_FIRST_NAME = By.XPATH, "//div[text()='First Name'"
    COLUMN_LAST_NAME = By.XPATH, "//div[text()='Last Name']"
    COLUMN_AGE = By.XPATH, "//div[text()='Age']"
    COLUMN_EMAIL = By.XPATH, "//div[text()='Email']"
    COLUMN_SALARY = By.XPATH, "//div[text()='Salary']"
    COLUMN_DEPARTMENT = By.XPATH, "//div[text()='Department']"
    COLUMN_ACTION = By.XPATH, "//div[text()='Action']"

    FIRST_NAME_INPUT = By.ID, "firstName"
    LAST_NAME_INPUT = By.ID, "lastName"
    EMAIL_INPUT = By.ID, "userEmail"
    AGE_INPUT = By.ID, "age"
    SALARY_INPUT = By.ID, "salary"
    DEPARTMENT_INPUT = By.ID, "department"
    SUBMIT_BUTTON = By.ID, "submit"
    DELETE_BUTTON = By.XPATH, "//span[@title='Delete']"
    EDIT_BUTTON = By.XPATH, "//span[@title='Edit']"
    EDIT_BUTTON_LAST_USER = By.XPATH, "(//span[@title='Edit'])[last()]"

    TABLE_ROWS_SELECTOR = By.XPATH, "//select[@aria-label='rows per page']"
    TABLE_ROWS_OPTION_5 = By.XPATH, "//option[@value='5']"
    TABLE_ROWS_OPTION_10 = By.XPATH, "//option[@value='10']"
    TABLE_ROWS_OPTION_20 = By.XPATH, "//option[@value='20']"
    TABLE_ROWS_OPTION_25 = By.XPATH, "//option[@value='25']"
    TABLE_ROWS_OPTION_50 = By.XPATH, "//option[@value='50']"
    TABLE_ROWS_OPTION_100 = By.XPATH, "//option[@value='100']"

    FIELDS = By.XPATH, "//div[@class='rt-tr-group']"


    FIRST_NAME_ADDED_CHECK = By.XPATH, "//*[text()='kierra@example.com']/parent::div"

    def open_web_tables_page(self):
        self.open(WEB_TABLES_URL)

    def add_button_click(self):
        self.click(self.ADD_BUTTON)

    def click_edit_button_lust_user(self):
        self.click(self.EDIT_BUTTON_LAST_USER)

    def set_first_name(self):
        first_name = Generation.first_name()
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        return first_name

    def set_last_name(self):
        last_name = Generation.last_name()
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        return last_name

    def set_email(self):
        email = Generation.email()
        self.send_keys(self.EMAIL_INPUT, email)
        return email

    def set_age(self):
        age = Generation.age()
        self.send_keys(self.AGE_INPUT, age)
        return age

    def set_salary(self):
        salary = Generation.salary()
        self.send_keys(self.SALARY_INPUT, salary)
        return salary

    def set_department(self):
        department = Generation.department()
        self.send_keys(self.DEPARTMENT_INPUT, department)
        return department

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    def fill_user_form_and_get_data(self, returned: str = "no", ):
        first = self.set_first_name()
        last = self.set_last_name()
        email = self.set_email()
        age = self.set_age()
        salary = self.set_salary()
        dept = self.set_department()
        if returned == "yes":
            return [first, last, age, email, salary, dept]


    def get_result_new_user(self, email):
        locator_user = By.XPATH, f"//*[text()='{email}']/parent::div/div"
        user_elements = self.find_elements(locator_user)
        output_result = [el.text for el in user_elements if el.text]

        return output_result

    def delete_last_user(self):
        delete_elements = self.find_elements(self.DELETE_BUTTON)
        self.click(delete_elements[-1])

    def is_user_deleted(self, email):
        locator_user = By.XPATH, f"//*[text()='{email}']/parent::div/div"
        user_elements = self.find_elements_for_web_tables(locator_user)

        return len(user_elements) == 0

    def get_quantity_fields(self):
        quantity = self.find_elements(self.FIELDS)
        return len(quantity)

    def select_number_of_rows(self, quantity):
        row_option_locator = By.XPATH, f"//option[@value='{quantity}']"
        self.click(self.TABLE_ROWS_SELECTOR)
        self.click(row_option_locator)

    def set_search(self, search_element):
        self.send_keys(self.SEARCH_INPUT, search_element)

    def is_user_found(self, search_element):
        locator_users = By.XPATH, "//div[@class='rt-tr-group'][1]/div/div"
        user_elements = self.find_elements(locator_users)
        output_result = [el.text for el in user_elements if el.text]

        return search_element in output_result

    def click_column_to_sort(self, locator_column):
        locator = By.XPATH, f"{locator_column}"
        self.click(locator)

    def get_sorted_results(self, lap):
        locator = By.XPATH, f"//div[@class='rt-tr-group'][1]//div[@class='rt-td'][{lap}]"
        text_result = self.get_text(locator)
        return text_result


class Buttons(BasePage):
    DOUBLE_BUTTON = By.ID, "doubleClickBtn"
    RIGHT_BUTTON = By.ID, "rightClickBtn"
    CLICK_BUTTON = By.XPATH, "//div[3]/button"
    DOUBLE_CLICK_MESSAGE = By.ID, "doubleClickMessage"
    RIGHT_CLICK_MESSAGE = By.ID, "rightClickMessage"
    DYNAMIC_CLICK_MESSAGE = By.ID, "dynamicClickMessage"


    def open_button_page(self):
        self.open(BUTTONS_URL)

    def double_click_button(self):
        self.action_double_click(self.DOUBLE_BUTTON)
        text_result = self.get_text(self.DOUBLE_CLICK_MESSAGE)
        return text_result

    def right_click_button(self):
        self.action_right_click(self.RIGHT_BUTTON)
        text_result = self.get_text(self.RIGHT_CLICK_MESSAGE)
        return text_result

    def click_me_button(self):
        self.click(self.CLICK_BUTTON)
        text_result = self.get_text(self.DYNAMIC_CLICK_MESSAGE)
        return text_result

class Links(BasePage):
    HOME_LINK = By.ID, "simpleLink"
    DYNAMIC_LINK = By.ID, "dynamicLink"
    CREATED_LINK = By.ID, "created"
    NO_CONTENT_LINK = By.ID, "no-content"
    MOVED_LINK = By.ID, "moved"
    BAD_REQUEST_LINK = By.ID, "bad-request"
    UNAUTHORIZED_LINK = By.ID, "unauthorized"
    FORBIDDEN_LINK = By.ID, "forbidden"
    NOT_FOUND_LINK = By.ID, "invalid-url"

    RESPONSE_STATUS_CODE = By.XPATH, "//p[@id='linkResponse']/b[1]"
    RESPONSE_TEXT = By.XPATH, "//p[@id='linkResponse']/b[2]"


    def open_link_page(self):
        self.open(LINKS_URL)

    def click_on_the_link(self, locator):
        href_attribute = self.get_attribute(locator, "href")
        response = requests.get(href_attribute)
        if response.status_code == 200:
            self.click(locator)
            self.switch_to_new_windows()
            url = self.get_current_url()
            return url, href_attribute
        else:
            return href_attribute, response.status_code

    def click_on_the_link_api_call(self, locator):
        locator_link = By.ID, f"{locator}"
        self.click(locator_link)
        response_status_code = self.get_text(self.RESPONSE_STATUS_CODE)
        response_text = self.get_text(self.RESPONSE_TEXT)
        return response_status_code, response_text

class UploadAndDownload(BasePage):
    DOWNLOAD_BUTTON = By.ID, "downloadButton"
    UPLOAD_INPUT = By.ID, "uploadFile"
    UPLOAD_RESULT = By.ID, "uploadedFilePath"

    def open_upload_and_download_page(self):
        self.open(UPLOAD_AND_DOWNLOAD_URL)

    @staticmethod
    def wait_for_file(file_path, timeout=20):
        start = time.time()
        while time.time() - start < timeout:
            if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
                return True
            time.sleep(0.5)
        return False

    def click_download_button(self):
        file_path = r"C:\Users\adizerko\Downloads\sampleFile.jpeg"
        self.click(self.DOWNLOAD_BUTTON)
        result = self.wait_for_file(file_path)
        if result:
            os.remove(file_path)
        return result

    def upload_file(self):
        file_name, file_path = Generation.text_file()
        self.send_keys(self.UPLOAD_INPUT, file_path)
        os.remove(file_path)
        result = self.get_text(self.UPLOAD_RESULT)
        return file_name, result

