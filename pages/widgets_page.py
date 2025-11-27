import random


import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from curl import ACCORDIAN_URL, AUTO_COMPLETE_URL, DATE_PICKER_URL, SLIDER_URL
from data import AutoCompleteData
from generation import Generation
from helper import Helper
from pages.base_page import BasePage


class AccordianPage(BasePage):
    SECTION_FIRST = By.ID, "section1Heading"
    SECTION_FIRST_TEXT = By.XPATH, "//div[@id='section1Content']//p"
    SECTION_FIRST_ATTRIBUTE = By.XPATH, "//div[@id='section1Heading']//following-sibling::div"
    SECTION_SECOND = By.ID, "section2Heading"
    SECTION_SECOND_TEXT = By.XPATH, "//div[@id='section2Content']/p"
    SECTION_SECOND_ATTRIBUTE = By.XPATH, "//div[@id='section2Heading']//following-sibling::div"
    SECTION_THIRD = By.ID, "section3Heading"
    SECTION_THIRD_TEXT = By.XPATH, "//div[@id='section3Content']//p"
    SECTION_THIRD_ATTRIBUTE = By.XPATH, "//div[@id='section3Heading']//following-sibling::div"

    def open_accordian_page(self):
        self.open(ACCORDIAN_URL)

    @allure.step("Кликаем по секции: {locator}")
    def click_section(self, locator):
        self.click(locator)

    def click_first_section(self):
        self.click_section(self.SECTION_FIRST)

    def click_second_section(self):
        self.click_section(self.SECTION_SECOND)

    def click_third_section(self):
        self.click_section(self.SECTION_THIRD)

    @allure.step("Получаем текст секции 1")
    def get_text_first_section(self):
        return self.get_text(self.SECTION_FIRST_TEXT)

    @allure.step("Получаем текст секции 2")
    def get_text_second_section(self):
        return self.get_text(self.SECTION_SECOND_TEXT)

    @allure.step("Получаем текст секции 3")
    def get_text_third_section(self):
        return self.get_text(self.SECTION_THIRD_TEXT)

    @allure.step("Получаем css-класс раскрытия секции 1")
    def get_attribute_section_first(self):
        attribute = self.get_attribute(self.SECTION_FIRST_ATTRIBUTE, "class")
        return attribute

    @allure.step("Получаем заголовок секции по локатору")
    def get_text_title_section(self, locator):
        title_text = self.get_text(locator)
        return title_text


class AutoCompletePage(BasePage):
    INPUT_MULTIPLE = By.ID, "autoCompleteMultipleInput"
    DELETE_TAG_BUTTONS = By.XPATH, "//div[contains(@class, 'auto-complete__multi-value__remove')]"
    CLEAR_ALL_BUTTON = By.XPATH, "//div[contains(@class, 'auto-complete__clear-indicator')]"
    TAG_LIST_MULTIPLE = By.XPATH, "//div[contains(@class, 'css-12jo7m5')]"
    SUGGESTION_ITEMS = By.XPATH, "//div[contains(@class, 'auto-complete__option')]"

    INPUT_SINGLE = By.ID, "autoCompleteSingleInput"
    TAG_SINGLE = By.XPATH, "//div[contains(@class, 'auto-complete__single-value')]"
    SUGGESTION_ITEMS_SINGLE = By.XPATH, "//div[contains(@class, 'auto-complete__option')]"

    @allure.step("Открыть страницу AutoComplete")
    def open_auto_complete_page(self):
        self.open(AUTO_COMPLETE_URL)

    @allure.step("Кликнуть по multiple input")
    def click_on_multiple_input(self):
        self.click(self.INPUT_MULTIPLE)

    @allure.step("Кликнуть по single input")
    def click_on_single_input(self):
        self.click(self.INPUT_SINGLE)

    @allure.step("Получить подсказки для случайной буквы")
    def get_suggestions_for_random_letter(self, input_field):
        letter = random.choice(list(AutoCompleteData.AUTO_COMPLETE_OPTIONS.keys()))
        expected_suggestions = AutoCompleteData.AUTO_COMPLETE_OPTIONS[letter]
        self.send_keys(input_field, letter)
        elements = self.find_elements(self.SUGGESTION_ITEMS)
        actual_suggestions = [el.text for el in elements]

        return expected_suggestions, actual_suggestions

    @allure.step("Добавить {quantity} случайных тегов в multiple поле")
    def set_random_color_in_multiple_field(self, quantity):
        used_colors = set()
        for _ in range(quantity):
            color = Generation.color()

            while color in used_colors:
                color = Generation.color()

            used_colors.add(color)

            self.send_keys(self.INPUT_MULTIPLE, color)
            self.click(self.SUGGESTION_ITEMS)

    @allure.step("Удалить один тег")
    def delete_tag(self):
        self.click(self.DELETE_TAG_BUTTONS)

    @allure.step("Удалить все теги одной кнопкой")
    def delete_all_tags(self):
        self.click(self.CLEAR_ALL_BUTTON)

    @allure.step("Проверить, что список тегов пуст")
    def is_tag_list_empty(self):
        result = self.get_elements(self.TAG_LIST_MULTIPLE)
        return result

