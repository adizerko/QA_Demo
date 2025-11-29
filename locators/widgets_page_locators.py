from selenium.webdriver.common.by import By


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
