from selenium.webdriver.common.by import By


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
