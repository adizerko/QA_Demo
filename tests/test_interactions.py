import allure

from data import SortableData
from locators.interactions_page_locators import SortablePageLocators
from pages.interactions_page import SortablePage


@allure.suite("Interactions")
class TestInteractions:
    @allure.feature("Sortable")
    class TestSortable:

        @allure.title("Сортировка списка — обратный порядок")
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver)
            sortable_page.open_sortable_page()
            sortable_page.reverse_sorting(
                SortableData.ITEMS_LIST_TO_REVERSE, SortablePageLocators.ONE_LIST)
            after_sort = sortable_page.get_tab_items_text(
                SortablePageLocators.TAB_LISTS, )

            assert after_sort == SortableData.expected_sort_by_list

        @allure.title("Сортировка сетки — обратный порядок")
        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver)
            sortable_page.open_sortable_page()
            sortable_page.click_tab_grid()
            sortable_page.reverse_sorting(
                SortableData.ITEMS_GRID_TO_REVERSE, SortablePageLocators.ONE_GRID)
            after_sort = sortable_page.get_tab_items_text(
                SortablePageLocators.TAB_GRIDS)

            assert after_sort == SortableData.expected_sort_by_grid
