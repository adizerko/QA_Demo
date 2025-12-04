import random
import os
import time

import allure
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from curl import TEXT_BOX_URL, CHECK_BOX_URL, RADIO_BUTTON_URL, \
    WEB_TABLES_URL, BUTTONS_URL, LINKS_URL, UPLOAD_AND_DOWNLOAD_URL
from data.elements_data import CheckBoxData, UploadAndDownloadData

from generation import Generation
from locators.elements_page_locators import TextBoxPageLocators, \
    CheckBoxLocators, RadioButtonLocators, WebTablesLocators, ButtonsPageLocators, \
    LinksPageLocators, UploadAndDownloadLocators
from pages.base_page import BasePage


class TextBox(BasePage):
    locators = TextBoxPageLocators

    @allure.step("Открываем страницу Text Box")
    def open_text_box_page(self) -> None:
        self.open(TEXT_BOX_URL)

    @allure.step("Вводим имя пользователя: {user_name}")
    def set_user_name(self, user_name: str) -> None:
        self.send_keys(self.locators.USER_NAME_INPUT, user_name)

    @allure.step("Вводим email пользователя: {email}")
    def set_user_email(self, email: str) -> None:
        self.send_keys(self.locators.USER_EMAIL_INPUT, email)

    @allure.step("Вводим текущий адрес: {current_address}")
    def set_current_address(self, current_address: str) -> None:
        self.send_keys(self.locators.CURRENT_ADDRESS, current_address)

    @allure.step("Вводим постоянный адрес: {permanent_address}")
    def set_permanent_address(self, permanent_address: str) -> None:
        self.send_keys(self.locators.PERMANENT_ADDRESS, permanent_address)

    @allure.step("Кликаем на кнопку Submit")
    def click_submit_button(self) -> None:
        self.click(self.locators.SUBMIT)

    @allure.step("Проверяем корректность имени: {user_name}")
    def is_user_name_correct(self, user_name: str) -> bool:
        user_name_result = self.get_text(self.locators.USER_NAME_RESULT).split(":")[1]
        return user_name == user_name_result

    @allure.step("Проверяем корректность email: {user_email}")
    def is_user_email_correct(self, user_email: str) -> bool:
        user_email_result = self.get_text(self.locators.USER_EMAIL_RESULT).split(":")[1]
        return user_email == user_email_result

    @allure.step("Проверяем корректность текущего адреса: {user_current_address}")
    def is_current_address_correct(self, user_current_address: str) -> bool:
        user_current_address_result = self.get_text(
            self.locators.USER_CURRENT_ADDRESS_RESULT).split(":")[1]
        return user_current_address == user_current_address_result

    @allure.step("Проверяем корректность постоянного адреса: {user_permanent_address}")
    def is_permanent_address_correct(self, user_permanent_address: str) -> bool:
        user_permanent_address_result = self.get_text(
            self.locators.USER_PERMANENT_ADDRESS_RESULT).split(":")[1]
        return user_permanent_address == user_permanent_address_result


class CheckBox(BasePage):
    locators = CheckBoxLocators

    @allure.step("Открываем страницу Check Box")
    def open_check_box_page(self) -> None:
        self.open(CHECK_BOX_URL)

    @allure.step("Кликаем на корневой элемент чекбоксов")
    def click_root_toggle(self) -> None:
        element = self.wait_for_element(self.locators.ROOT_TOGGLE)
        element.click()

    @allure.step("Кликаем на Desktop")
    def click_desktop_toggle(self) -> None:
        self.click(self.locators.DESKTOP_TOGGLE)

    @allure.step("Кликаем на Documents")
    def click_documents_toggle(self) -> None:
        self.click(self.locators.DOCUMENTS_TOGGLE)

    @allure.step("Кликаем на Documents")
    def click_downloads_toggle(self) -> None:
        self.click(self.locators.DOWNLOADS_TOGGLE)

    @allure.step("Кликаем на Workspace")
    def click_workspace_toggle(self) -> None:
        self.click(self.locators.WORKSPACE_TOGGLE)

    @allure.step("Кликаем на Office")
    def click_office_toggle(self) -> None:
        self.click(self.locators.OFFICE_TOGGLE)

    @allure.step("Выбираем все чекбоксы")
    def click_all_toggle(self) -> None:
        self.click_root_toggle()
        self.click_desktop_toggle()
        self.click_documents_toggle()
        self.click_downloads_toggle()
        self.click_workspace_toggle()
        self.click_office_toggle()

    @allure.step("Выбираем случайные чекбоксы")
    def click_choosing_random_checkboxes(self) -> None:
        random_list_element_checkbox: list[str] = random.sample(
            CheckBoxData.CHECKBOX_ELEMENTS, random.randint(1, 16))

        for el in random_list_element_checkbox:
            check_box_element = By.XPATH, f"//span[text()='{el}']/parent::label/span[1]"
            with allure.step(f"Кликаем на чекбокс '{el}'"):
                self.click(check_box_element)

    @allure.step("Получаем выбранные элементы чекбоксов")
    def get_checked_checkbox_elements(self) -> list[str]:
        items: list[WebElement] = self.find_elements(self.locators.CHECKED_ITEMS)
        checked_elements = []

        for i in items:
            checked_elements.append(i.text.lower().split('.doc')[0].replace(' ', ''))
        return checked_elements

    @allure.step("Получаем результат выбранных элементов в Output")
    def get_result_checked_checkbox_elements(self) -> list[str]:
        items: list[WebElement] = self.find_elements(self.locators.OUTPUT_RESULT)
        result_checked_elements = []

        for i in items:
            result_checked_elements.append(i.text.lower().replace(' ', ''))
        return result_checked_elements


