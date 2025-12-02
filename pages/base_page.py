from typing import Tuple

import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    @allure.step("Открываем страницу {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Ждём видимость элемента {locator}")
    def wait_for_element(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Ждём появления alert")
    def wait_for_alert(self, timeout: int =10) -> Alert:
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    @allure.step("Ждём, пока элемент {locator} станет кликабельным")
    def wait_for_clickable(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Кликаем на элемент {locator}")
    def click(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    @allure.step("Вводим текст '{keys}' в элемент {locator}")
    def send_keys(self, locator: Tuple[str, str], keys: str, timeout: int = 10) -> None:
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получаем текст элемента {locator}")
    def get_text(self, locator: Tuple[str, str], timeout: int = 10) -> str:
        return self.wait_for_element(locator, timeout).text

    @allure.step("Находим элементы по локатору {locator}")
    def find_elements(self, locator: Tuple[str, str], timeout: int = 10) -> list[WebElement]:
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    @allure.step("Находим элементы по локатору {locator} без ожидания")
    def get_elements(self, locator: Tuple[str, str]) -> list[WebElement]:
        by, value = locator
        elements = self.driver.find_elements(by, value)
        return elements

    def find_elements_for_web_tables(self, locator: Tuple[str, str]) -> list[WebElement]:
        elements = self.driver.find_elements(*locator)
        return elements

    @allure.step("Выбираем текст '{text}' в элементе {locator}")
    def select_by_text(self, locator: Tuple[str, str], text: str, timeout: int = 10) -> None:
        element = self.wait_for_clickable(locator, timeout)
        Select(element).select_by_visible_text(text)

    @allure.step("Выбираем значение '{text}' в элементе {locator}")
    def select_by_value(self, locator: Tuple[str, str], text: str, timeout: int = 10) -> None:
        element = self.wait_for_clickable(locator, timeout)
        Select(element).select_by_value(text)

    @allure.step("Переключаемся на новое окно")
    def switch_to_new_windows(self) -> None:
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получаем первый выбранный элемент в селекте {locator}")
    def select_get_first_option_text(self, locator: Tuple[str, str], timeout: int = 10) -> str:
        element = self.wait_for_clickable(locator, timeout)
        return Select(element).first_selected_option.text

    @allure.step("Получаем текст всех выбранных элементов в селекте {locator}")
    def select_all_options_text(self, locator: Tuple[str, str], timeout: int = 10) -> list[str]:
        element = self.wait_for_clickable(locator, timeout)
        select = Select(element)
        options_text = [opt.text for opt in select.all_selected_options]
        return options_text

    @allure.step("Двойной клик по элементу {locator}")
    def action_double_click(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        elements = self.wait_for_element(locator, timeout)
        action = ActionChains(self.driver)
        action.double_click(elements)
        action.perform()

    @allure.step("Правый клик по элементу {locator}")
    def action_right_click(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        elements = self.wait_for_element(locator, timeout)
        action = ActionChains(self.driver)
        action.context_click(elements)
        action.perform()

    @allure.step("Получаем атрибут '{attribute}' элемента {locator}")
    def get_attribute(self, locator: Tuple[str, str], attribute: str, timeout: int = 10) -> str | None:
        element = self.wait_for_element(locator, timeout)
        attr_value = element.get_attribute(attribute)
        return attr_value

    @allure.step("Получаем атрибут '{value}' элемента {locator}")
    def get_attribute_via_presence(self, locator: Tuple[str, str], value: str, timeout: int = 10) -> str | None:
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        attr_value = element.get_attribute(value)
        return attr_value

    @allure.step("Получаем текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Очищаем поле ввода через JS по ID '{element_id}'")
    def clear_input_js(self, element_id: str) -> None:
        self.driver.execute_script(f"document.getElementById('{element_id}').value = ''")

    @allure.step("Переключаемся на alert")
    def switch_to_alert(self) -> Alert:
        alert = self.wait_for_alert()
        return alert

    @allure.step("Переключаемся на iframe {locator}")
    def switch_to_frame(self, locator: Tuple[str, str], timeout: int = 10) -> bool:
        frame = WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )
        return frame

    @allure.step("Перетаскиваем элемент {element} на смещение ({x_coords}, {y_coords})")
    def action_drag_and_drop_by_offset(self, element: WebElement, x_coords: int, y_coords: int) -> None:
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords).perform()

    @allure.step("Наводим курсор на элемент {locator}")
    def action_move_to_element(self, element: WebElement) -> None:
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @allure.step("Перетаскиваем элемент {source} на элемент {target}")
    def drag_and_drop(self, first_locator: Tuple[str, str], second_locator: Tuple[str, str], timeout: int = 10) -> None:
        source = self.wait_for_clickable(first_locator, timeout)
        target = self.wait_for_clickable(second_locator, timeout)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    @allure.step("Получаем позицию элемента {locator}")
    def get_element_position(self, locator: Tuple[str, str], timeout: int = 10) -> dict[str, int]:
        element = self.wait_for_element(locator, timeout)
        return element.location
