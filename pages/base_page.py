from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import requests


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver


    def open(self, url: str) -> None:
        self.driver.get(url)

    def wait_for_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
        )

    def wait_for_visible(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def click(self, locator, timeout: int = 10):
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    def send_keys(self, locator, keys: str, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    def get_text(self, locator, timeout: int = 10):
        text = self.wait_for_element(locator).text
        return text

    def find_elements(self, locator, timeout: int = 10):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def find_elements_for_web_tables(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements


    def action_double_click(self, locator):
        elements = self.wait_for_element(locator)
        action = ActionChains(self.driver)
        action.double_click(elements)
        action.perform()

    def action_right_click(self, locator):
        elements = self.wait_for_element(locator)
        action = ActionChains(self.driver)
        action.context_click(elements)
        action.perform()

    def get_attribute(self, locator, attribute, timeout: int = 10):
        element = self.wait_for_element(locator)
        attribute = element.get_attribute(attribute)
        return attribute

    def switch_to_new_windows(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def clear_input_js(self):
        self.driver.execute_script("document.getElementById('dateOfBirthInput').value = ''")

    def switch_to_alert(self):
        return self.driver.switch_to.alert
