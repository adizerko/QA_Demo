import allure
import pytest

from conftest import driver
from data import AccordianData, AutoCompleteData
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage


@allure.suite("Widgets")
class TestWidgets:
    @allure.feature("Accordian")
    class TestAccordian:

        @allure.title("Проверка, что первая секция открыта по умолчанию")
        def test_first_section_default_state_is_open(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open_accordian_page()
            attribute = accordian_page.get_attribute_section_first()
            assert attribute == "collapse show"

        @pytest.mark.parametrize(
            "locator_section, expected_title", AccordianData.SECTION_TITLES)
        def test_section_title_is_correct(
                self, driver, locator_section, expected_title):
            allure.dynamic.title(f"Проверка заголовка секции: {expected_title}")
            accordian_page = AccordianPage(driver)
            accordian_page.open_accordian_page()
            title_text = accordian_page.get_text_title_section(locator_section)

            assert title_text == expected_title

        @allure.title("Проверка текста всех секций после кликов")
        def test_sections_content_is_correct_after_clicks(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open_accordian_page()
            text_first_section = accordian_page.get_text_first_section()
            accordian_page.click_second_section()
            text_second_section = accordian_page.get_text_second_section()
            accordian_page.click_third_section()
            text_third_section = accordian_page.get_text_third_section()

            assert text_first_section == AccordianData.FIRST_SECTION_TEXT_EXPECTED
            assert text_second_section == AccordianData.SECOND_SECTION_TEXT_EXPECTED
            assert text_third_section == AccordianData.THIRD_SECTION_TEXT_EXPECTED


    @allure.feature("Auto Complete")
    class TestAutoComplete:

        @allure.title("Проверка подсказок автозаполнения поля")
        @pytest.mark.parametrize("input_field", AutoCompleteData.INPUT_FIELDS,
                                 ids=["multiple", "single"])
        def test_auto_complete_suggestions(self, driver, input_field):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            expected_suggestions, actual_suggestions = (
                auto_complete_page.get_suggestions_for_random_letter(input_field))

            assert expected_suggestions == actual_suggestions

        @allure.title("Удаление одного тега из multiple поля")
        def test_tag_is_removed_after_click_close_icon(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            auto_complete_page.set_random_color_in_multiple_field(1)
            auto_complete_page.delete_tag()
            tags = auto_complete_page.is_tag_list_empty()

            assert len(tags) == 0

        @allure.title("Удаление всех тегов из multiple поля")
        def test_delete_all_tags_from_multiple_field(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            auto_complete_page.set_random_color_in_multiple_field(3)
            auto_complete_page.delete_all_tags()
            tags = auto_complete_page.is_tag_list_empty()

            assert len(tags) == 0

        @allure.title("Добавление {quantity_tags} тегов в multiple поле")
        @pytest.mark.parametrize("quantity_tags", [1,5,9,10])
        def test_test_add_multiple_tags(self, driver, quantity_tags: int):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            auto_complete_page.set_random_color_in_multiple_field(quantity_tags)
            auto_complete_page.delete_all_tags()
            tags = auto_complete_page.is_tag_list_empty()

            assert len(tags) == 0


    @allure.feature("Date Picker")
    class TestDatePicker:
        @allure.title("Выбор случайной даты через ручной ввод")
        def test_select_random_date_manual_input_valid_date(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_expected = date_picker_page.set_date()
            date_actual = date_picker_page.get_date_value()

            assert date_expected == date_actual

        @allure.title("Выбор даты с помощью календаря")
        def test_select_date_using_calendar(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_picker_page.open_calendar()
            date_expected = date_picker_page.select_random_date()
            date_actual = date_picker_page.get_date_value()

            assert date_actual == date_expected

        @allure.title("Выбор случайной даты и времени через ручной ввод")
        def test_select_random_date_and_time_manual_input(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_expected = date_picker_page.set_date_and_time()
            date_actual = date_picker_page.get_date_and_time_value()

            assert date_expected == date_actual

        @allure.title("Выбор даты и времени с помощью календаря")
        def test_select_date_and_tim_using_calendar(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_picker_page.open_calendar_date_and_time()
            date_expected = date_picker_page.select_random_date_and_time()
            date_actual = date_picker_page.get_date_and_time_value()

            assert date_expected == date_actual
