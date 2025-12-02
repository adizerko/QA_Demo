from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    USER_NAME_INPUT = By.ID, "userName"
    USER_EMAIL_INPUT = By.ID, "userEmail"
    CURRENT_ADDRESS = By.ID, "currentAddress"
    PERMANENT_ADDRESS = By.ID, "permanentAddress"
    SUBMIT = By.ID, "submit"

    USER_NAME_RESULT = By.ID, "name"
    USER_EMAIL_RESULT = By.ID, "email"
    USER_CURRENT_ADDRESS_RESULT = By.XPATH, "//p[@id='currentAddress']"
    USER_PERMANENT_ADDRESS_RESULT = By.XPATH, "//p[@id='permanentAddress']"


class CheckBoxLocators:
    ROOT_TOGGLE = By.CSS_SELECTOR, "button[aria-label='Toggle']"
    CHECKBOX_HOME = By.CSS_SELECTOR, "span.rct-checkbox > svg"

    DESKTOP_TOGGLE = By.XPATH, "//span[text()='Desktop']/parent::label/parent::span/button"
    DESKTOP_CHECKBOX = By.XPATH, "//span[text()='Desktop']/parent::label/span[1]"
    NOTES_CHECKBOX = By.XPATH, "//span[text()='Notes']/parent::label/span[1]"
    COMMANDS_CHECKBOX = By.XPATH, "//span[text()='Commands']/parent::label/span[1]"

    DOCUMENTS_TOGGLE = By.XPATH, "//span[text()='Documents']/parent::label/parent::span/button"
    DOCUMENTS_CHECKBOX = By.XPATH, "//span[text()='Documents']/parent::label/span[1]"

    DOWNLOADS_TOGGLE = By.XPATH, "//span[text()='Downloads']/parent::label/parent::span/button"
    DOWNLOADS_CHECKBOX = By.XPATH, "//span[text()='Downloads']/parent::label/span[1]"
    WORD_FILE_CHECKBOX = By.XPATH, "//span[text()='Word File.doc']/parent::label/span[1]"
    EXCEL_FILE_CHECKBOX = By.XPATH, "//span[text()='Excel File.doc']/parent::label/span[1]"

    WORKSPACE_TOGGLE = By.XPATH, "//span[text()='WorkSpace']/parent::label/parent::span/button"
    WORKSPACE_CHECKBOX = By.XPATH, "//span[text()='WorkSpace']/parent::label/span[1]"
    REACT_CHECKBOX = By.XPATH, "//span[text()='React']/parent::label/span[1]"
    ANGULAR_CHECKBOX = By.XPATH, "//span[text()='Angular']/parent::label/span[1]"
    VEU_CHECKBOX = By.XPATH, "//span[text()='Veu']/parent::label/span[1]"

    OFFICE_TOGGLE = By.XPATH, "//span[text()='Office']/parent::label/parent::span/button"
    OFFICE_CHECKBOX = By.XPATH, "//span[text()='Office']/parent::label/span[1]"
    PUBLIC_CHECKBOX = By.XPATH, "//span[text()='Public']/parent::label/span[1]"
    PRIVATE_CHECKBOX = By.XPATH, "//span[text()='Private']/parent::label/span[1]"
    CLASSIFIED_CHECKBOX = By.XPATH, "//span[text()='Classified']/parent::label/span[1]"
    GENERAL_CHECKBOX = By.XPATH, "//span[text()='General']/parent::label/span[1]"

    CHECKED_ITEMS = By.XPATH, "//span[@class='rct-checkbox']//*[contains(@class, 'rct-icon-check')]/ancestor::label/span[@class='rct-title']"
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = By.CSS_SELECTOR, "span[class='text-success']"


class RadioButtonLocators:
    YES_RADIO = By.XPATH, "//label[@for='yesRadio']"
    IMPRESSIVE_RADIO = By.XPATH, "//label[@for='impressiveRadio']"
    NO_RADIO = By.XPATH, "//label[@for='noRadio']"
    SELECTED = By.CLASS_NAME, "text-success"


