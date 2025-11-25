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

LOCATOR_GENDERS = [
    (By.ID, "gender-radio-1"),
    (By.ID, "gender-radio-2"),
    (By.ID, "gender-radio-3"),
]

SUBJECTS_LIST = [
    "Hindi", "English", "Maths", "Physics", "Chemistry",
    "Biology", "Computer Science", "Commerce", "Accounting",
    "Economics", "Arts", "Social Studies", "History", "Civics",
]

STATE_AND_CITY = {
    "NCR": ["Delhi", "Gurgaon", "Noida"],
    "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
    "Haryana": ["Karnal", "Panipat"],
    "Rajasthan": ["Jaipur", "Jaiselmer"]
}

FRAME_LOCATOR = [
    (By.ID, "frame1"),
    (By.ID, "frame2")
]

class ModalDialogsData:
    SMALL_MODAL_EXPECTED_TEXT = "This is a small modal. It has very less content"

    LARGE_MODAL_EXPECTED_TEXT = (
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
    "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
    "It has survived not only five centuries, but also the leap into electronic typesetting, "
    "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets "
    "containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker "
    "including versions of Lorem Ipsum."
)

