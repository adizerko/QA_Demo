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
