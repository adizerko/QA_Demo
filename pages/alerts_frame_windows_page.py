import allure
from selenium.webdriver.common.by import By

from curl import BROWSER_WINDOWS_URL, ALERT_URL, FRAME_URL
from generation import Generation
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    NEW_TAB_BUTTON = By.ID, "tabButton"
    NEW_WINDOW_BUTTON = By.ID, "windowButton"
    NEW_WINDOW_MESSAGE = By.ID, "messageWindowButton"
    SAMPLE_PAGE = By.ID, "sampleHeading"
    NEW_WINDOW_MESSAGE_TEXT  = By.XPATH, "//body"


    @allure.step("Открыть страницу Browser Windows")
    def open_browser_windows_page(self):
        self.open(BROWSER_WINDOWS_URL)

    @allure.step("Кликнуть на кнопку New Tab")
    def click_new_tab_button(self):
        self.click(self.NEW_TAB_BUTTON)

    @allure.step("Кликнуть на кнопку New Window")
    def click_new_window_button(self):
        self.click(self.NEW_WINDOW_BUTTON)

    @allure.step("Кликнуть на кнопку New Window Message")
    def click_new_window_message_button(self):
        self.click(self.NEW_WINDOW_MESSAGE)

    @allure.step("Получить URL с новой вкладки")
    def get_new_tab_url(self):
        self.switch_to_new_windows()
        current_url = self.get_current_url()
        text_new_tab = self.get_text(self.SAMPLE_PAGE)
        return current_url, text_new_tab


class AlertsPage(BasePage):
    ALERT_BUTTON = By.ID, "alertButton"
    TIMER_ALERT_BUTTON = By.ID, "timerAlertButton"
    CONFIRM_BUTTON = By.ID, "confirmButton"
    PROMPT_BUTTON = By.ID, "promtButton"
    CONFIRM_RESULT = By.ID, "confirmResult"
    PROMPT_RESULT = By.ID, "promptResult"

    @allure.step("Открываем страницу с alert")
    def open_alerts_page(self):
        self.open(ALERT_URL)

    @allure.step("Кликаем кнопку простого alert")
    def click_alert_button(self):
        self.click(self.ALERT_BUTTON)

    @allure.step("Кликаем кнопку таймерного alert")
    def click_timer_alert_button(self):
        self.click(self.TIMER_ALERT_BUTTON)

    @allure.step("Кликаем кнопку confirm alert")
    def click_confirm_button(self):
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Кликаем кнопку prompt alert")
    def click_prompt_button(self):
        self.click(self.PROMPT_BUTTON)

    @allure.step("Принимаем alert и возвращаем его текст")
    def accept_alert(self):
        alert = self.switch_to_alert()
        text = alert.text
        alert.accept()
        return text

    @allure.step("Отклоняем alert и возвращаем его текст")
    def dismiss_alert(self):
        alert = self.switch_to_alert()
        text = alert.text
        alert.dismiss()
        return text

    @allure.step("Получаем результат confirm alert на странице")
    def get_result_confirm_alert(self):
        result_confirm = self.get_text(self.CONFIRM_RESULT)
        return result_confirm

    @allure.step("Отправляем текст в prompt alert и возвращаем введённый текст и текст alert")
    def send_text_to_prompt(self):
        alert = self.switch_to_alert()
        text_prompt = Generation.first_name()
        alert.send_keys(text_prompt)
        text_alert_prompt = alert.text
        alert.accept()
        return text_prompt, text_alert_prompt

    @allure.step("Получаем результат prompt alert на странице")
    def get_result_prompt_alert(self):
        result_prompt = self.get_text(self.PROMPT_RESULT)
        return result_prompt


class FramePage(BasePage):
    FRAME_1 = By.ID, "frame1"
    FRAME_2 = By.ID, "frame2"
    SAMPLE_HEADING = By.ID, "sampleHeading"

    @allure.step("Открываем страницу Frames")
    def open_frame_page(self):
        self.open(FRAME_URL)

    @allure.step("Переключаемся на фрейм и получаем текст внутри фрейма: {locator}")
    def switch_to_frame_and_get_text(self, locator):
        self.switch_to_frame(locator)
        text_frame = self.get_text(self.SAMPLE_HEADING)
        return text_frame
