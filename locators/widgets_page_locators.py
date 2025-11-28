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
