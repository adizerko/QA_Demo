import allure


from curl import BROWSER_WINDOWS_URL, ALERT_URL, FRAME_URL, NESTED_FRAME_URL, MODAL_DIALOGS_URL
from generation import Generation
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramePageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators

    @allure.step("Открыть страницу Browser Windows")
    def open_browser_windows_page(self) -> None:
        self.open(BROWSER_WINDOWS_URL)

    @allure.step("Кликнуть на кнопку New Tab")
    def click_new_tab_button(self) -> None:
        self.click(self.locators.NEW_TAB_BUTTON)

    @allure.step("Кликнуть на кнопку New Window")
    def click_new_window_button(self) -> None:
        self.click(self.locators.NEW_WINDOW_BUTTON)

    @allure.step("Кликнуть на кнопку New Window Message")
    def click_new_window_message_button(self) -> None:
        self.click(self.locators.NEW_WINDOW_MESSAGE)

    @allure.step("Получить URL с новой вкладки")
    def get_new_tab_url(self) -> tuple[str, str]:
        self.switch_to_new_windows()
        current_url = self.get_current_url()
        text_new_tab = self.get_text(self.locators.SAMPLE_PAGE)
        return current_url, text_new_tab


class AlertsPage(BasePage):
    locators = AlertsPageLocators

    @allure.step("Открываем страницу с alert")
    def open_alerts_page(self) -> None:
        self.open(ALERT_URL)

    @allure.step("Кликаем кнопку простого alert")
    def click_alert_button(self) -> None:
        self.click(self.locators.ALERT_BUTTON)

    @allure.step("Кликаем кнопку таймерного alert")
    def click_timer_alert_button(self) -> None:
        self.click(self.locators.TIMER_ALERT_BUTTON)

    @allure.step("Кликаем кнопку confirm alert")
    def click_confirm_button(self) -> None:
        self.click(self.locators.CONFIRM_BUTTON)

    @allure.step("Кликаем кнопку prompt alert")
    def click_prompt_button(self) -> None:
        self.click(self.locators.PROMPT_BUTTON)

    @allure.step("Принимаем alert и возвращаем его текст")
    def accept_alert(self) -> str:
        alert = self.switch_to_alert()
        text = alert.text
        alert.accept()
        return text

    @allure.step("Отклоняем alert и возвращаем его текст")
    def dismiss_alert(self) -> str:
        alert = self.switch_to_alert()
        text = alert.text
        alert.dismiss()
        return text

    @allure.step("Получаем результат confirm alert на странице")
    def get_result_confirm_alert(self) -> str:
        result_confirm = self.get_text(self.locators.CONFIRM_RESULT)
        return result_confirm

    @allure.step("Отправляем текст в prompt alert и возвращаем введённый текст и текст alert")
    def send_text_to_prompt(self) -> tuple[str, str]:
        alert = self.switch_to_alert()
        text_prompt = Generation.first_name()
        alert.send_keys(text_prompt)
        text_alert_prompt = alert.text
        alert.accept()
        return text_prompt, text_alert_prompt

    @allure.step("Получаем результат prompt alert на странице")
    def get_result_prompt_alert(self) -> str:
        result_prompt = self.get_text(self.locators.PROMPT_RESULT)
        return result_prompt


class FramePage(BasePage):
    locators = FramePageLocators

    @allure.step("Открываем страницу Frames")
    def open_frame_page(self) -> None:
        self.open(FRAME_URL)

    @allure.step("Переключаемся на фрейм и получаем текст внутри фрейма: {locator}")
    def switch_to_frame_and_get_text(self, locator: tuple[str, str]) -> str:
        self.switch_to_frame(locator)
        text_frame = self.get_text(self.locators.SAMPLE_HEADING)
        return text_frame


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators

    @allure.step("Открываем страницу Nested Frames")
    def open_nested_frame_page(self) -> None:
        self.open(NESTED_FRAME_URL)

    @allure.step("Переключаемся на родительский фрейм")
    def switch_to_parent_frame(self) -> None:
        self.switch_to_frame(self.locators.PARENT_FRAME)

    @allure.step("Переключаемся на дочерний фрейм")
    def switch_to_child_frame(self) -> None:
        self.switch_to_frame(self.locators.CHILD_FRAME)

    @allure.step("Получаем текст из текущего фрейма")
    def get_text_frame(self) -> str:
        parent_text = self.get_text(self.locators.PARENT_FRAME_TEXT)
        return parent_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators

    @allure.step("Открываем страницу Modal Dialogs")
    def ope_modal_dialogs_page(self) -> None:
        self.open(MODAL_DIALOGS_URL)

    @allure.step("Нажимаем кнопку маленького модального окна")
    def click_small_modal_button(self) -> None:
        self.click(self.locators.SMALL_MODAL_BUTTON)

    @allure.step("Закрываем маленькое модальное окно")
    def click_close_small_modal_button(self) -> None:
        self.click(self.locators.CLOSE_SMALL_MODAL_BUTTON)

    @allure.step("Получаем текст маленького модального окна")
    def get_text_small_modal(self) -> str:
        text_small_modal = self.get_text(self.locators.TEXT_SMALL_MODAL)
        return text_small_modal

    @allure.step("Нажимаем кнопку большого модального окна")
    def click_large_modal_button(self) -> None:
        self.click(self.locators.LARGE_MODAL_BUTTON)

    @allure.step("Получаем текст большого модального окна")
    def get_text_large_modal(self) -> str:
        text_large_modal = self.get_text(self.locators.TEXT_LARGE_MODAL)
        return text_large_modal

    @allure.step("Закрываем большое модальное окно")
    def click_close_large_modal_button(self) -> None:
        self.click(self.locators.CLOSE_LARGE_MODAL_BUTTON)
