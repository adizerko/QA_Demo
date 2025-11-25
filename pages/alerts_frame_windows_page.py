import allure
from selenium.webdriver.common.by import By

from curl import BROWSER_WINDOWS_URL, ALERT_URL
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

    def open_alerts_page(self):
        self.open(ALERT_URL)

    def click_alert_button(self):
        self.click(self.ALERT_BUTTON)

