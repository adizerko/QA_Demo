import time

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

    class TestAlerts:
        def test_alerts_button(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open_alerts_page()
            alerts_page.click_alert_button()
            time.sleep(2)