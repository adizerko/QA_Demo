import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage

@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindows:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:

        @allure.title("Проверка открытия новой вкладки")
        def test_click_new_tab_button(self, driver):
            browser_window_page = BrowserWindowsPage(driver)
            browser_window_page.open_browser_windows_page()
            browser_window_page.click_new_tab_button()
            current_url, text = browser_window_page.get_new_tab_url()

            assert current_url == "https://demoqa.com/sample"
            assert text == "This is a sample page"

        @allure.title("Проверка открытия нового окна")
        def test_click_new_window_button(self, driver):
            browser_window_page = BrowserWindowsPage(driver)
            browser_window_page.open_browser_windows_page()
            browser_window_page.click_new_window_button()
            current_url, text = browser_window_page.get_new_tab_url()

            assert current_url == "https://demoqa.com/sample"
            assert text == "This is a sample page"


    @allure.feature('Alerts Page')
    class TestAlerts:
        @allure.title("Клик на кнопку alert и проверка текста")
        def test_alerts_button(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_alert_button()
            text = alerts_page.accept_alert()

            assert text == "You clicked a button"

        @allure.title("Клик на кнопку таймерного alert и проверка текста")
        def test_timer_alert_button(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_timer_alert_button()
            text = alerts_page.accept_alert()

            assert text == "This alert appeared after 5 seconds"

        @allure.title("Принятие confirm alert")
        def test_confirm_alert_button(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_confirm_button()
            text = alerts_page.accept_alert()
            result_confirm  = alerts_page.get_result_confirm_alert()

            assert text == "Do you confirm action?"
            assert result_confirm == "You selected Ok"

        @allure.title("Отклонение confirm alert")
        def test_dismiss_alert_button(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_confirm_button()
            text = alerts_page.dismiss_alert()
            result_confirm = alerts_page.get_result_confirm_alert()

            assert text == "Do you confirm action?"
            assert result_confirm == "You selected Cancel"

        @allure.title("Отправка текста в prompt alert")
        def test_prompt_button(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_prompt_button()
            text_prompt, text_alert_prompt = alerts_page.send_text_to_prompt()
            prompt_result = alerts_page.get_result_prompt_alert()

            assert text_alert_prompt == "Please enter your name"
            assert prompt_result == f"You entered {text_prompt}"
