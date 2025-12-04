import random
import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from curl import ACCORDIAN_URL, AUTO_COMPLETE_URL, DATE_PICKER_URL, SLIDER_URL, \
    PROGRESS_BAR_URL, TABS_URL, TOOL_TIPS_URL, MENU_URL, SELECT_MENU_URL
from data import AutoCompleteData
from generation import Generation
from helper import Helper
from locators.widgets_page_locators import TabsPageLocators, ToolTipsPageLocators, \
    MenuPageLocators, SelectMenuLocators, AccordianPageLocators, AutoCompletePageLocators, \
    DatePickerPageLocators, SliderPageLocators, ProgressBarPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators

    def open_accordian_page(self) -> None:
        self.open(ACCORDIAN_URL)

    @allure.step("Кликаем по секции: {locator}")
    def click_section(self, locator) -> None:
        self.click(locator)

    @allure.step("Кликаем по первой секции")
    def click_first_section(self) -> None:
        self.click_section(self.locators.SECTION_FIRST)

    @allure.step("Кликаем по второй секции")
    def click_second_section(self) -> None:
        self.click_section(self.locators.SECTION_SECOND)

    @allure.step("Кликаем по третьей секции")
    def click_third_section(self) -> None:
        self.click_section(self.locators.SECTION_THIRD)

    @allure.step("Получаем текст секции 1")
    def get_text_first_section(self) -> str:
        return self.get_text(self.locators.SECTION_FIRST_TEXT)

    @allure.step("Получаем текст секции 2")
    def get_text_second_section(self) -> str:
        return self.get_text(self.locators.SECTION_SECOND_TEXT)

    @allure.step("Получаем текст секции 3")
    def get_text_third_section(self) -> str:
        return self.get_text(self.locators.SECTION_THIRD_TEXT)

    @allure.step("Получаем css-класс раскрытия секции 1")
    def get_attribute_section_first(self) -> str | None:
        return self.get_attribute(
            self.locators.SECTION_FIRST_ATTRIBUTE, "class")

    @allure.step("Получаем заголовок секции по локатору")
    def get_text_title_section(self, locator: tuple[str, str]) -> str:
        return self.get_text(locator)


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators

    @allure.step("Открыть страницу AutoComplete")
    def open_auto_complete_page(self) -> None:
        self.open(AUTO_COMPLETE_URL)

    @allure.step("Кликнуть по multiple input")
    def click_on_multiple_input(self) -> None:
        self.click(self.locators.INPUT_MULTIPLE)

    @allure.step("Кликнуть по single input")
    def click_on_single_input(self) -> None:
        self.click(self.locators.INPUT_SINGLE)

    @allure.step("Получить подсказки для случайной буквы")
    def get_suggestions_for_random_letter(
            self,
            input_field: tuple[str, str]
    ) -> tuple[list[str], list[str]]:
        letter: str = random.choice(list(AutoCompleteData.AUTO_COMPLETE_OPTIONS.keys()))
        expected_suggestions: list[str] = AutoCompleteData.AUTO_COMPLETE_OPTIONS[letter]

        self.send_keys(input_field, letter)

        elements = self.find_elements(self.locators.SUGGESTION_ITEMS)
        actual_suggestions = [el.text for el in elements]
        return expected_suggestions, actual_suggestions

    @allure.step("Добавить {quantity} случайных тегов в multiple поле")
    def set_random_color_in_multiple_field(self, quantity: int) -> None:
        used_colors = set()

        for _ in range(quantity):
            color = Generation.color()

            while color in used_colors:
                color = Generation.color()

            used_colors.add(color)

            self.send_keys(self.locators.INPUT_MULTIPLE, color)
            self.click(self.locators.SUGGESTION_ITEMS)

    @allure.step("Удалить один тег")
    def delete_tag(self) -> None:
        self.click(self.locators.DELETE_TAG_BUTTONS)

    @allure.step("Удалить все теги одной кнопкой")
    def delete_all_tags(self) -> None:
        self.click(self.locators.CLEAR_ALL_BUTTON)

    @allure.step("Проверить, что список тегов пуст")
    def is_tag_list_empty(self) -> list[WebElement]:
        result = self.get_elements(self.locators.TAG_LIST_MULTIPLE)
        return result


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators

    @allure.step("Открываем страницу DatePicker")
    def open_date_picker_page(self) -> None:
        self.open(DATE_PICKER_URL)

    @allure.step("Устанавливаем дату через инпут")
    def set_date(self) -> str:
        date: str = Generation.date()
        self.send_keys(self.locators.DATE_INPUT, Keys.CONTROL + "a")
        self.clear_input_js("datePickerMonthYearInput")
        self.send_keys(self.locators.DATE_INPUT, date)
        self.send_keys(self.locators.DATE_INPUT, Keys.ENTER)
        return date

    @allure.step("Получаем значение даты из инпута")
    def get_date_value(self) -> str | None:
        date = self.get_attribute(self.locators.DATE_INPUT, "value")
        return date

    @allure.step("Открываем календарь")
    def open_calendar(self) -> None:
        self.click(self.locators.DATE_INPUT)

    @allure.step("Выбираем случайный месяц")
    def set_random_month(self) -> str:
        random_month = random.randint(0,11)
        self.select_by_value(self.locators.DATE_SELECT_MONTH, str(random_month))
        random_month += 1
        month_str = f"{random_month:02d}"
        return month_str

    @allure.step("Выбираем случайный год")
    def set_random_year(self) -> str:
        random_year = str(random.randint(1900, 2100))
        self.select_by_text(self.locators.DATE_SELECT_YEAR, random_year)
        return random_year

    @allure.step("Выбираем случайный день")
    def set_random_day(self) -> str:
        days: list[WebElement] = self.get_elements(self.locators.DATE_SELECT_DAY_LIST)
        day_element: WebElement = random.choice(days)
        day_number = day_element.text
        day_element.click()
        day_str = f"{int(day_number):02d}"
        return day_str

    @allure.step("Выбираем случайную дату")
    def select_random_date(self) -> str:
        month = self.set_random_month()
        year = self.set_random_year()
        day = self.set_random_day()
        return f"{month}/{day}/{year}"

    @allure.step("Устанавливаем дату и время через инпут")
    def set_date_and_time(self) -> str:
        date_and_time = Generation.date_and_time()
        self.send_keys(self.locators.DATE_AND_TIME_INPUT, Keys.CONTROL + "a")
        self.clear_input_js("dateAndTimePickerInput")
        self.send_keys(self.locators.DATE_AND_TIME_INPUT, date_and_time)
        self.send_keys(self.locators.DATE_AND_TIME_INPUT, Keys.ENTER)
        return date_and_time

    @allure.step("Получаем значение даты и времени из инпута")
    def get_date_and_time_value(self) -> str | None:
        date_and_time = self.get_attribute(self.locators.DATE_AND_TIME_INPUT, "value")
        return date_and_time

    @allure.step("Открываем календарь для выбора даты и времени")
    def open_calendar_date_and_time(self) -> None:
        self.click(self.locators.DATE_AND_TIME_INPUT)

    @allure.step("Выбираем случайный месяц (Date & Time)")
    def select_random_mont(self) -> str:
        self.click(self.locators.DATE_AND_TIME_MONTH)
        month_element: WebElement = random.choice(
            self.get_elements(self.locators.DATE_AND_TIME_MONTH_LIST))
        month_text = month_element.text
        month_element.click()
        return month_text

    @allure.step("Выбираем случайный год (Date & Time)")
    def select_random_year(self) -> str:
        self.click(self.locators.DATE_AND_TIME_YEAR)
        year_element: WebElement = random.choice(self.get_elements(self.locators.DATE_AND_TIME_YEAR_LIST))
        year_text = year_element.text
        year_element.click()
        return year_text

    @allure.step("Выбираем случайный день (Date & Time)")
    def select_random_day(self) -> str:
        day_element: WebElement = random.choice(
            self.get_elements(self.locators.DATE_AND_TIME_DAY_LIST))
        day_text = day_element.text
        day_element.click()
        return day_text

    @allure.step("Выбираем случайное время")
    def select_random_time(self) -> str:
        time_element: WebElement = random.choice(
            self.get_elements(self.locators.DATE_AND_TIME_TIME))
        time_text = time_element.text
        time_element.click()
        return time_text

    @allure.step("Выбираем случайную дату и время")
    def select_random_date_and_time(self) -> str:
        month = self.select_random_mont()
        year = self.select_random_year()
        day = self.select_random_day()
        time = Helper.formated_time(self.select_random_time())
        date_and_time = f"{month} {day}, {year} {time}"
        return date_and_time


