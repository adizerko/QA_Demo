import allure
from selenium.webdriver.common.by import By

from curl import ACCORDIAN_URL
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
