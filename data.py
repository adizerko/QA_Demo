from attr import dataclass
from selenium.webdriver.common.by import By

from locators.widgets_page_locators import TabsPageLocators, ToolTipsPageLocators

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

class AccordianData:
    SECTION_TITLES = [
        ((By.ID, "section1Heading"), "What is Lorem Ipsum?"),
        ((By.ID, "section2Heading"), "Where does it come from?"),
        ((By.ID, "section3Heading"), "Why do we use it?")
    ]

    SECTION = [
        ((By.XPATH, "//div[@id='section1Heading']//following-sibling::div"), (By.ID, "section1Heading")),
        ((By.XPATH, "//div[@id='section2Heading']//following-sibling::div"), (By.ID, "section2Heading")),
        ((By.XPATH, "//div[@id='section3Heading']//following-sibling::div"), (By.ID, "section3Heading"))
    ]


    FIRST_SECTION_TEXT_EXPECTED = (
         "Lorem Ipsum is simply dummy text of the printing"
         " and typesetting industry. Lorem Ipsum has been the"
         " industry's standard dummy text ever since the 1500s,"
         " when an unknown printer took a galley of type and"
         " scrambled it to make a type specimen book."
         " It has survived not only five centuries,"
         " but also the leap into electronic typesetting,"
         " remaining essentially unchanged."
         " It was popularised in the 1960s with the release of"
         " Letraset sheets containing Lorem Ipsum passages,"
         " and more recently with desktop publishing software"
         " like Aldus PageMaker including versions of Lorem Ipsum."
                                   )

    SECOND_SECTION_TEXT_EXPECTED = (
        'Contrary to popular belief, Lorem Ipsum is not simply random text.'
         ' It has roots in a piece of classical Latin literature from 45 BC,'
         ' making it over 2000 years old. Richard McClintock,'
         ' a Latin professor at Hampden-Sydney College in Virginia,'
         ' looked up one of the more obscure Latin words, consectetur,'
         ' from a Lorem Ipsum passage, and going through the cites of'
         ' the word in classical literature, discovered the undoubtable source.'
         ' Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of'
         ' "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil)'
         ' by Cicero, written in 45 BC. This book is a treatise on the theory'
         ' of ethics, very popular during the Renaissance.'
         ' The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..",'
         ' comes from a line in section 1.10.32.'
    )
    THIRD_SECTION_TEXT_EXPECTED = (
            "It is a long established fact that a reader will"
            " be distracted by the readable content of a page"
            " when looking at its layout. The point of using"
            " Lorem Ipsum is that it has a more-or-less normal"
            " distribution of letters, as opposed to using"
            " 'Content here, content here', making it look like"
            " readable English. Many desktop publishing packages"
            " and web page editors now use Lorem Ipsum as their"
            " default model text, and a search for 'lorem ipsum'"
            " will uncover many web sites still in their infancy."
            " Various versions have evolved over the years,"
            " sometimes by accident, sometimes on purpose"
            " (injected humour and the like)."
    )

class AutoCompleteData:

    COLORS = ["Red",
              "Blue",
              "Green",
              "Yellow",
              "Black",
              "White",
              "Voilet",
              "Indigo",
              "Magenta",
              "Aqua",]

    AUTO_COMPLETE_OPTIONS = {
        "a": ["Black", "Magenta", "Aqua"],
        "b": ["Blue", "Black"],
        "c": ["Black"],
        "d": ["Red", "Indigo"],
        "i": ["White", "Voilet", "Indigo"],
        "e": ["Red", "Blue", "Green", "Yellow", "Purple", "White", "Voilet", "Magenta"],
        "g": ["Green", "Indigo", "Magenta"],
        "h": ["White"],
        "l": ["Blue", "Yellow", "Purple", "Black", "Voilet"],
        "bl": ["Blue", "Black"],
        "en": ["Green", "Magenta"],
    }

    INPUT_FIELDS = [
        (By.ID, "autoCompleteMultipleInput"),
        (By.ID, "autoCompleteSingleInput")
    ]

class DatePickerData:
    pass


class TabsData:
    locator = TabsPageLocators()

    WHAT_TEXT = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    ORIGIN_TEXT = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
    USE_TEXT = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

    TABS_TEST_DATA = [
        (locator.WHAT_TAB, locator.WHAT_TAB_TEXT, WHAT_TEXT),
        (locator.ORIGIN_TAB, locator.ORIGIN_TAB_TEXT, ORIGIN_TEXT),
        (locator.USE_TAB, locator.USE_TAB_TEXT, USE_TEXT),
    ]

    ACTIVE_TABS = [
        (locator.WHAT_TAB, "true"),
        (locator.ORIGIN_TAB, "true"),
        (locator.USE_TAB, "true")
    ]


class ToolTipsData:
    locator = ToolTipsPageLocators()
    TOOLTIPS_HOVER = [
        (locator.BUTTON, "You hovered over the Button"),
        (locator.INPUT, "You hovered over the text field"),
        (locator.CONTRARY_LINK, "You hovered over the Contrary"),
        (locator.SECTION_LINK, "You hovered over the 1.10.32")
    ]
