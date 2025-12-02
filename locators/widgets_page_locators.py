from selenium.webdriver.common.by import By

class AccordianPageLocators:
    SECTION_FIRST = By.ID, "section1Heading"
    SECTION_FIRST_TEXT = By.XPATH, "//div[@id='section1Content']//p"
    SECTION_FIRST_ATTRIBUTE = By.XPATH, "//div[@id='section1Heading']//following-sibling::div"
    SECTION_SECOND = By.ID, "section2Heading"
    SECTION_SECOND_TEXT = By.XPATH, "//div[@id='section2Content']/p"
    SECTION_SECOND_ATTRIBUTE = By.XPATH, "//div[@id='section2Heading']//following-sibling::div"
    SECTION_THIRD = By.ID, "section3Heading"
    SECTION_THIRD_TEXT = By.XPATH, "//div[@id='section3Content']//p"
    SECTION_THIRD_ATTRIBUTE = By.XPATH, "//div[@id='section3Heading']//following-sibling::div"


class AutoCompletePageLocators:
    INPUT_MULTIPLE = By.ID, "autoCompleteMultipleInput"
    DELETE_TAG_BUTTONS = By.XPATH, "//div[contains(@class, 'auto-complete__multi-value__remove')]"
    CLEAR_ALL_BUTTON = By.XPATH, "//div[contains(@class, 'auto-complete__clear-indicator')]"
    TAG_LIST_MULTIPLE = By.XPATH, "//div[contains(@class, 'css-12jo7m5')]"
    SUGGESTION_ITEMS = By.XPATH, "//div[contains(@class, 'auto-complete__option')]"

    INPUT_SINGLE = By.ID, "autoCompleteSingleInput"
    TAG_SINGLE = By.XPATH, "//div[contains(@class, 'auto-complete__single-value')]"
    SUGGESTION_ITEMS_SINGLE = By.XPATH, "//div[contains(@class, 'auto-complete__option')]"


class DatePickerPageLocators:
    DATE_INPUT = By.ID, "datePickerMonthYearInput"
    DATE_SELECT_MONTH = By.XPATH, "//select[@class='react-datepicker__month-select']"
    DATE_SELECT_YEAR = By.XPATH, "//select[@class='react-datepicker__year-select']"
    DATE_SELECT_DAY_LIST = By.XPATH, "//div[contains(@class,'react-datepicker__day') and(contains(@class, 'react-datepicker__day--'))and not(contains(@class,'outside-month'))]"

    DATE_AND_TIME_INPUT = By.ID, "dateAndTimePickerInput"
    DATE_AND_TIME_MONTH = By.CLASS_NAME, "react-datepicker__month-read-view--down-arrow"
    DATE_AND_TIME_MONTH_LIST = By.XPATH, "//div[contains(@class, 'react-datepicker__month-option')]"
    DATE_AND_TIME_DAY_LIST = By.XPATH, "//div[contains(@class,'react-datepicker__day') and(contains(@class, 'react-datepicker__day--'))and not(contains(@class,'outside-month'))]"
    DATE_AND_TIME_YEAR = By.CLASS_NAME, "react-datepicker__year-read-view--selected-year"
    DATE_AND_TIME_YEAR_LIST = By.XPATH, "(//div[contains(@class,'react-datepicker__year-option')])[position() > 1 and position() < last()]"
    DATE_AND_TIME_TIME = By.CLASS_NAME, "react-datepicker__time-list-item"


class SliderPageLocators:
    INPUT_SLIDER = By.XPATH, "//input[@class='range-slider range-slider--primary']"
    INPUT_SLIDER_VALUE = By.ID, "sliderValue"


class ProgressBarPageLocators:
    START_BUTTON = By.ID, "startStopButton"
    RESET_BUTTON = By.ID, "resetButton"
    PROGRESS_BAR = By.ID, "progressBar"
    PROGRESS_BAR_VALUE = By.XPATH, "//div[@class='progress-bar bg-info' or @class='progress-bar bg-success']"


class TabsPageLocators:
    WHAT_TAB = By.ID, "demo-tab-what"
    WHAT_TAB_TEXT = By.XPATH, "//div[@id='demo-tabpane-what']/p"
    ORIGIN_TAB = By.ID, "demo-tab-origin"
    ORIGIN_TAB_TEXT = By.XPATH, "//div[@id='demo-tabpane-origin']/p"
    USE_TAB = By.ID, "demo-tab-use"
    USE_TAB_TEXT = By.XPATH, "//div[@id='demo-tabpane-use']/p"
    MORE_TAB = By.ID, "demo-tab-more"
    MORE_TAB_TEXT = By.XPATH, "//div[@id='demo-tabpane-more']/p"

class ToolTipsPageLocators:
    BUTTON = By.ID, "toolTipButton"
    INPUT = By.ID, "toolTipTextField"
    CONTRARY_LINK = By.XPATH, "//div[@id='texToolTopContainer']/a[1]"
    SECTION_LINK = By.XPATH, "//div[@id='texToolTopContainer']/a[2]"

    TOOL_TIP = By.CLASS_NAME, "tooltip-inner"


class MenuPageLocators:
    MENU_ITEM_LIST = By.XPATH, "//ul[@id='nav']//li//a"

    MAIN_ITEM_LIST = By.XPATH, "//ul[@id='nav']/li"
    MAIN_ITEM_1 = By.XPATH, "//a[text()='Main Item 1']"
    MAIN_ITEM_2 = By.XPATH, "//a[text()='Main Item 2']"
    SUB_ITEM_ONE = By.XPATH, "//a[text()='Main Item 2']/following-sibling::ul/li[1]/a"
    SUB_ITEM_TWO = By.XPATH, "//a[text()='Main Item 2']/following-sibling::ul/li[2]/a"
    SUB_SUB_LIST = By.XPATH, "//a[text()='Main Item 2']/following-sibling::ul/li[3]/a"
    SUB_SUB_ITEM_1 = By.XPATH, "//a[text()='Sub Sub Item 1']"
    SUB_SUB_ITEM_2 = By.XPATH, "//a[text()='Sub Sub Item 2']"

    MAIN_ITEM_3 = By.XPATH, "//a[text()='Main Item 3']"


class SelectMenuLocators:
    SELECT_VALUE_INPUT = By.ID, "withOptGroup"
    SELECT_VALUE_OPTION_LIST = By.XPATH, "//div[contains(@id, 'react-select-2-option')]"
    SELECT_VALUE_TEXT = By.XPATH, "//div[@id='withOptGroup']//div[@class=' css-1uccc91-singleValue']"

    SELECT_ONE_INPUT = By.ID, "selectOne"
    SELECT_ONE_OPTION_LIST = By.XPATH, "//div[contains(@id, 'react-select-3-option')]"
    SELECT_ONE_TEXT = By.XPATH, "//div[@id='selectOne']//div[@class=' css-1uccc91-singleValue']"

    OLD_STYLE_SELECT_MENU = By.ID, "oldSelectMenu"

    MULTISELECT_DROP_DOWN = By.XPATH, "(//div[@class=' css-2b097c-container'])[3]"
    MULTISELECT_DROP_DOWN_OPTIONS = By.XPATH, "//div[contains(@id, 'react-select-4-option-')]"
    MULTISELECT_DROP_DOWN_CHOICES_COLORS = By.CLASS_NAME, "css-12jo7m5"

    STANDARD_MULTI_SELECT = By.ID, "cars"
