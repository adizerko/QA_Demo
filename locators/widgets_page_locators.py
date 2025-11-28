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