class WebTablesLocators:
    ADD_BUTTON = By.ID, "addNewRecordButton"
    SEARCH_INPUT = By.ID, "searchBox"
    PREVIOUS_BUTTON = By.XPATH, "//div[@class='-previous']/button"
    NEXT_BUTTON = By.XPATH, "//div[@class='-next']/button"
    PAGE_INPUT = By.XPATH, "//input[@aria-label='jump to page']"
    COLUMN_FIRST_NAME = By.XPATH, "//div[text()='First Name'"
    COLUMN_LAST_NAME = By.XPATH, "//div[text()='Last Name']"
    COLUMN_AGE = By.XPATH, "//div[text()='Age']"
    COLUMN_EMAIL = By.XPATH, "//div[text()='Email']"
    COLUMN_SALARY = By.XPATH, "//div[text()='Salary']"
    COLUMN_DEPARTMENT = By.XPATH, "//div[text()='Department']"
    COLUMN_ACTION = By.XPATH, "//div[text()='Action']"

    FIRST_NAME_INPUT = By.ID, "firstName"
    LAST_NAME_INPUT = By.ID, "lastName"
    EMAIL_INPUT = By.ID, "userEmail"
    AGE_INPUT = By.ID, "age"
    SALARY_INPUT = By.ID, "salary"
    DEPARTMENT_INPUT = By.ID, "department"
    SUBMIT_BUTTON = By.ID, "submit"
    DELETE_BUTTON = By.XPATH, "//span[@title='Delete']"
    EDIT_BUTTON = By.XPATH, "//span[@title='Edit']"
    EDIT_BUTTON_LAST_USER = By.XPATH, "(//span[@title='Edit'])[last()]"

    TABLE_ROWS_SELECTOR = By.XPATH, "//select[@aria-label='rows per page']"
    TABLE_ROWS_OPTION_5 = By.XPATH, "//option[@value='5']"
    TABLE_ROWS_OPTION_10 = By.XPATH, "//option[@value='10']"
    TABLE_ROWS_OPTION_20 = By.XPATH, "//option[@value='20']"
    TABLE_ROWS_OPTION_25 = By.XPATH, "//option[@value='25']"
    TABLE_ROWS_OPTION_50 = By.XPATH, "//option[@value='50']"
    TABLE_ROWS_OPTION_100 = By.XPATH, "//option[@value='100']"

    FIELDS = By.XPATH, "//div[@class='rt-tr-group']"
    FIRST_NAME_ADDED_CHECK = By.XPATH, "//*[text()='kierra@example.com']/parent::div"


class ButtonsPageLocators:
    DOUBLE_BUTTON = By.ID, "doubleClickBtn"
    RIGHT_BUTTON = By.ID, "rightClickBtn"
    CLICK_BUTTON = By.XPATH, "//div[3]/button"
    DOUBLE_CLICK_MESSAGE = By.ID, "doubleClickMessage"
    RIGHT_CLICK_MESSAGE = By.ID, "rightClickMessage"
    DYNAMIC_CLICK_MESSAGE = By.ID, "dynamicClickMessage"


class LinksPageLocators:
    HOME_LINK = By.ID, "simpleLink"
    DYNAMIC_LINK = By.ID, "dynamicLink"
    CREATED_LINK = By.ID, "created"
    NO_CONTENT_LINK = By.ID, "no-content"
    MOVED_LINK = By.ID, "moved"
    BAD_REQUEST_LINK = By.ID, "bad-request"
    UNAUTHORIZED_LINK = By.ID, "unauthorized"
    FORBIDDEN_LINK = By.ID, "forbidden"
    NOT_FOUND_LINK = By.ID, "invalid-url"

    RESPONSE_STATUS_CODE = By.XPATH, "//p[@id='linkResponse']/b[1]"
    RESPONSE_TEXT = By.XPATH, "//p[@id='linkResponse']/b[2]"


class UploadAndDownloadLocators:
    DOWNLOAD_BUTTON = By.ID, "downloadButton"
    UPLOAD_INPUT = By.ID, "uploadFile"
    UPLOAD_RESULT = By.ID, "uploadedFilePath"


class SortablePageLocators:
    LIST = By.ID, "demo-tab-list"
    TAB_LISTS = By.XPATH, "//div[@class='vertical-list-container mt-4']/div"
    ONE_LIST = By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='One']"
    TWO_LIST = By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='Two']"
    THREE_LIST = By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='Three']"
    FOUR_LIST = By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='Four']"
    FIVE_LIST = By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='Five']"
    SIX_LIST = By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='Six']"

    GRID = By.ID, "demo-tab-grid"
    TAB_GRIDS = By.XPATH, "//div[@class='create-grid']/div"
    ONE_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='One']"
    TWO_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Two']"
    THREE_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Three']"
    FOUR_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Four']"
    FIVE_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Five']"
    SIX_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Six']"
    SEVEN_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Seven']"
    EIGHT_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Eight']"
    NINE_GRID = By.XPATH, "//div[@class='create-grid']/div[text()='Nine']"


