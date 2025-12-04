from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    # ------------------ Кнопки ------------------
    NEW_TAB_BUTTON = By.ID, "tabButton"
    NEW_WINDOW_BUTTON = By.ID, "windowButton"
    NEW_WINDOW_MESSAGE = By.ID, "messageWindowButton"

    # ------------------ Контент новой вкладки/окна ------------------
    SAMPLE_PAGE = By.ID, "sampleHeading"
    NEW_WINDOW_MESSAGE_TEXT = By.XPATH, "//body"


class AlertsPageLocators:
    # ------------------ Кнопки alert ------------------
    ALERT_BUTTON = By.ID, "alertButton"
    TIMER_ALERT_BUTTON = By.ID, "timerAlertButton"
    CONFIRM_BUTTON = By.ID, "confirmButton"
    PROMPT_BUTTON = By.ID, "promtButton"

    # ------------------ Результаты alert ------------------
    CONFIRM_RESULT = By.ID, "confirmResult"
    PROMPT_RESULT = By.ID, "promptResult"


class FramePageLocators:
    # ------------------ Фреймы ------------------
    FRAME_1 = By.ID, "frame1"
    FRAME_2 = By.ID, "frame2"

    # ------------------ Контент внутри фреймов ------------------
    SAMPLE_HEADING = By.ID, "sampleHeading"


class NestedFramesPageLocators:
    # ------------------ Фреймы ------------------
    PARENT_FRAME = By.ID, "frame1"
    CHILD_FRAME = By.XPATH, ".//iframe"

    # ------------------ Тексты внутри фреймов ------------------
    PARENT_FRAME_TEXT = By.XPATH, "//body"
    CHILD_FRAME_TEXT = By.XPATH, "//body/p"


class ModalDialogsPageLocators:
    # ------------------ Кнопки модальных окон ------------------
    SMALL_MODAL_BUTTON = By.ID, "showSmallModal"
    LARGE_MODAL_BUTTON = By.ID, "showLargeModal"
    CLOSE_SMALL_MODAL_BUTTON = By.ID, "closeSmallModal"
    CLOSE_LARGE_MODAL_BUTTON = By.ID, "closeLargeModal"

    # ------------------ Тексты модальных окон ------------------
    TEXT_SMALL_MODAL = By.CLASS_NAME, "modal-body"
    TEXT_LARGE_MODAL = By.XPATH, "//div[@class='modal-body']/p"
