import allure
import pytest

from data import AccordianData
from pages.widgets_page import AccordianPage

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
