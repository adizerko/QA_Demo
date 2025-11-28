import allure
import pytest

from conftest import driver
from data import AccordianData, AutoCompleteData, TabsData
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage


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

    @allure.feature("Slider")
    class TestSlider:

        @allure.title("Проверяем перемещение ползунка")
        def test_slider_moves_when_dragged(self, driver):
            slider_page = SliderPage(driver)
            slider_page.open_slider_page()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after

    @allure.feature("Progress Bar")
    class TestProgressBar:
        @allure.title("Прогресс-бар запускается после нажатия Start")
        def test_progress_bar_is_running_after_start_click(self, driver):
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open_progress_bar_page()
            initial_value, finished_value = progress_bar_page.start_and_get_progress()

            assert initial_value < finished_value

        @allure.title("Прогресс-бар останавливается после нажатия Stop")
        def test_progress_bar_stops_after_click_stop(self, driver):
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open_progress_bar_page()
            stop_value, value_after_wait = progress_bar_page.stop_progress_bar_and_get_values()

            assert stop_value == value_after_wait

        @allure.title("Прогресс-бар сбрасывается в 0 после нажатия Reset")
        def test_progress_bar_resets_to_zero_after_reset_click(self, driver):
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open_progress_bar_page()
            value_before_reset, value_after_reset = progress_bar_page.reset_progress_bar_and_get_values()

            assert value_before_reset != value_after_reset
            assert value_after_reset == '0'

    @allure.feature("Tabs")
    class TestTabs:
        @allure.title("Проверка отображения корректного контента при переключении вкладок")
        @pytest.mark.parametrize(
            "tab, text, expected_text", TabsData.TABS_TEST_DATA,
            ids=["What", "Origin", "Use"])
        def test_tab_content_is_displayed_after_click(
                self, driver, tab, text, expected_text):
            tabs_page = TabsPage(driver)
            tabs_page.open_tabs_page()
            tabs_page.click_tab(tab)
            text_actual = tabs_page.get_tab_text(text)

            assert text_actual == expected_text

        @allure.title("Активная вкладка имеет aria-selected = true")
        @pytest.mark.parametrize(
            "tab, expected_value", TabsData.ACTIVE_TABS,
            ids=["WHAT", "ORIGIN", "USE"])
        def test_active_tab_has_aria_selected_true(
                self, driver, tab, expected_value):
            tabs_page = TabsPage(driver)
            tabs_page.open_tabs_page()
            tabs_page.click_tab(tab)

            assert tabs_page.is_tab_active(tab)