class RadioButton(BasePage):
    locators = RadioButtonLocators

    @allure.step("Открываем страницу Radio Button")
    def open_radio_button_page(self) -> None:
        self.open(RADIO_BUTTON_URL)

    @allure.step("Выбираем радио-кнопку 'Yes'")
    def select_radio_button_yes(self) -> None:
        self.click(self.locators.YES_RADIO)

    @allure.step("Выбираем радио-кнопку 'Impressive'")
    def select_radio_button_impressive(self) -> None:
        self.click(self.locators.IMPRESSIVE_RADIO)

    @allure.step("Выбираем радио-кнопку 'No'")
    def select_radio_button_no(self) -> None:
        self.click(self.locators.NO_RADIO)

    @allure.step("Получаем результат выбранной радио-кнопки")
    def get_radio_result(self) -> str:
        return self.get_text(self.locators.SELECTED)


class WebTables(BasePage):
    locators = WebTablesLocators

    @allure.step("Открываем страницу Web Tables")
    def open_web_tables_page(self) -> None:
        self.open(WEB_TABLES_URL)

    @allure.step("Открываем страницу Web Tables")
    def add_button_click(self) -> None:
        self.click(self.locators.ADD_BUTTON)

    @allure.step("Открываем страницу Web Tables")
    def click_edit_button_lust_user(self) -> None:
        self.click(self.locators.EDIT_BUTTON_LAST_USER)

    @allure.step("Заполняем поле 'First Name'")
    def set_first_name(self) -> str:
        first_name = Generation.first_name()
        self.send_keys(self.locators.FIRST_NAME_INPUT, first_name)
        return first_name

    @allure.step("Заполняем поле 'First Name'")
    def set_last_name(self) -> str:
        last_name = Generation.last_name()
        self.send_keys(self.locators.LAST_NAME_INPUT, last_name)
        return last_name

    @allure.step("Заполняем поле 'First Name'")
    def set_email(self) -> str:
        email = Generation.email()
        self.send_keys(self.locators.EMAIL_INPUT, email)
        return email

    @allure.step("Заполняем поле 'Age'")
    def set_age(self) -> str:
        age = Generation.age()
        self.send_keys(self.locators.AGE_INPUT, age)
        return age

    @allure.step("Заполняем поле 'Salary'")
    def set_salary(self) -> str:
        salary = Generation.salary()
        self.send_keys(self.locators.SALARY_INPUT, salary)
        return salary

    @allure.step("Заполняем поле 'Department'")
    def set_department(self) -> str:
        department = Generation.department()
        self.send_keys(self.locators.DEPARTMENT_INPUT, department)
        return department

    @allure.step("Нажимаем кнопку 'Submit'")
    def click_submit(self) -> None:
        self.click(self.locators.SUBMIT_BUTTON)

    @allure.step("Заполняем форму пользователя и получаем данные")
    def fill_user_form_and_get_data(self, returned: str = "no", ) -> list[str] | None:
        first = self.set_first_name()
        last = self.set_last_name()
        email = self.set_email()
        age = self.set_age()
        salary = self.set_salary()
        dept = self.set_department()

        if returned == "yes":
            return [first, last, age, email, salary, dept]
        return None

    @allure.step("Получаем данные нового пользователя по email: {email}")
    def get_result_new_user(self, email: str) -> list[str]:
        locator_user = By.XPATH, f"//*[text()='{email}']/parent::div/div"
        user_elements = self.find_elements(locator_user)
        output_result = [el.text for el in user_elements if el.text]
        return output_result

    @allure.step("Удаляем последнего пользователя")
    def delete_last_user(self) -> None:
        delete_elements = self.find_elements(self.locators.DELETE_BUTTON)
        delete_elements[-1].click()

    @allure.step("Проверяем, что пользователь с email {email} удалён")
    def is_user_deleted(self, email: str) -> bool:
        locator_user = By.XPATH, f"//*[text()='{email}']/parent::div/div"
        user_elements = self.find_elements_for_web_tables(locator_user)
        return len(user_elements) == 0

    @allure.step("Получаем количество полей в таблице")
    def get_quantity_fields(self) -> int:
        quantity = self.find_elements(self.locators.FIELDS)
        return len(quantity)

    @allure.step("Выбираем количество отображаемых строк: {quantity}")
    def select_number_of_rows(self, quantity: int) -> None:
        row_option_locator = By.XPATH, f"//option[@value='{quantity}']"
        self.click(self.locators.TABLE_ROWS_SELECTOR)
        self.click(row_option_locator)

    @allure.step("Вводим текст '{search_element}' в поле поиска")
    def set_search(self, search_element: str) -> None:
        self.send_keys(self.locators.SEARCH_INPUT, search_element)

    @allure.step("Проверяем, что пользователь '{search_element}' найден")
    def is_user_found(self, search_element: str) -> bool:
        locator_users = By.XPATH, "//div[@class='rt-tr-group'][1]/div/div"
        user_elements = self.find_elements(locator_users)
        output_result = [el.text for el in user_elements if el.text]
        return search_element in output_result

    @allure.step("Сортируем колонку {locator_column}")
    def click_column_to_sort(self, locator_column: str) -> None:
        locator = By.XPATH, f"{locator_column}"
        self.click(locator)

    @allure.step("Получаем результат сортировки колонки номер {lap}")
    def get_sorted_results(self, lap: int) -> str:
        locator = By.XPATH, f"//div[@class='rt-tr-group'][1]//div[@class='rt-td'][{lap}]"
        text_result = self.get_text(locator)
        return text_result


