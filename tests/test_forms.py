import time

from pages.forms_page import FormsPage


class TestForms:
    def test_submit_practice_form_with_valid_data_displays_correct_results(self, driver):
        forms_page = FormsPage(driver)
        forms_page.open_forms_page()
        first_name = forms_page.set_first_name()
        last_name = forms_page.set_last_name()
        email = forms_page.set_email()
        gender = forms_page.set_gender()
        phone = forms_page.set_phone_number()
        date_of_birth = forms_page.set_date_of_birth()
        subjects = forms_page.set_subjects()
        hobbies = forms_page.set_hobbies()
        file_name = forms_page.set_file()
        current_address = forms_page.set_current_address()
        state = forms_page.select_state()
        city = forms_page.select_city()
        forms_page.click_submit()
