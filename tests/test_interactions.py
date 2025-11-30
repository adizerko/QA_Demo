
import allure
import pytest

from data import SortableData, ResizableData
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    @allure.feature("Selectable")
    class TestSelectable:
        @allure.title("Проверка выбора случайных элементов в List")
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver)
            selectable_page.open_selectable_page()

            expected_selected_items = selectable_page.select_random_items(
                SelectablePageLocators.ITEMS_LIST)
            actual_selected_items = selectable_page.get_selected_items_text(
                SelectablePageLocators.SELECT_ITEMS_LIST)

            assert expected_selected_items == actual_selected_items

        @allure.title("Проверка выбора случайных элементов в Grid")
        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver)
            selectable_page.open_selectable_page()
            selectable_page.click_tab_grid()

            expected_selected_items = selectable_page.select_random_items(
                SelectablePageLocators.GRID_LIST)
            actual_selected_items = selectable_page.get_selected_items_text(
                SelectablePageLocators.GRID_SELECT_LIST)

            assert expected_selected_items == actual_selected_items

    @allure.feature("Resizable")
    class TestResizable:
        @allure.title("Изменение размера ограниченного resizable-бокса")
        @pytest.mark.parametrize(
            "width, height", ResizableData.BOX_SIZES, ids=["min size", "max size", "random size"])
        def test_resizable_box(self, driver, width, height):
            resizable_page = ResizablePage(driver)
            resizable_page.open_resizable_page()
            resizable_page.resize_box(width, height)
            actual_width, actual_height = resizable_page.get_box_size()

            assert actual_width == width, f"Ожидалось {width}px, получено {actual_width}px"
            assert actual_height == height, f"Ожидалось {height}px, получено {actual_height}px"
