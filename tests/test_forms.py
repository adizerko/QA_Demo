import allure

from pages.forms_page import FormsPage

@allure.feature("Форма регистрации")
class TestForms:
    @allure.story("Отправка формы с корректными данными и проверка результата")
    def test_submit_practice_form_with_valid_data_displays_correct_results(self, driver):
        forms_page = FormsPage(driver)
        forms_page.open_forms_page()
        form_data = forms_page.fill_form_data()
        forms_page.click_submit()

        result = forms_page.get_result_from_data()

        assert form_data["student name"] == result["student name"]
        assert form_data["email"] == result["email"]
        assert form_data["gender"] == result["gender"]
        assert form_data["mobile"] == result["mobile"]
        assert form_data["date of birth"] == result["date of birth"]
        assert form_data["subjects"] == result["subjects"]
        assert form_data["hobbies"] == result["hobbies"]
        assert form_data["file name"] == result["file name"]
        assert form_data["address"] == result["address"]
        assert form_data["state and city"] == result["state and city"]
