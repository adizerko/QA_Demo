import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from data.elements_data import UploadAndDownloadData
from pages.elements_page import WebTables


@pytest.fixture
def driver() -> WebDriver:
    os.makedirs(UploadAndDownloadData.DOWNLOADS_DIR, exist_ok=True)
    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": os.path.abspath(UploadAndDownloadData.DOWNLOADS_DIR),
        "download.prompt_for_download": False,
        "directory_upgrade": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def add_new_user_web_tables_form(driver: WebDriver):
    web_tables_page = WebTables(driver)
    web_tables_page.open_web_tables_page()
    web_tables_page.add_button_click()
    new_user = web_tables_page.fill_user_form_and_get_data("yes")
    web_tables_page.click_submit()

    yield web_tables_page, new_user[3]
    web_tables_page.delete_last_user()
