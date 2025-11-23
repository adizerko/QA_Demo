import time
from itertools import count
from random import randint

from faker.generator import random
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from curl import PRACTICE_FORM_URL
from generation import Generation
from pages.base_page import BasePage


class FormsPage(BasePage):
    NAME_INPUT = By.ID, "firstName"
    LAST_NAME_INPUT = By.ID, "lastName"
    EMAIL_INPUT = By.ID, "userEmail"
    MALE_RADIO = By.XPATH, "//input[@id='gender-radio-1']/following-sibling::label"
    FEMALE_RADIO = By.XPATH, "//input[@id='gender-radio-2']/following-sibling::label"
    OTHER_RADIO = By.XPATH, "//input[@id='gender-radio-3']/following-sibling::label"
    MOBILE_INPUT = By.ID, "userNumber"
    DATE_OF_BIRTH = By.ID, "dateOfBirthInput"
    SUBJECTS_INPUT = By.XPATH, "//input[@id='subjectsInput']"
    SUBJECTS_OPTION_ONE = By.XPATH, "//div[@id='react-select-2-option-0']"
    SPORTS_CHECKBOX = By.XPATH, "//input[@id='hobbies-checkbox-1']/following-sibling::label"
    READING_CHECKBOX = By.XPATH, "//input[@id='hobbies-checkbox-2']/following-sibling::label"
    MUSIC_CHECKBOX = By.XPATH, "//input[@id='hobbies-checkbox-3']/following-sibling::label"
    PICTURE_UPLOAD = By.ID, "uploadPicture"
    CURRENT_ADDRESS_INPUT = By.ID, "currentAddress"

    SELECT_STATE = By.XPATH, "//div[text()='Select State']"
    NCR_STATE = By.XPATH, "//div[text()='NCR']"
    UTTAR_PRADESH_STATE = By.XPATH, "//div[text()='Uttar Pradesh']"
    HARYANA_STATE = By.XPATH, "//div[text()='Haryana']"
    RAJASTHAN_STATE = By.XPATH, "//div[text()='Rajasthan']"
    DELHI_CITY = By.XPATH, "//div[text()='Delhi']"
    GURGAON_CITY = By.XPATH, "//div[text()='Gurgaon']"
    NOIDA_CITY = By.XPATH, "//div[text()='Noida']"

    SELECT_CITY = By.XPATH, "//div[text()='Select City']"
    SUBMIT_BUTTON = By.ID, "submit"

    RESULT_STUDENT_NAME = By.XPATH, "//td[text()='Student Name']/following-sibling::td"
    RESULT_STUDENT_EMAIL = By.XPATH, "//td[text()='Student Email']/following-sibling::td"
    RESULT_GENDER = By.XPATH, "//td[text()='Gender']/following-sibling::td"
    RESULT_MOBILE = By.XPATH, "//td[text()='Mobile']/following-sibling::td"
    RESULT_DATE_OF_BIRTH = By.XPATH, "//td[text()='Date of Birth']/following-sibling::td"
    RESULT_SUBJECTS = By.XPATH, "//td[text()='Subjects']/following-sibling::td"
    RESULT_HOBBIES = By.XPATH, "//td[text()='Hobbies']/following-sibling::td"
    RESULT_PICTURE = By.XPATH, "//td[text()='Picture']/following-sibling::td"
    RESULT_ADDRESS = By.XPATH, "//td[text()='Address']/following-sibling::td"
    RESULT_STATE_AND_CITY = By.XPATH, "//td[text()='State and City']/following-sibling::td"

    def open_forms_page(self):
        self.open(PRACTICE_FORM_URL)

    def set_first_name(self):
        first_name = Generation.first_name()
        self.send_keys(self.NAME_INPUT, first_name)
        return first_name

    def set_last_name(self):
        last_name = Generation.last_name()
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        return last_name

    def set_email(self):
        email = Generation.email()
        self.send_keys(self.EMAIL_INPUT, email)
        return email

    def set_gender(self):
        gender, num = Generation.gender_forms()
        locator_gender = By.XPATH, f"//input[@id='gender-radio-{num}']/following-sibling::label"
        self.click(locator_gender)
        return gender

    def set_phone_number(self):
        phone = Generation.phone_number()
        self.send_keys(self.MOBILE_INPUT, phone)
        return phone

    def set_date_of_birth(self):
        date_of_birth = Generation.date_of_birth()
        self.send_keys(self.DATE_OF_BIRTH, Keys.CONTROL + "a")
        self.clear_input_js()
        self.send_keys(self.DATE_OF_BIRTH, date_of_birth)
        self.send_keys(self.DATE_OF_BIRTH, Keys.ENTER)
        return  date_of_birth

    def set_subjects(self) -> list:
        subjects = Generation.subjects()

        for sub in subjects:
            self.send_keys(self.SUBJECTS_INPUT, sub)
            self.click(self.SUBJECTS_OPTION_ONE)
        return subjects

    def set_hobbies(self):
        self.click(self.SPORTS_CHECKBOX)
        return "Sports"

    def set_file(self):
        file_name, file_path = Generation.text_file()
        self.send_keys(self.PICTURE_UPLOAD, file_path)
        return file_name

    def set_current_address(self):
        current_address = Generation.address()
        self.send_keys(self.CURRENT_ADDRESS_INPUT, current_address)
        return current_address

    def select_state(self):
        self.click(self.SELECT_STATE)
        state = self.get_text(self.NCR_STATE)
        self.click(self.NCR_STATE)
        return state

    def select_city(self):
        self.click(self.SELECT_CITY)
        city = self.get_text(self.DELHI_CITY)
        self.click(self.DELHI_CITY)
        return city

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)