class SliderPage(BasePage):
    locators = SliderPageLocators

    @allure.step("Открываем страницу Slider")
    def open_slider_page(self) -> None:
        self.open(SLIDER_URL)

    @allure.step("Двигаем ползунок")
    def change_slider_value(self) -> tuple[str | None, str | None]:
        value_before = self.get_attribute(self.locators.INPUT_SLIDER_VALUE, "value")
        element = self.wait_for_element(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(element, random.randint(1,100), 0)
        value_after = self.get_attribute(self.locators.INPUT_SLIDER_VALUE, "value")
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators

    @allure.step("Открываем страницу Progress Bar")
    def open_progress_bar_page(self) -> None:
        self.open(PROGRESS_BAR_URL)

    @allure.step("Нажимаем кнопку Start/Stop")
    def click_start_stop(self) -> None:
        self.click(self.locators.START_BUTTON)

    @allure.step("Нажимаем кнопку Reset")
    def click_reset(self) -> None:
        self.click(self.locators.RESET_BUTTON)

    @allure.step("Получаем значение прогресс-бара")
    def get_value_progress_bar(self) -> str | None:
        value = self.get_attribute_via_presence(
            self.locators.PROGRESS_BAR_VALUE, "aria-valuenow")
        return value

    @allure.step("Старт прогресс-бара и получение значения")
    def start_and_get_progress(self) -> tuple[str | None, str | None]:
        initial_value = self.get_value_progress_bar()
        self.click_start_stop()
        time.sleep(random.randint(1, 5))
        finished_value = self.get_value_progress_bar()
        return initial_value, finished_value

    @allure.step("Сброс прогресс-бара и получение значений до и после")
    def reset_progress_bar_and_get_values(self) -> tuple[str | None, str | None]:
        self.click_start_stop()
        time.sleep(10.5)
        value_before_reset = self.get_value_progress_bar()
        self.click_reset()
        value_after_reset = self.get_value_progress_bar()
        return value_before_reset, value_after_reset

    @allure.step("Остановка прогресс-бара и получение значения")
    def stop_progress_bar_and_get_values(self) -> tuple[str | None, str | None]:
        self.click_start_stop()
        time.sleep(2)
        self.click_start_stop()
        stop_value = self.get_value_progress_bar()
        time.sleep(2)
        value_after_wait = self.get_value_progress_bar()
        return stop_value, value_after_wait


class TabsPage(BasePage):
    locator = TabsPageLocators()

    @allure.step("Открываем страницу Tabs")
    def open_tabs_page(self) -> None:
        self.open(TABS_URL)

    @allure.step("Кликаем по вкладке")
    def click_tab(self, tab_locator: tuple[str, str]) -> None:
        self.click(tab_locator)

    @allure.step("Получаем текст контента активной вкладки")
    def get_tab_text(self, locator_text: tuple[str, str]) -> str:
        text = self.get_text(locator_text)
        return text

    @allure.step("Проверяем, что вкладка активна (aria-selected='true')")
    def is_tab_active(self, locator: tuple[str, str]) -> bool:
        value = self.get_attribute(locator, "aria-selected")
        return value == "true"


class ToolTipsPage(BasePage):
    locator = ToolTipsPageLocators()

    @allure.step("Открываем страницу Tool Tips")
    def open_tool_tips_page(self) -> None:
        self.open(TOOL_TIPS_URL)

    @allure.step("Наводим курсор на элемент: {locator}")
    def hover(self, locator: tuple[str, str]) -> None:
        element = self.wait_for_element(locator)
        self.action_move_to_element(element)

    @allure.step("Получаем текст Tooltip")
    def get_tooltip_text(self) -> str:
        text_tool_tip = self.get_text(self.locator.TOOL_TIP)
        return text_tool_tip


class MenuPage(BasePage):
    locators = MenuPageLocators

    @allure.step("Открываем страницу Menu")
    def open_menu_page(self) -> None:
        self.open(MENU_URL)

    @allure.step("Наводим курсор на каждый пункт меню и получаем их текст")
    def get_menu_items_text_when_hovered(self) -> list[str]:
        menu_items: list[WebElement] = self.get_elements(self.locators.MENU_ITEM_LIST)
        hovered_menu_texts = []

        for item in menu_items:
            with allure.step(f"Наводим на пункт меню: '{item.text}'"):
                self.action_move_to_element(item)
                hovered_menu_texts.append(item.text)
        return hovered_menu_texts


class SelectMenuPage(BasePage):
    locators = SelectMenuLocators

    @allure.step("Открыть страницу Select Menu")
    def open_select_menu_page(self) -> None:
        self.open(SELECT_MENU_URL)

    @allure.step("Выбрать случайное значение в Select Value")
    def set_select_value(self) -> tuple[str, str]:
        self.click(self.locators.SELECT_VALUE_INPUT)
        elem, expected_text = self.random_choice_option(
            self.locators.SELECT_VALUE_OPTION_LIST)
        elem.click()
        actual_text = self.get_text(self.locators.SELECT_VALUE_TEXT)
        return expected_text, actual_text

    @allure.step("Выбрать случайное значение в Select One")
    def set_select_one(self) -> tuple[str, str]:
        self.click(self.locators.SELECT_ONE_INPUT)
        elem, expected_text = self.random_choice_option(
            self.locators.SELECT_ONE_OPTION_LIST)
        elem.click()
        actual_text = self.get_text(self.locators.SELECT_ONE_TEXT)
        return expected_text, actual_text

    @allure.step("Выбрать цвет в Old Style Select Menu")
    def set_old_style_select_menu(self) -> tuple[str, str]:
        color_option = Generation.color_for_old_menu()
        self.click(self.locators.OLD_STYLE_SELECT_MENU)
        self.select_by_text(self.locators.OLD_STYLE_SELECT_MENU, color_option)

        actual_color_options = self.select_get_first_option_text(
            self.locators.OLD_STYLE_SELECT_MENU)
        return color_option, actual_color_options

    @allure.step("Выбрать несколько случайных цветов в MultiSelect Dropdown")
    def set_multiselect_drop_down(self) -> tuple[list[str], list[str]]:
        expected_colors = Generation.colors_for_multiselect_drop_down()
        self.click(self.locators.MULTISELECT_DROP_DOWN)

        for color in expected_colors:
            locator = By.XPATH, f"//div[text()='{color}']"
            self.click(locator)

        elements_choices_colors = self.get_elements(self.locators.MULTISELECT_DROP_DOWN_CHOICES_COLORS)
        actual_colors = [el.text for el in elements_choices_colors]
        return expected_colors, actual_colors

    @allure.step("Выбрать несколько машин в стандартном Multi Select")
    def set_standard_multi_select(self) -> tuple[list[str], list[str]]:
        cars = Generation.cars_for_standard_select_menu()

        for car in cars:
            self.select_by_text(self.locators.STANDARD_MULTI_SELECT, car)

        cars_selected = self.select_all_options_text(self.locators.STANDARD_MULTI_SELECT)
        return cars, cars_selected

    def random_choice_option(self, locator) -> tuple[WebElement, str]:
        elements = self.get_elements(locator)
        elem = random.choice(elements)
        return elem, elem.text
