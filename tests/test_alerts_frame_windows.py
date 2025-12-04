import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


from data import ModalDialogsData, FrameData, BrowserWindowsData
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, \
    FramePage, NestedFramesPage, ModalDialogsPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindows:

    @allure.feature('Browser Windows')
    class TestBrowserWindows:

        @allure.title("Проверка открытия новой вкладки")
        def test_click_new_tab_button(self, driver: WebDriver) -> None:
            browser_window_page = BrowserWindowsPage(driver)
            browser_window_page.open_browser_windows_page()
            browser_window_page.click_new_tab_button()
            current_url, text = browser_window_page.get_new_tab_url()

            assert current_url == BrowserWindowsData.SAMPLE_PAGE_URL, \
                "Открыта неверная вкладка"

            assert text == BrowserWindowsData.SAMPLE_PAGE_TITLE_TEXT, \
                "Текст на странице некорректный"

        @allure.title("Проверка открытия нового окна")
        def test_click_new_window_button(self, driver: WebDriver) -> None:
            browser_window_page = BrowserWindowsPage(driver)
            browser_window_page.open_browser_windows_page()
            browser_window_page.click_new_window_button()
            current_url, text = browser_window_page.get_new_tab_url()

            assert current_url == BrowserWindowsData.SAMPLE_PAGE_URL, \
                "Открыта неверная вкладка"

            assert text == BrowserWindowsData.SAMPLE_PAGE_TITLE_TEXT, \
                "Текст на странице некорректный"

    @allure.feature('Alerts Page')
    class TestAlerts:

        @allure.title("Клик на кнопку alert и проверка текста")
        def test_alerts_button(self, driver: WebDriver) -> None:
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_alert_button()
            text = alerts_page.accept_alert()

            assert text == BrowserWindowsData.YOU_CLICKED_A_BUTTON_TEXT, \
                "Неверный текст alert"

        @allure.title("Клик на кнопку таймерного alert и проверка текста")
        def test_timer_alert_button(self, driver: WebDriver) -> None:
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_timer_alert_button()
            text = alerts_page.accept_alert()

            assert text == BrowserWindowsData.ALERT_APPEARED_AFTER_5_SEC_TEXT, \
                "Неверный текст таймерного alert"

        @allure.title("Принятие confirm alert")
        def test_confirm_alert_button(self, driver: WebDriver) -> None:
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_confirm_button()
            text = alerts_page.accept_alert()
            result_confirm  = alerts_page.get_result_confirm_alert()

            assert text == BrowserWindowsData.CONFIRM_ALERT_TEXT, \
                "Неверный confirm-текст"

            assert result_confirm == BrowserWindowsData.CONFIRM_ALERT_OK_RESULT, \
                "Ответ после принятия неверный"

        @allure.title("Отклонение confirm alert")
        def test_dismiss_alert_button(self, driver: WebDriver) -> None:
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_confirm_button()
            text = alerts_page.dismiss_alert()
            result_confirm = alerts_page.get_result_confirm_alert()

            assert text == BrowserWindowsData.CONFIRM_ALERT_TEXT, \
                "Неверный confirm-текст"

            assert result_confirm == BrowserWindowsData.CONFIRM_ALERT_CANCEL_RESULT, \
                "Ответ после отмены неверный"

        @allure.title("Отправка текста в prompt alert")
        def test_prompt_button(self, driver: WebDriver) -> None:
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_prompt_button()
            text_prompt, text_alert_prompt = alerts_page.send_text_to_prompt()
            prompt_result = alerts_page.get_result_prompt_alert()

            assert text_alert_prompt == BrowserWindowsData.PROMPT_ALERT_MESSAGE,\
                "Неверный текст prompt"

            assert prompt_result == f"You entered {text_prompt}", \
                "Неверный результат prompt"

    @allure.feature('Frame Page')
    class TestFrame:

        @allure.title("Проверяем текст во фрейме")
        @pytest.mark.parametrize("frame", FrameData.FRAME_LOCATOR, ids=["Frame 1", "Frame 2"])
        def test_frame_page(self, driver: WebDriver, frame: tuple[str, str]) -> None:
            frame_page = FramePage(driver)
            frame_page.open_frame_page()
            text_frame = frame_page.switch_to_frame_and_get_text(frame)

            assert text_frame == BrowserWindowsData.SAMPLE_PAGE_TITLE_TEXT, \
                "Неверный текст во фрейме"

    @allure.feature('Nested Frame Page')
    class TestNestedFrame:
        @allure.title("Проверка текста в родительском фрейме")
        def test_parent_frame(self, driver: WebDriver) -> None:
            nested_frames_page = NestedFramesPage(driver)
            nested_frames_page.open_nested_frame_page()
            nested_frames_page.switch_to_parent_frame()
            parent_text = nested_frames_page.get_text_frame()

            assert parent_text == BrowserWindowsData.PARENT_FRAME_TEXT, \
                "Неверный текст родительского фрейма"

        @allure.title("Проверка текста в дочернем фрейме")
        def test_child_frame(self, driver: WebDriver) -> None:
            nested_frames_page = NestedFramesPage(driver)
            nested_frames_page.open_nested_frame_page()
            nested_frames_page.switch_to_parent_frame()
            nested_frames_page.switch_to_child_frame()
            child_text = nested_frames_page.get_text_frame()

            assert child_text == BrowserWindowsData.CHILD_FRAME_TEXT, \
                "Неверный текст дочернего фрейма"

    @allure.feature("Modal Dialogs Page")
    class TestModalDialogs:

        @allure.title("Проверка текста маленького модального окна")
        def test_small_modal(self, driver: WebDriver) -> None:
            modal_dialogs_page = ModalDialogsPage(driver)
            modal_dialogs_page.ope_modal_dialogs_page()
            modal_dialogs_page.click_small_modal_button()
            text_modal = modal_dialogs_page.get_text_small_modal()
            modal_dialogs_page.click_close_small_modal_button()

            assert text_modal == ModalDialogsData.SMALL_MODAL_EXPECTED_TEXT, \
                "Неверный текст small modal"

        @allure.title("Проверка текста большого модального окна")
        def test_large_modal(self, driver: WebDriver) -> None:
            modal_dialogs_page = ModalDialogsPage(driver)
            modal_dialogs_page.ope_modal_dialogs_page()
            modal_dialogs_page.click_large_modal_button()
            text_modal = modal_dialogs_page.get_text_large_modal()
            modal_dialogs_page.click_close_large_modal_button()

            assert text_modal == ModalDialogsData.LARGE_MODAL_EXPECTED_TEXT, \
                "Неверный текст large modal"
