import allure
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    @allure.step("Открываем страницу {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Ждём видимость элемента {locator}")
    def wait_for_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
        )

    @allure.step("Ждём появления alert")
    def wait_for_alert(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    @allure.step("Ждём, пока элемент {locator} станет кликабельным")
    def wait_for_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Кликаем на элемент {locator}")
    def click(self, locator, timeout: int = 10):
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    @allure.step("Вводим текст '{keys}' в элемент {locator}")
    def send_keys(self, locator, keys: str, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получаем текст элемента {locator}")
    def get_text(self, locator, timeout: int = 10):
        text = self.wait_for_element(locator).text
        return text

    @allure.step("Находим элементы по локатору {locator}")
    def find_elements(self, locator, timeout: int = 10):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    @allure.step("Находим элементы по локатору {locator} без ожидания")
    def get_elements(self, locator):
        by, value = locator
        elements = self.driver.find_elements(by, value)
        return elements

    def find_elements_for_web_tables(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    @allure.step("Выбираем текст '{text}' в элементе {locator}")
    def select_by_text(self, locator, text, timeout = 10):
        element = self.wait_for_clickable(locator)
        Select(element).select_by_visible_text(text)

    @allure.step("Выбираем значение '{text}' в элементе {locator}")
    def select_by_value(self, locator, text, timeout = 10):
        element = self.wait_for_clickable(locator)
        Select(element).select_by_value(text)

    @allure.step("Переключаемся на новое окно")
    def switch_to_new_windows(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получаем первый выбранный элемент в селекте {locator}")
    def select_get_first_option_text(self, locator, timeout: int = 10):
        element = self.wait_for_clickable(locator)
        return Select(element).first_selected_option.text

    @allure.step("Получаем текст всех выбранных элементов в селекте {locator}")
    def select_all_options_text(self, locator, timeout: int = 10):
        element = self.wait_for_clickable(locator)
        options_text = []

        for sel_el in Select(element).all_selected_options:
            options_text.append(sel_el.text)

        return options_text

    @allure.step("Двойной клик по элементу {locator}")
    def action_double_click(self, locator):
        elements = self.wait_for_element(locator)
        action = ActionChains(self.driver)
        action.double_click(elements)
        action.perform()

    @allure.step("Правый клик по элементу {locator}")
    def action_right_click(self, locator):
        elements = self.wait_for_element(locator)
        action = ActionChains(self.driver)
        action.context_click(elements)
        action.perform()

    @allure.step("Получаем атрибут '{attribute}' элемента {locator}")
    def get_attribute(self, locator, attribute, timeout: int = 10):
        element = self.wait_for_element(locator, timeout)
        attribute = element.get_attribute(attribute)
        return attribute

    @allure.step("Получаем атрибут '{value}' элемента {locator}")
    def get_attribute_via_presence(self, locator, value, timeout: int =10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element.get_attribute(value)

    @allure.step("Перетаскиваем элемент {element} на смещение ({x_coords}, {y_coords})")
    def switch_to_new_windows(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        url = self.driver.current_url
        return url

    @allure.step("Очищаем поле ввода через JS по ID '{element_id}'")
    def clear_input_js(self, element_id):
        self.driver.execute_script(f"document.getElementById('{element_id}').value = ''")

    @allure.step("Переключаемся на alert")
    def switch_to_alert(self):
        alert = self.wait_for_alert()
        return alert

    @allure.step("Переключаемся на iframe {locator}")
    def switch_to_frame(self, locator, timeout = 10):
        frame = WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )
        return frame

    @allure.step("Перетаскиваем элемент {element} на смещение ({x_coords}, {y_coords})")
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step("Наводим курсор на элемент {locator}")
    def action_move_to_element(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator)
        action.perform()

    @allure.step("Перетаскиваем элемент {source} на элемент {target}")
    def drag_and_drop(self, first_locator, second_locator, timeout: int = 10):
        source = self.wait_for_clickable(first_locator)
        target = self.wait_for_clickable(second_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target)
        action.perform()

    @allure.step("Получаем позицию элемента {locator}")
    def get_element_position(self, locator, timeout: int = 10):
        element = self.wait_for_element(locator, timeout)
        position = element.location
        return position
