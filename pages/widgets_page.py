import random

import allure
from selenium.webdriver.common.by import By

from curl import ACCORDIAN_URL, AUTO_COMPLETE_URL
from data import AccordianData, AutoCompleteData
from generation import Generation
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
