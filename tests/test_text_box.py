import time

import pytest

from conftest import driver
from data import LOCATORS_SORT_BY_COLUMN, SUCCESS_DOUBLE_CLICK_MESSAGE, SUCCESS_RIGHT_CLICK_MESSAGE, \
    SUCCESS_CLICK_MESSAGE, LOCATORS_LINKS_PAGE, LOCATORS_LINKS_API_PAGE
from generation import Generation
from pages.elements_page import TextBox, CheckBox, RadioButton, WebTables, Buttons, Links, UploadAndDownload


class TestTextBox:
    def test_text_box_success(self, driver):
        text_box_page = TextBox(driver)
        text_box_page.open_text_box_page()

        user_name, user_email, current_address, permanent_address = Generation.text_box_input()

        text_box_page.set_user_name(user_name)
        text_box_page.set_user_email(user_email)
        text_box_page.set_current_address(current_address)
        text_box_page.set_permanent_address(permanent_address)

        text_box_page.click_submit_button()

        assert text_box_page.is_user_name_correct(user_name), "Имя не совпадает"
        assert text_box_page.is_user_email_correct(user_email), "Email не совпадает"
        assert text_box_page.is_current_address_correct(current_address), "Текущий адрес не совпадает"
        assert text_box_page.is_permanent_address_correct(permanent_address), "Постоянный адрес не совпадает"

class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBox(driver)
        check_box_page.open_check_box_page()
        check_box_page.click_all_toggle()

        check_box_page.click_choosing_random_checkboxes()
        checked_elements = check_box_page.get_checked_checkbox_elements()
        result_checked_elements = check_box_page.get_result_checked_checkbox_elements()

        assert checked_elements == result_checked_elements


class TestRadioButton:
    def test_radio_button_selected_yes(self, driver):
        radio_button_page = RadioButton(driver)
        radio_button_page.open_radio_button_page()
        radio_button_page.select_radio_button_yes()
        radio_result = radio_button_page.get_radio_result()

        assert radio_result == 'Yes'

    def test_radio_button_selected_impressive(self, driver):
        radio_button_page = RadioButton(driver)
        radio_button_page.open_radio_button_page()
        radio_button_page.select_radio_button_impressive()
        radio_result = radio_button_page.get_radio_result()

        assert radio_result == 'Impressive'

    def test_radio_button_selected_no(self, driver):
        radio_button_page = RadioButton(driver)
        radio_button_page.open_radio_button_page()
        radio_button_page.select_radio_button_no()
        radio_result = radio_button_page.get_radio_result()

        assert radio_result == 'No'

class TestWebTables:

    def test_add_new_user(self, driver):
        web_tables_page = WebTables(driver)
        web_tables_page.open_web_tables_page()
        web_tables_page.add_button_click()

        input_result = web_tables_page.fill_user_form_and_get_data("yes")
        email = input_result[3]
        web_tables_page.click_submit()

        output_result = web_tables_page.get_result_new_user(email)
        assert output_result == input_result

    def test_add_new_user_and_edit(self, driver, add_new_user_web_tables_form):
        web_tables_page, email = add_new_user_web_tables_form
        web_tables_page.click_edit_button_lust_user()
        input_result_after_edit = web_tables_page.fill_user_form_and_get_data("yes")
        email = input_result_after_edit[3]
        web_tables_page.click_submit()
        output_result = web_tables_page.get_result_new_user(email)

        assert output_result == input_result_after_edit

    def test_add_new_user_and_delete(self, driver, add_new_user_web_tables_form):
        web_tables_page, email = add_new_user_web_tables_form
        web_tables_page.delete_last_user()

        assert web_tables_page.is_user_deleted(email)

    @pytest.mark.parametrize("quantity", [5,10,20,25,50,100])
    def test_rows_change_on_selection(self, driver, quantity):
        web_tables_page = WebTables(driver)
        web_tables_page.open_web_tables_page()
        web_tables_page.select_number_of_rows(quantity)
        displayed_rows = web_tables_page.get_quantity_fields()

        assert displayed_rows == quantity

    @pytest.mark.parametrize("search_element", [
        "Alden", "Cantrell", "45", "alden@example.com", "1200", "Compliance"] )
    def test_user_search(self, driver, search_element):
        web_tables_page = WebTables(driver)
        web_tables_page.open_web_tables_page()
        web_tables_page.set_search(search_element)

        assert web_tables_page.is_user_found(search_element)

    @pytest.mark.parametrize("click_column, expected_sorted_column, lap", LOCATORS_SORT_BY_COLUMN)
    def test_sorting_by_table_columns(self, driver, click_column, expected_sorted_column, lap):
        web_tables_page = WebTables(driver)
        web_tables_page.open_web_tables_page()
        web_tables_page.click_column_to_sort(click_column)
        sort_result_text = web_tables_page.get_sorted_results(lap)

        assert sort_result_text == expected_sorted_column

class TestButtons:

    def test_double_click(self, driver):
        buttons_page = Buttons(driver)
        buttons_page.open_button_page()
        text_result = buttons_page.double_click_button()

        assert text_result == SUCCESS_DOUBLE_CLICK_MESSAGE

    def test_right_click(self, driver):
        buttons_page = Buttons(driver)
        buttons_page.open_button_page()
        text_result = buttons_page.right_click_button()

        assert text_result == SUCCESS_RIGHT_CLICK_MESSAGE

    def test_dynamic_click(self, driver):
        buttons_page = Buttons(driver)
        buttons_page.open_button_page()
        text_result = buttons_page.click_me_button()

        assert text_result == SUCCESS_CLICK_MESSAGE

class TestLinks:

    @pytest.mark.parametrize("locator", LOCATORS_LINKS_PAGE)
    def test_links_open_new_tab(self, driver, locator):
        links_page = Links(driver)
        links_page.open_link_page()
        current_url, href_link = links_page.click_on_the_link(locator)

        assert current_url == href_link

    @pytest.mark.parametrize("locator, status_code_expected, response_text_expected",
                             LOCATORS_LINKS_API_PAGE)
    def test_links_api_call(
            self, driver, locator, status_code_expected, response_text_expected):
        links_page = Links(driver)
        links_page.open_link_page()
        response_status_code, response_text = links_page.click_on_the_link_api_call(locator)

        assert status_code_expected == response_status_code
        assert response_text_expected == response_text



class TestUploadAndDownload:

    def test_download_file(self, driver):
        upload_and_download_page = UploadAndDownload(driver)
        upload_and_download_page.open_upload_and_download_page()
        assert upload_and_download_page.click_download_button()

    def test_upload_file(self, driver):
        upload_page = UploadAndDownload(driver)
        upload_page.open_upload_and_download_page()
        file_name, result = upload_page.upload_file()
        assert file_name in result




