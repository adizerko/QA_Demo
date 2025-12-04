import os

from locators.elements_page_locators import LinksPageLocators


class CheckBoxData:
    CHECKBOX_ELEMENTS = [
        "Desktop",
        "Notes",
        "Commands",
        "Documents",
        "Downloads",
        "Word File.doc",
        "Excel File.doc",
        "WorkSpace",
        "React",
        "Angular",
        "Veu",
        "Office",
        "Public",
        "Private",
        "Classified",
        "General",
    ]


class RadioButtonData:
    RADIO_YES = "Yes"
    RADIO_IMPRESSIVE = "Impressive"
    RADIO_NO = "No"


class WebTablesData:
    DEPARTMENT = ["Insurance", "Compliance", "Legal"]
    SEARCH_TEST_DATA = ["Alden", "Cantrell", "45", "alden@example.com", "1200", "Compliance",]
    TABLE_ROWS_OPTIONS = [5, 10, 20, 25, 50, 100]

    LOCATORS_SORT_BY_COLUMN = [
        ("//div[text()='First Name']", "Alden", 1),
        ("//div[text()='Last Name']", "Cantrell", 2),
        ("//div[text()='Age']", "29", 3),
        ("//div[text()='Email']", "alden@example.com", 4),
        ("//div[text()='Salary']", "2000", 5),
        ("//div[text()='Department']", "Compliance", 6),
    ]


class ButtonsData:
    SUCCESS_DOUBLE_CLICK_MESSAGE = "You have done a double click"
    SUCCESS_RIGHT_CLICK_MESSAGE = "You have done a right click"
    SUCCESS_CLICK_MESSAGE = "You have done a dynamic click"


class LinksData:
    LOCATORS_LINKS_PAGE = [
        LinksPageLocators.HOME_LINK,
        LinksPageLocators.DYNAMIC_LINK
    ]

    LOCATORS_LINKS_API_PAGE = [
        ("created", "201", "Created"),
        ("no-content", "204", "No Content"),
        ("moved", "301", "Moved Permanently"),
        ("bad-request", "400", "Bad Request"),
        ("unauthorized", "401", "Unauthorized"),
        ("forbidden", "403", "Forbidden"),
        ("invalid-url", "404", "Not Found")
    ]


class UploadAndDownloadData:
    DOWNLOADS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "downloads"))