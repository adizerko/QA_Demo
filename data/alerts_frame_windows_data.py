from locators.alerts_frame_windows_page_locators import FramePageLocators


class BrowserWindowsData:
    SAMPLE_PAGE_URL = "https://demoqa.com/sample"
    SAMPLE_PAGE_TITLE_TEXT = "This is a sample page"
    YOU_CLICKED_A_BUTTON_TEXT = "You clicked a button"
    ALERT_APPEARED_AFTER_5_SEC_TEXT = "This alert appeared after 5 seconds"
    CONFIRM_ALERT_TEXT = "Do you confirm action?"
    CONFIRM_ALERT_OK_RESULT = "You selected Ok"
    CONFIRM_ALERT_CANCEL_RESULT = "You selected Cancel"
    PROMPT_ALERT_MESSAGE = "Please enter your name"
    PARENT_FRAME_TEXT = "Parent frame"
    CHILD_FRAME_TEXT = "Child Iframe"


class FrameData:
    FRAME_LOCATOR = [
        FramePageLocators.FRAME_1,
        FramePageLocators.FRAME_2
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