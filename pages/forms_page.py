import random
from typing import Any

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from curl import PRACTICE_FORM_URL
from generation import Generation
from locators.interactions_page_locators import FormsPageLocators
from pages.base_page import BasePage


class FormsPage(BasePage):
    locators = FormsPageLocators

    @allure.step("Открывает страницу формы")
    def open_forms_page(self) -> None:
        self.open(PRACTICE_FORM_URL)

    @allure.step("Заполняем имя")
    def set_first_name(self) -> str:
        first_name = Generation.first_name()
        self.send_keys(self.locators.NAME_INPUT, first_name)
        return first_name

    @allure.step("Заполняем фамилию")
    def set_last_name(self) -> str:
        last_name = Generation.last_name()
        self.send_keys(self.locators.LAST_NAME_INPUT, last_name)
        return last_name

    @allure.step("Заполняем email")
    def set_email(self) -> str:
        email = Generation.email()
        self.send_keys(self.locators.EMAIL_INPUT, email)
        return email

    @allure.step("Выбираем пол:")
    def set_gender(self) -> str:
        gender, num = Generation.gender_forms()
        locator_gender = By.XPATH, f"//input[@id='gender-radio-{num}']/following-sibling::label"
        self.click(locator_gender)
        return gender

    @allure.step("Заполняем номер телефона")
    def set_phone_number(self) -> str:
        phone = Generation.phone_number()
        self.send_keys(self.locators.MOBILE_INPUT, phone)
        return str(phone)

    @allure.step("Устанавливаем дату рождения")
    def set_date_of_birth(self) -> str:
        date_of_birth = Generation.date_of_birth()
        self.send_keys(self.locators.DATE_OF_BIRTH, Keys.CONTROL + "a")
        self.clear_input_js("dateOfBirthInput")
        self.send_keys(self.locators.DATE_OF_BIRTH, date_of_birth)
        self.send_keys(self.locators.DATE_OF_BIRTH, Keys.ENTER)
        return  date_of_birth

    @allure.step("Выбираем предметы")
    def set_subjects(self) -> str:
        subjects = Generation.subjects()

        for sub in subjects:
            self.send_keys(self.locators.SUBJECTS_INPUT, sub)
            self.click(self.locators.SUBJECTS_OPTION_ONE)
        return ", ".join(subjects)

    @allure.step("Выбираем хобби")
    def set_hobbies(self) -> str:
        num_hobbies_to_select = random.randint(1, 3)
        hobby_indexes = random.sample(range(1, 4), num_hobbies_to_select)
        selected_hobbies = []
        hobby_labels = {1: "Sports", 2: "Reading", 3: "Music"}

        for index in hobby_indexes:
            locator = By.XPATH, f"//input[@id='hobbies-checkbox-{index}']/following-sibling::label"
            self.click(locator)
            selected_hobbies.append(hobby_labels[index])

        return ", ".join(selected_hobbies)

    @allure.step("Загружаем файл")
    def set_file(self) -> str:
        file_name, file_path = Generation.text_file()
        self.send_keys(self.locators.PICTURE_UPLOAD, file_path)
        return file_name

    @allure.step("Заполняем адрес")
    def set_current_address(self) -> str:
        current_address = Generation.address()
        self.send_keys(self.locators.CURRENT_ADDRESS_INPUT, current_address)
        return current_address

    @allure.step("Выбираем штат и город")
    def select_state_and_city(self) -> tuple[Any, Any]:
        state, city = Generation.state_and_city()
        state_locator = By.XPATH, f"//div[text()='{state}']"
        city_locator = By.XPATH, f"//div[text()='{city}']"
        self.click(self.locators.SELECT_STATE)
        self.click(state_locator)
        state = self.get_text(state_locator)
        self.click(self.locators.SELECT_CITY)
        self.click(city_locator)
        return state, city

    @allure.step("Нажимаем кнопку Submit")
    def click_submit(self) -> None:
        self.click(self.locators.SUBMIT_BUTTON)

    @allure.step("Заполняем всю форму")
    def fill_form_data(self) -> dict[str, str]:
        first_name: str = self.set_first_name()
        last_name: str = self.set_last_name()
        email: str = self.set_email()
        gender: str = self.set_gender()
        mobile: str = self.set_phone_number()
        date_of_birth: str = self.set_date_of_birth()
        subjects: str = self.set_subjects()
        hobbies: str = self.set_hobbies()
        file_name: str = self.set_file()
        address: str = self.set_current_address()
        state, city = self.select_state_and_city()

        form_data = {
            "student name": f"{first_name} {last_name}",
            "email": email,
            "gender": gender,
            "mobile": mobile,
            "date of birth": date_of_birth,
            "subjects": subjects,
            "hobbies": hobbies,
            "file name": file_name,
            "address": address,
            "state and city": f"{state} {city}"
        }

        return form_data

    @allure.step("Получаем данные с окна результата")
    def get_result_from_data(self) -> dict[str, str]:
        student_name_result: str = self.get_text(self.locators.RESULT_STUDENT_NAME)
        email: str = self.get_text(self.locators.RESULT_STUDENT_EMAIL)
        gender: str = self.get_text(self.locators.RESULT_GENDER)
        mobile: str = self.get_text(self.locators.RESULT_MOBILE)
        date_of_birth: str = self.get_text(self.locators.RESULT_DATE_OF_BIRTH)
        subjects: str = self.get_text(self.locators.RESULT_SUBJECTS)
        hobbies: str = self.get_text(self.locators.RESULT_HOBBIES)
        file: str = self.get_text(self.locators.RESULT_PICTURE)
        address : str = self.get_text(self.locators.RESULT_ADDRESS)
        state_and_city: str = self.get_text(self.locators.RESULT_STATE_AND_CITY)

        result = {"student name" :student_name_result,
                  "email" :email,
                  "gender" :gender,
                  "mobile" :mobile,
                  "date of birth" :date_of_birth,
                  "subjects" : subjects,
                  "hobbies" :hobbies,
                  "file name" :file,
                  "address" : address,
                  "state and city" :state_and_city}

        return result
