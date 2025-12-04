from typing import Tuple

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from data import WebTablesData, ButtonsData, LinksData, RadioButtonData
from generation import Generation
from pages.elements_page import TextBox, CheckBox, RadioButton, WebTables, Buttons, Links, UploadAndDownload


@allure.suite("Elements")
class TestElements:

    @allure.feature("Text Box")
    class TestTextBox:

        @allure.title("Проверка успешного заполнения Text Box")
        def test_text_box_success(self, driver: WebDriver) -> None:
            text_box_page = TextBox(driver)
            text_box_page.open_text_box_page()

            user_name, user_email, current_address, permanent_address\
                = Generation.text_box_input()

            text_box_page.set_user_name(user_name)
            text_box_page.set_user_email(user_email)
            text_box_page.set_current_address(current_address)
            text_box_page.set_permanent_address(permanent_address)

            text_box_page.click_submit_button()

            assert text_box_page.is_user_name_correct(user_name),\
                "Имя не совпадает"

            assert text_box_page.is_user_email_correct(user_email),\
                "Email не совпадает"

            assert text_box_page.is_current_address_correct(current_address),\
                "Текущий адрес не совпадает"

            assert text_box_page.is_permanent_address_correct(permanent_address),\
                "Постоянный адрес не совпадает"

    @allure.feature("Check Box")
    class TestCheckBox:

        @allure.title("Тест выбора чекбоксов и проверки результатов")
        def test_check_box(self, driver: WebDriver):
            check_box_page = CheckBox(driver)
            check_box_page.open_check_box_page()
            check_box_page.click_all_toggle()

            check_box_page.click_choosing_random_checkboxes()
            checked_elements = check_box_page.get_checked_checkbox_elements()
            result_checked_elements = check_box_page.get_result_checked_checkbox_elements()

            assert checked_elements == result_checked_elements,\
                "Результаты чекбоксов не совпадают"

    @allure.feature("Radio Button")
    class TestRadioButton:

        @allure.title("Проверка выбора радио-кнопки 'Yes'")
        def test_radio_button_selected_yes(self, driver: WebDriver):
            radio_button_page = RadioButton(driver)
            radio_button_page.open_radio_button_page()
            radio_button_page.select_radio_button_yes()
            radio_result = radio_button_page.get_radio_result()

            assert radio_result == RadioButtonData.RADIO_YES,\
                "Выбрана неверная радио-кнопка"

        @allure.title("Проверка выбора радио-кнопки 'Impressive'")
        def test_radio_button_selected_impressive(self, driver: WebDriver):
            radio_button_page = RadioButton(driver)
            radio_button_page.open_radio_button_page()
            radio_button_page.select_radio_button_impressive()
            radio_result = radio_button_page.get_radio_result()

            assert radio_result == RadioButtonData.RADIO_IMPRESSIVE,\
                "Выбрана неверная радио-кнопка"

        @allure.title("Проверка выбора радио-кнопки 'No'")
        def test_radio_button_selected_no(self, driver: WebDriver):
            radio_button_page = RadioButton(driver)
            radio_button_page.open_radio_button_page()
            radio_button_page.select_radio_button_no()
            radio_result = radio_button_page.get_radio_result()

            assert radio_result == RadioButtonData.RADIO_NO,\
                "Выбрана неверная радио-кнопка"

    @allure.feature("Web Tables")
    class TestWebTables:

        @allure.title("Добавление нового пользователя")
        def test_add_new_user(self, driver: WebDriver) -> None:
            web_tables_page = WebTables(driver)
            web_tables_page.open_web_tables_page()
            web_tables_page.add_button_click()
            input_result = web_tables_page.fill_user_form_and_get_data("yes")
            email = input_result[3]
            web_tables_page.click_submit()
            output_result = web_tables_page.get_result_new_user(email)

            assert output_result == input_result,\
                "Данные нового пользователя не совпадают"

        @allure.title("Редактирование последнего пользователя")
        def test_add_new_user_and_edit(
                self,
                driver: WebDriver,
                add_new_user_web_tables_form: Tuple[WebTables, str]
        ) -> None:
            web_tables_page, email = add_new_user_web_tables_form
            web_tables_page.click_edit_button_lust_user()
            input_result_after_edit = web_tables_page.fill_user_form_and_get_data("yes")
            email = input_result_after_edit[3]
            web_tables_page.click_submit()
            output_result = web_tables_page.get_result_new_user(email)

            assert output_result == input_result_after_edit,\
                "Данные пользователя после редактирования не совпадают"

        @allure.title("Удаление последнего пользователя")
        def test_add_new_user_and_delete(
                self,
                driver: WebDriver,
                add_new_user_web_tables_form: Tuple[WebTables, str]
        ) -> None:
            web_tables_page, email = add_new_user_web_tables_form
            web_tables_page.delete_last_user()

            assert web_tables_page.is_user_deleted(email), "Пользователь не удалён"

        @allure.title("Изменение количества отображаемых строк")
        @pytest.mark.parametrize("quantity", WebTablesData.TABLE_ROWS_OPTIONS)
        def test_rows_change_on_selection(self, driver: WebDriver, quantity: int) -> None:
            web_tables_page = WebTables(driver)
            web_tables_page.open_web_tables_page()
            web_tables_page.select_number_of_rows(quantity)
            displayed_rows = web_tables_page.get_quantity_fields()

            assert displayed_rows == quantity, \
                f"Отображено {displayed_rows} строк, ожидалось {quantity}"

        @allure.title("Поиск пользователя по значению {search_element}")
        @pytest.mark.parametrize("search_element", WebTablesData.SEARCH_TEST_DATA)
        def test_user_search(self, driver: WebDriver, search_element: str) -> None:
            web_tables_page = WebTables(driver)
            web_tables_page.open_web_tables_page()
            web_tables_page.set_search(search_element)

            assert web_tables_page.is_user_found(search_element), \
                f"Пользователь {search_element} не найден"

        @allure.title("Сортировка таблицы по колонке {click_column}")
        @pytest.mark.parametrize("click_column, expected_sorted_column, lap", WebTablesData.LOCATORS_SORT_BY_COLUMN)
        def test_sorting_by_table_columns(
                self,
                driver: WebDriver,
                click_column: str,
                expected_sorted_column: str,
                lap: int
        ) -> None:
            web_tables_page = WebTables(driver)
            web_tables_page.open_web_tables_page()
            web_tables_page.click_column_to_sort(click_column)
            sort_result_text = web_tables_page.get_sorted_results(lap)

            assert sort_result_text == expected_sorted_column, \
                f"Сортировка по колонке {click_column} некорректна"

    @allure.feature("Buttons")
    class TestButtons:

        @allure.title("Проверка двойного клика по кнопке")
        def test_double_click(self, driver: WebDriver):
            buttons_page = Buttons(driver)
            buttons_page.open_button_page()
            text_result: str = buttons_page.double_click_button()

            assert text_result == ButtonsData.SUCCESS_DOUBLE_CLICK_MESSAGE, \
                "Неверное сообщение после двойного клика"

        @allure.title("Проверка клика правой кнопкой по кнопке")
        def test_right_click(self, driver: WebDriver):
            buttons_page = Buttons(driver)
            buttons_page.open_button_page()
            text_result: str = buttons_page.right_click_button()

            assert text_result == ButtonsData.SUCCESS_RIGHT_CLICK_MESSAGE, \
                 "Неверное сообщение после клика правой кнопкой"

        @allure.title("Проверка обычного клика по кнопке")
        def test_dynamic_click(self, driver: WebDriver):
            buttons_page = Buttons(driver)
            buttons_page.open_button_page()
            text_result: str = buttons_page.click_me_button()

            assert text_result == ButtonsData.SUCCESS_CLICK_MESSAGE, \
                "Неверное сообщение после обычного клика"

    class TestLinks:

        @allure.title("Проверка открытия ссылок в новой вкладке")
        @pytest.mark.parametrize("locator", LinksData.LOCATORS_LINKS_PAGE)
        def test_links_open_new_tab(self, driver: WebDriver, locator: tuple[str, str]) -> None:
            links_page = Links(driver)
            links_page.open_link_page()
            current_url, href_link = links_page.click_on_the_link(locator)

            assert current_url == href_link, \
                f"Ссылка не открылась корректно: ожидалось {href_link}, получено {current_url}"

        @allure.title("Проверка API вызова по ссылкам")
        @pytest.mark.parametrize("locator, status_code_expected, response_text_expected",
                                 LinksData.LOCATORS_LINKS_API_PAGE)
        def test_links_api_call(
                self,
                driver: WebDriver,
                locator: str,
                status_code_expected: str,
                response_text_expected: str
        ) -> None:
            links_page = Links(driver)
            links_page.open_link_page()
            response_status_code, response_text = links_page.click_on_the_link_api_call(locator)

            assert status_code_expected == response_status_code, \
                "Неверный статус код"

            assert response_text_expected == response_text, \
                "Неверный текст ответа"

    @allure.feature("Upload and Download Page")
    class TestUploadAndDownload:

        @allure.title("Скачивание файла")
        def test_download_file(self, driver: WebDriver) -> None:
            upload_and_download_page = UploadAndDownload(driver)
            upload_and_download_page.open_upload_and_download_page()

            assert upload_and_download_page.click_download_button(),\
                "Файл не был загружен"

        @allure.title("Загрузка файла")
        def test_upload_file(self, driver: WebDriver) -> None:
            upload_page = UploadAndDownload(driver)
            upload_page.open_upload_and_download_page()
            file_name, result = upload_page.upload_file()

            assert file_name in result, "Загруженный файл не найден в результате"
