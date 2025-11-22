from selenium.webdriver.common.by import By

CHECKBOX_ELEMENTS = ["Desktop", "Notes", "Commands",
                     "Documents", "Downloads", "Word File.doc",
                     "Excel File.doc", "WorkSpace", "React",
                     "Angular", "Veu", "Office", "Public", "Private",
                     "Classified", "General",]

RADIO_BUTTON_ELEMENTS = ["yesRadio","impressiveRadio",]

DEPARTMENT = ["Insurance", "Compliance", "Legal"]

LOCATORS_SORT_BY_COLUMN = [
    ("//div[text()='First Name']", "Alden", 1),
    ("//div[text()='Last Name']", "Cantrell", 2),
    ("//div[text()='Age']", "29", 3),
    ("//div[text()='Email']", "alden@example.com", 4),
    ("//div[text()='Salary']", "2000", 5),
    ("//div[text()='Department']", "Compliance", 6),
]

SUCCESS_DOUBLE_CLICK_MESSAGE = "You have done a double click"
SUCCESS_RIGHT_CLICK_MESSAGE = "You have done a right click"
SUCCESS_CLICK_MESSAGE = "You have done a dynamic click"

LOCATORS_LINKS_PAGE = [
    (By.ID, "simpleLink"),
    (By.ID, "dynamicLink")
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