class DatePickerPage(BasePage):
    DATE_INPUT = By.ID, "datePickerMonthYearInput"
    DATE_SELECT_MONTH = By.XPATH, "//select[@class='react-datepicker__month-select']"
    DATE_SELECT_YEAR = By.XPATH, "//select[@class='react-datepicker__year-select']"
    DATE_SELECT_DAY_LIST = By.XPATH, "//div[contains(@class,'react-datepicker__day') and(contains(@class, 'react-datepicker__day--'))and not(contains(@class,'outside-month'))]"

    DATE_AND_TIME_INPUT = By.ID, "dateAndTimePickerInput"
    DATE_AND_TIME_MONTH = By.CLASS_NAME, "react-datepicker__month-read-view--down-arrow"
    DATE_AND_TIME_MONTH_LIST = By.XPATH, "//div[contains(@class, 'react-datepicker__month-option')]"
    DATE_AND_TIME_DAY_LIST = By.XPATH, "//div[contains(@class,'react-datepicker__day') and(contains(@class, 'react-datepicker__day--'))and not(contains(@class,'outside-month'))]"
    DATE_AND_TIME_YEAR = By.CLASS_NAME, "react-datepicker__year-read-view--selected-year"
    DATE_AND_TIME_YEAR_LIST = By.XPATH, "(//div[contains(@class,'react-datepicker__year-option')])[position() > 1 and position() < last()]"
    DATE_AND_TIME_TIME = By.CLASS_NAME, "react-datepicker__time-list-item"

    @allure.step("Открываем страницу DatePicker")
    def open_date_picker_page(self):
        self.open(DATE_PICKER_URL)

    @allure.step("Устанавливаем дату через инпут")
    def set_date(self):
        date = Generation.date()
        self.send_keys(self.DATE_INPUT, Keys.CONTROL + "a")
        self.clear_input_js("datePickerMonthYearInput")
        self.send_keys(self.DATE_INPUT, date)
        self.send_keys(self.DATE_INPUT, Keys.ENTER)
        return date

    @allure.step("Получаем значение даты из инпута")
    def get_date_value(self):
        date = self.get_attribute(self.DATE_INPUT, "value")
        return date

    @allure.step("Открываем календарь")
    def open_calendar(self):
        self.click(self.DATE_INPUT)

    @allure.step("Выбираем случайный месяц")
    def set_random_month(self):
        random_month = random.randint(0,11)
        self.select_by_value(self.DATE_SELECT_MONTH, str(random_month))
        random_month += 1
        month_str = f"{random_month:02d}"
        return month_str

    @allure.step("Выбираем случайный год")
    def set_random_year(self):
        random_year = str(random.randint(1900, 2100))
        self.select_by_text(self.DATE_SELECT_YEAR, random_year)
        return random_year

    @allure.step("Выбираем случайный день")
    def set_random_day(self):
        days = self.get_elements(self.DATE_SELECT_DAY_LIST)
        day_element = random.choice(days)
        day_number = day_element.text
        self.click(day_element)
        day_str = f"{int(day_number):02d}"
        return day_str

    @allure.step("Выбираем случайную дату")
    def select_random_date(self):
        month = self.set_random_month()
        year = self.set_random_year()
        day = self.set_random_day()
        return f"{month}/{day}/{year}"

    @allure.step("Устанавливаем дату и время через инпут")
    def set_date_and_time(self):
        date_and_time = Generation.date_and_time()
        self.send_keys(self.DATE_AND_TIME_INPUT, Keys.CONTROL + "a")
        self.clear_input_js("dateAndTimePickerInput")
        self.send_keys(self.DATE_AND_TIME_INPUT, date_and_time)
        self.send_keys(self.DATE_AND_TIME_INPUT, Keys.ENTER)
        return date_and_time

    @allure.step("Получаем значение даты и времени из инпута")
    def get_date_and_time_value(self):
        date_and_time = self.get_attribute(self.DATE_AND_TIME_INPUT, "value")
        return date_and_time

    @allure.step("Открываем календарь для выбора даты и времени")
    def open_calendar_date_and_time(self):
        self.click(self.DATE_AND_TIME_INPUT)

    @allure.step("Выбираем случайный месяц (Date & Time)")
    def select_random_mont(self):
        self.click(self.DATE_AND_TIME_MONTH)
        month_element = random.choice(self.get_elements(self.DATE_AND_TIME_MONTH_LIST))
        month_text = month_element.text
        self.click(month_element)
        return month_text

    @allure.step("Выбираем случайный год (Date & Time)")
    def select_random_year(self):
        self.click(self.DATE_AND_TIME_YEAR)
        year_element = random.choice(self.get_elements(self.DATE_AND_TIME_YEAR_LIST))
        year_text = year_element.text
        self.click(year_element)
        return year_text

    @allure.step("Выбираем случайный день (Date & Time)")
    def select_random_day(self):
        day_element = random.choice(self.get_elements(self.DATE_AND_TIME_DAY_LIST))
        day_text = day_element.text
        self.click(day_element)
        return day_text

    @allure.step("Выбираем случайное время")
    def select_random_time(self):
        time_element = random.choice(self.get_elements(self.DATE_AND_TIME_TIME))
        time_text = time_element.text
        self.click(time_element)
        return time_text

    @allure.step("Выбираем случайную дату и время")
    def select_random_date_and_time(self):
        month = self.select_random_mont()
        year = self.select_random_year()
        day = self.select_random_day()
        time = Helper.formated_time(self.select_random_time())  # допустим, возвращает "23:30"
        date_and_time = f"{month} {day}, {year} {time}"
        return date_and_time


class SliderPage(BasePage):
    INPUT_SLIDER = By.XPATH, "//input[@class='range-slider range-slider--primary']"
    INPUT_SLIDER_VALUE = By.ID, "sliderValue"

    @allure.step("Открываем страницу Slider")
    def open_slider_page(self):
        self.open(SLIDER_URL)

    @allure.step("Двигаем ползунок")
    def change_slider_value(self):
        value_before = self.get_attribute(self.INPUT_SLIDER_VALUE, "value")
        element = self.wait_for_element(self.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(element, random.randint(1,100), 0)
        value_after = self.get_attribute(self.INPUT_SLIDER_VALUE, "value")
        return value_before, value_after