class Buttons(BasePage):
    locators = ButtonsPageLocators

    @allure.step("Открываем страницу кнопок")
    def open_button_page(self) -> None:
        self.open(BUTTONS_URL)

    @allure.step("Двойной клик по кнопке")
    def double_click_button(self) -> str:
        self.action_double_click(self.locators.DOUBLE_BUTTON)
        return self.get_text(self.locators.DOUBLE_CLICK_MESSAGE)

    @allure.step("Клик правой кнопкой по кнопке")
    def right_click_button(self) -> str:
        self.action_right_click(self.locators.RIGHT_BUTTON)
        return self.get_text(self.locators.RIGHT_CLICK_MESSAGE)

    @allure.step("Обычный клик по кнопке")
    def click_me_button(self) -> str:
        self.click(self.locators.CLICK_BUTTON)
        return self.get_text(self.locators.DYNAMIC_CLICK_MESSAGE)


class Links(BasePage):
    locators = LinksPageLocators

    @allure.step("Открываем страницу ссылок")
    def open_link_page(self) -> None:
        self.open(LINKS_URL)

    @allure.step("Кликаем по ссылке и проверяем статус через requests")
    def click_on_the_link(
            self,
            locator: tuple[str, str]
    ) -> tuple[str, str | None] | tuple[str | None, int]:
        href_attribute = str(self.get_attribute(locator, "href"))
        response = requests.get(href_attribute)

        if response.status_code == 200:
            self.click(locator)
            self.switch_to_new_windows()
            url = self.get_current_url()
            return url, href_attribute
        else:
            return href_attribute, response.status_code

    @allure.step("Кликаем по ссылке с API вызовом")
    def click_on_the_link_api_call(self, locator: str) -> tuple[str, str]:
        locator_link = By.ID, f"{locator}"
        self.click(locator_link)
        response_status_code = self.get_text(self.locators.RESPONSE_STATUS_CODE)
        response_text = self.get_text(self.locators.RESPONSE_TEXT)
        return response_status_code, response_text


class UploadAndDownload(BasePage):
    locators =  UploadAndDownloadLocators

    @allure.step("Открываем страницу загрузки и скачивания файлов")
    def open_upload_and_download_page(self) -> None:
        self.open(UPLOAD_AND_DOWNLOAD_URL)

    @staticmethod
    @allure.step("Ожидание появления файла: {file_path}")
    def wait_for_file(file_path, timeout: int = 20) -> bool:
        start = time.time()

        while time.time() - start < timeout:
            if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
                return True
            time.sleep(0.5)
        return False

    @allure.step("Скачиваем файл")
    def click_download_button(self) -> bool:
        file_name = "sampleFile.jpeg"
        file_path = os.path.join(UploadAndDownloadData.DOWNLOADS_DIR, file_name)
        self.click(self.locators.DOWNLOAD_BUTTON)
        result = self.wait_for_file(file_path)

        if result:
            os.remove(file_path)
        return result

    @allure.step("Загружаем файл")
    def upload_file(self) -> tuple[str, str]:
        file_name, file_path = Generation.text_file()
        self.send_keys(self.locators.UPLOAD_INPUT, file_path)
        result = self.get_text(self.locators.UPLOAD_RESULT)
        os.remove(file_path)
        return file_name, result
