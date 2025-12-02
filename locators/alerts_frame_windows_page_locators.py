from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = By.ID, "tabButton"
    NEW_WINDOW_BUTTON = By.ID, "windowButton"
    NEW_WINDOW_MESSAGE = By.ID, "messageWindowButton"
    SAMPLE_PAGE = By.ID, "sampleHeading"
    NEW_WINDOW_MESSAGE_TEXT  = By.XPATH, "//body"


class AlertsPageLocators:
    ALERT_BUTTON = By.ID, "alertButton"
    TIMER_ALERT_BUTTON = By.ID, "timerAlertButton"
    CONFIRM_BUTTON = By.ID, "confirmButton"
    PROMPT_BUTTON = By.ID, "promtButton"
    CONFIRM_RESULT = By.ID, "confirmResult"
    PROMPT_RESULT = By.ID, "promptResult"


class FramePageLocators:
    FRAME_1 = By.ID, "frame1"
    FRAME_2 = By.ID, "frame2"
    SAMPLE_HEADING = By.ID, "sampleHeading"


class NestedFramesPageLocators:
    PARENT_FRAME = By.ID, "frame1"
    CHILD_FRAME = By.XPATH, ".//iframe"
    PARENT_FRAME_TEXT = By.XPATH, "//body"
    CHILD_FRAME_TEXT = By.XPATH, "//body/p"


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = By.ID, "showSmallModal"
    LARGE_MODAL_BUTTON = By.ID, "showLargeModal"
    CLOSE_SMALL_MODAL_BUTTON = By.ID, "closeSmallModal"
    CLOSE_LARGE_MODAL_BUTTON = By.ID, "closeLargeModal"
    TEXT_SMALL_MODAL = By.CLASS_NAME, "modal-body"
    TEXT_LARGE_MODAL = By.XPATH, "//div[@class='modal-body']/p"
