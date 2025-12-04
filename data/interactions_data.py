from faker.generator import random

from locators.interactions_page_locators import SortablePageLocators


class SortableData:
    locators = SortablePageLocators

    ITEMS_LIST_TO_REVERSE = [
        locators.SIX_LIST,
        locators.FIVE_LIST,
        locators.FOUR_LIST,
        locators.THREE_LIST,
        locators.TWO_LIST,
    ]

    ITEMS_GRID_TO_REVERSE = [
        locators.NINE_GRID,
        locators.EIGHT_GRID,
        locators.SEVEN_GRID,
        locators.SIX_GRID,
        locators.FIVE_GRID,
        locators.FOUR_GRID,
        locators.THREE_GRID,
        locators.TWO_GRID

    ]

    expected_sort_by_list = ["Six", "Five", "Four", "Three", "Two", "One"]
    expected_sort_by_grid = ["Nine","Eight","Seven","Six", "Five", "Four",
                             "Three", "Two", "One"]
    SORT = [
        (locators.LIST, locators.TAB_LISTS, ITEMS_LIST_TO_REVERSE, locators.ONE_LIST, expected_sort_by_list),
        (locators.GRID, locators.TAB_GRIDS, ITEMS_GRID_TO_REVERSE, locators.ONE_GRID, expected_sort_by_grid)
    ]


class ResizableData:
    BOX_SIZES = [
        (150, 150),
        (500, 300),
        (random.randint(150,500), random.randint(150,300))
    ]


class DroppableData:
    success_text = "Dropped!"
    expected_not_drop_text = "Drop here"
    expected_inner_text = "Inner droppable (not greedy)"
    outer_default_text = "Outer droppable"
    position_after_move = {'x': 1142, 'y': 385}
