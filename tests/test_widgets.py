import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from data import AccordianData, AutoCompleteData, TabsData, ToolTipsData, MenuData
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, \
    SliderPage, ProgressBarPage, TabsPage, ToolTipsPage, MenuPage, SelectMenuPage


@allure.suite("Widgets")
class TestWidgets:

    @allure.feature("Accordian")
    class TestAccordian:

        @allure.title("Проверка, что первая секция открыта по умолчанию")
        def test_first_section_default_state_is_open(self, driver: WebDriver) -> None:
            accordian_page = AccordianPage(driver)
            accordian_page.open_accordian_page()
            attribute = accordian_page.get_attribute_section_first()
            assert attribute == "collapse show",\
                f"Первая секция должна быть открыта по умолчанию, но атрибут = '{attribute}'"

        @pytest.mark.parametrize(
            "locator_section, expected_title", AccordianData.SECTION_TITLES)
        def test_section_title_is_correct(
                self,
                driver: WebDriver,
                locator_section: tuple[str, str],
                expected_title: str
        )  -> None:
            allure.dynamic.title(f"Проверка заголовка секции: {expected_title}")
            accordian_page = AccordianPage(driver)
            accordian_page.open_accordian_page()
            title_text = accordian_page.get_text_title_section(locator_section)

            assert title_text == expected_title,\
                f"Ожидался заголовок секции '{expected_title}', но получен '{title_text}'"

        @allure.title("Проверка текста всех секций после кликов")
        def test_sections_content_is_correct_after_clicks(self, driver: WebDriver) -> None:
            accordian_page = AccordianPage(driver)
            accordian_page.open_accordian_page()
            text_first_section = accordian_page.get_text_first_section()
            accordian_page.click_second_section()
            text_second_section = accordian_page.get_text_second_section()
            accordian_page.click_third_section()
            text_third_section = accordian_page.get_text_third_section()

            assert text_first_section == AccordianData.FIRST_SECTION_TEXT_EXPECTED,\
                "Текст первой секции неверный"

            assert text_second_section == AccordianData.SECOND_SECTION_TEXT_EXPECTED, \
                "Текст второй секции неверный"

            assert text_third_section == AccordianData.THIRD_SECTION_TEXT_EXPECTED,\
                "Текст третьей секции неверный"

    @allure.feature("Auto Complete")
    class TestAutoComplete:

        @allure.title("Проверка подсказок автозаполнения поля")
        @pytest.mark.parametrize("input_field",
                                 AutoCompleteData.INPUT_FIELDS,
                                 ids=["multiple", "single"])
        def test_auto_complete_suggestions(
                self,
                driver: WebDriver,
                input_field: tuple[str, str]
        ) -> None:
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            expected_suggestions, actual_suggestions = (
                auto_complete_page.get_suggestions_for_random_letter(input_field))

            assert expected_suggestions == actual_suggestions,\
                f"Ожидались подсказки {expected_suggestions}, но получили {actual_suggestions}"

        @allure.title("Удаление одного тега из multiple поля")
        def test_tag_is_removed_after_click_close_icon(self, driver: WebDriver) -> None:
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            auto_complete_page.set_random_color_in_multiple_field(1)
            auto_complete_page.delete_tag()
            tags = auto_complete_page.is_tag_list_empty()

            assert len(tags) == 0, \
                f"Ожидалось, что список тегов пустой, но найдено {len(tags)} тегов"

        @allure.title("Удаление всех тегов из multiple поля")
        def test_delete_all_tags_from_multiple_field(self, driver: WebDriver) -> None:
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            auto_complete_page.set_random_color_in_multiple_field(3)
            auto_complete_page.delete_all_tags()
            tags = auto_complete_page.is_tag_list_empty()

            assert len(tags) == 0, \
                f"Ожидалось, что список тегов пустой, но найдено {len(tags)} тегов"

        @allure.title("Добавление {quantity_tags} тегов в multiple поле")
        @pytest.mark.parametrize("quantity_tags", [1,5,9,10])
        def test_test_add_multiple_tags(self, driver: WebDriver, quantity_tags: int) -> None:
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open_auto_complete_page()
            auto_complete_page.set_random_color_in_multiple_field(quantity_tags)
            auto_complete_page.delete_all_tags()
            tags = auto_complete_page.is_tag_list_empty()

            assert len(tags) == 0, \
                f"Ожидалось, что список тегов пустой, но найдено {len(tags)} тегов"

    @allure.feature("Date Picker")
    class TestDatePicker:

        @allure.title("Выбор случайной даты через ручной ввод")
        def test_select_random_date_manual_input_valid_date(self, driver: WebDriver) -> None:
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_expected = date_picker_page.set_date()
            date_actual = date_picker_page.get_date_value()

            assert date_expected == date_actual,\
                f"Ожидалась дата '{date_expected}', получена '{date_actual}'"

        @allure.title("Выбор даты с помощью календаря")
        def test_select_date_using_calendar(self, driver: WebDriver) -> None:
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_picker_page.open_calendar()
            date_expected = date_picker_page.select_random_date()
            date_actual = date_picker_page.get_date_value()

            assert date_actual == date_expected,\
                f"Ожидалась дата '{date_expected}', получена '{date_actual}'"

        @allure.title("Выбор случайной даты и времени через ручной ввод")
        def test_select_random_date_and_time_manual_input(self, driver: WebDriver) -> None:
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_expected = date_picker_page.set_date_and_time()
            date_actual = date_picker_page.get_date_and_time_value()

            assert date_expected == date_actual,\
                f"Ожидалась дата '{date_expected}', получена '{date_actual}'"

        @allure.title("Выбор даты и времени с помощью календаря")
        def test_select_date_and_tim_using_calendar(self, driver: WebDriver) -> None:
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open_date_picker_page()
            date_picker_page.open_calendar_date_and_time()
            date_expected = date_picker_page.select_random_date_and_time()
            date_actual = date_picker_page.get_date_and_time_value()

            assert date_expected == date_actual,\
                f"Ожидалась дата '{date_expected}', получена '{date_actual}'"

    @allure.feature("Slider")
    class TestSlider:

        @allure.title("Проверяем перемещение ползунка")
        def test_slider_moves_when_dragged(self, driver: WebDriver) -> None:
            slider_page = SliderPage(driver)
            slider_page.open_slider_page()
            value_before, value_after = slider_page.change_slider_value()

            assert value_before != value_after, \
                f"Значение слайдера до и после перемещения совпадает: {value_before}"

    @allure.feature("Progress Bar")
    class TestProgressBar:

        @allure.title("Прогресс-бар запускается после нажатия Start")
        def test_progress_bar_is_running_after_start_click(self, driver: WebDriver) -> None:
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open_progress_bar_page()
            initial_value, finished_value = progress_bar_page.start_and_get_progress()

            assert initial_value < finished_value,\
                f"Прогресс-бар не увеличился: {initial_value} >= {finished_value}"

        @allure.title("Прогресс-бар останавливается после нажатия Stop")
        def test_progress_bar_stops_after_click_stop(self, driver: WebDriver) -> None:
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open_progress_bar_page()
            stop_value, value_after_wait = progress_bar_page.stop_progress_bar_and_get_values()

            assert stop_value == value_after_wait, "Прогресс-бар не остановился"

        @allure.title("Прогресс-бар сбрасывается в 0 после нажатия Reset")
        def test_progress_bar_resets_to_zero_after_reset_click(self, driver: WebDriver) -> None:
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open_progress_bar_page()
            value_before_reset, value_after_reset = (
                progress_bar_page.reset_progress_bar_and_get_values())

            assert value_before_reset != value_after_reset,\
                "Прогресс-бар не изменился после сброса"

            assert value_after_reset == '0',\
                "Прогресс-бар после сброса не равен 0"

    @allure.feature("Tabs")
    class TestTabs:

        @allure.title("Проверка отображения корректного контента при переключении вкладок")
        @pytest.mark.parametrize("tab, text, expected_text",
                                 TabsData.TABS_TEST_DATA,
                                 ids=["What", "Origin", "Use"])
        def test_tab_content_is_displayed_after_click(
                self,
                driver: WebDriver,
                tab: tuple[str, str],
                text: tuple[str, str],
                expected_text: str
        ) -> None:
            tabs_page = TabsPage(driver)
            tabs_page.open_tabs_page()
            tabs_page.click_tab(tab)
            text_actual = tabs_page.get_tab_text(text)

            assert text_actual == expected_text,\
                f"Текст вкладки '{tab}' неверный"

        @allure.title("Активная вкладка имеет aria-selected = true")
        @pytest.mark.parametrize(
            "tab, expected_value",
            TabsData.ACTIVE_TABS,
            ids=["WHAT", "ORIGIN", "USE"])
        def test_active_tab_has_aria_selected_true(
                self,
                driver: WebDriver,
                tab: tuple[str, str],
                expected_value: str
        ) -> None:
            tabs_page = TabsPage(driver)
            tabs_page.open_tabs_page()
            tabs_page.click_tab(tab)

            assert tabs_page.is_tab_active(tab), f"Вкладка '{tab}' не активна"

    @allure.feature("Tool Tip")
    class TestToolTips:

        @pytest.mark.parametrize(
            "hover_target, expected_text",
            ToolTipsData.TOOLTIPS_HOVER,
            ids=["button", "input", "contrary", "section"])
        @allure.title("Tooltip отображается при наведении на элемент")
        def test_tooltip_is_displayed_on_element_hover(
                self,
                driver: WebDriver,
                hover_target: tuple[str, str],
                expected_text: str
        ) -> None:
            tool_tips = ToolTipsPage(driver)
            tool_tips.open_tool_tips_page()
            tool_tips.hover(hover_target)
            text_tool_tip = tool_tips.get_tooltip_text()

            assert text_tool_tip == expected_text,\
                f"Текст tooltip неверный: ожидалось '{expected_text}', получено '{text_tool_tip}'"

    @allure.feature("Menu")
    class TestMenu:

        @allure.title("Проверка текста всех пунктов меню при наведении курсора")
        def test_menu_items(self, driver: WebDriver) -> None:
            menu_page = MenuPage(driver)

            with allure.step("Открываем страницу меню"):
                menu_page.open_menu_page()

            with allure.step("Собираем текст всех пунктов меню после наведения"):
                menu_items_text_actual = menu_page.get_menu_items_text_when_hovered()

            with allure.step("Проверяем, что текст пунктов соответствует ожидаемому"):
                assert menu_items_text_actual == MenuData.MENU_TEXT, \
                    "Текст пунктов меню неверный"

    @allure.feature("Select Menu")
    class TestSelectMenu:

        @allure.title("Выбор случайного значения в Select Value")
        def test_select_value(self, driver: WebDriver) -> None:
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open_select_menu_page()
            expected_text_value, actual_text_value = select_menu_page.set_select_value()

            assert expected_text_value == actual_text_value, \
                f"Select Value: ожидалось {expected_text_value}, получено {actual_text_value}"

        @allure.title("Выбор случайного значения в Select One")
        def test_select_one(self, driver: WebDriver) -> None:
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open_select_menu_page()
            expected_text_one, actual_text_one = select_menu_page.set_select_one()

            assert expected_text_one == actual_text_one, \
                f"Select One: ожидалось {expected_text_one}, получено {actual_text_one}"

        @allure.title("Выбор цвета в старом стиле Select Menu")
        def test_old_style_select_menu(self, driver: WebDriver) -> None:
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open_select_menu_page()
            expected_color, actual_color = select_menu_page.set_old_style_select_menu()

            assert expected_color == actual_color, \
                f"Old Style Select Menu: ожидалось {expected_color}, получено {actual_color}"

        @allure.title("Выбор нескольких цветов в MultiSelect Dropdown")
        def test_multiselect_drop_down(self, driver: WebDriver) -> None:
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open_select_menu_page()
            expected_colors, actual_colors = select_menu_page.set_multiselect_drop_down()

            assert expected_colors == actual_colors, \
                f"MultiSelect Dropdown: ожидалось {expected_colors}, получено {actual_colors}"

        @allure.title("Выбор нескольких машин в стандартном Multi Select")
        def test_standard_multi_select(self, driver: WebDriver) -> None:
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open_select_menu_page()
            expected_cars, actual_cars = select_menu_page.set_standard_multi_select()

            assert expected_cars == actual_cars, \
                f"Standard Multi Select: ожидалось {expected_cars}, получено {actual_cars}"