class SelectablePageLocators:
    LIST = By.ID, "demo-tab-list"
    ITEMS_LIST = By.XPATH, "//ul[@id='verticalListContainer']/li[contains(@class, 'list-group-item')]"
    SELECT_ITEMS_LIST = By.XPATH, "//ul[@id='verticalListContainer']/li[contains(@class, 'active')]"

    GRID = By.ID, "demo-tab-grid"
    GRID_LIST = By.XPATH, "//div[@id='gridContainer']//li[contains(@class, 'list-group-item')]"
    GRID_SELECT_LIST = By.XPATH, "//div[@id='gridContainer']//li[contains(@class, 'active')]"


class ResizablePageLocators:
    RESIZABLE_RESTRICTION_BOX = By.ID, "resizableBoxWithRestriction"
    RESIZABLE_RESTRICTION_BOX_HANDLE = By.XPATH, "//div[@id='resizableBoxWithRestriction']//span"

    RESIZABLE_BOX = By.ID, "resizable"
    RESIZABLE_BOX_HANDLE = By.XPATH, "//div[@id='resizable']//span"


class DroppablePageLocators:
    TAB_SIMPLE = By.ID, "droppableExample-tab-simple"
    DRAGGABLE = By.ID, "draggable"
    DROPPABLE = By.ID, "droppable"
    DROPPABLE_TEXT = By.XPATH, "//div[@id='simpleDropContainer']//p"

    TAB_ACCEPT = By.ID, "droppableExample-tab-accept"
    ACCEPTABLE = By.ID, "acceptable"
    NOT_ACCEPTABLE = By.ID, "notAcceptable"
    ACCEPT_DROPPABLE = By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']"

    TAB_PREVENT_PROPOGATION = By.ID, "droppableExample-tab-preventPropogation"
    DRAG_ME = By.ID, "dragBox"
    OUTER_DROPPABLE = By.ID, "notGreedyDropBox"
    OUTER_DROPPABLE_TEXT = By.XPATH, "//div[@id='notGreedyDropBox']/p"
    INNER_DROPPABLE = By.ID, "notGreedyInnerDropBox"
    INNER_DROPPABLE_TEXT = By.XPATH, "//div[@id='notGreedyInnerDropBox']/p"
    GREEDY_DROP_BOX = By.ID, "greedyDropBox"
    GREEDY_DROP_BOX_TEXT = By.XPATH, "//div[@id='greedyDropBox']/p"
    GREEDY_DROP_BOX_INNER = By.ID, "greedyDropBoxInner"
    GREEDY_DROP_BOX_INNER_TEXT = By.XPATH, "//div[@id='greedyDropBoxInner']/p"

    TAB_REVERT_DRAGGABLE = By.ID, "droppableExample-tab-revertable"
    REVERT_ABLE = By.ID, "revertable"
    NOT_REVERT_ABLE = By.ID, "notRevertable"
    DROPPABLE_REVERT = By.XPATH, "(//div[@id='droppable'])[3]"
    DROPPABLE_REVERT_TEXT = By.XPATH, "(//div[@id='droppable'])[3]/p"


class DraggablePageLocators:
    DRAG_ME = By.ID, "dragBox"

    AXIS_RESTRICTED_TAB = By.ID, "draggableExample-tab-axisRestriction"
    ONLY_X = By.ID, "restrictedX"
    ONLY_Y = By.ID, "restrictedY"

    CONTAINER_RESTRICTED_TAB = By.ID, "draggableExample-tab-containerRestriction"
    BIG_CONTAINER = By.ID, "containmentWrapper"
    CONTAINED_DRAGGABLE = By.XPATH, "//div[@id='containmentWrapper']/div"
    SMALL_CONTAINER = By.CLASS_NAME, "draggable ui-widget-content m-3"
    CONTAINED_DRAGGABLE_SPAN = By.XPATH, "//div[@class='draggable ui-widget-content m-3']/span"
