import time

import allure
import pytest

from data import SortableData, ResizableData, DroppableData
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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


    @allure.feature("Droppable")
    class TestDroppable:
        @allure.story("Simple droppable")
        def test_simple_drop(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.drop_draggable_to_simple_box()
            actual_text = droppable_page.get_text_drop_box()

            assert actual_text == DroppableData.success_text

        @allure.story("Accept — box принимает только Acceptable")
        def test_accept_drop(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_accept_tab()
            droppable_page.drop_acceptable_to_accept_box()
            actual_text = droppable_page.drop_box_accept_text()

            assert actual_text == DroppableData.success_text

        @allure.story("Accept — Not Acceptable не активирует зону")
        def test_not_accept(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_accept_tab()
            droppable_page.drop_not_acceptable_to_accept_box()
            actual_text = droppable_page.drop_box_accept_text()

            assert actual_text == DroppableData.expected_not_drop_text

        @allure.story("Prevent Propagation — Not Greedy обновляет оба бокса")
        def test_not_greedy_updates_both(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_prevent_propogation_tab()
            droppable_page.drop_on_inner_not_greedy_box()

            outer_after_drop = droppable_page.outer_text()
            inner_after_drop = droppable_page.inner_text()

            assert outer_after_drop == DroppableData.success_text
            assert inner_after_drop == DroppableData.success_text

        @allure.story("Prevent Propagation — Greedy обновляется только внутренний бокс")
        def test_greedy_updates_only_inner(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_prevent_propogation_tab()
            droppable_page.drop_on_inner_greedy_box()

            actual_text_outer = droppable_page.greedy_outer_text()
            actual_text_inner = droppable_page.greedy_inner_text()

            assert actual_text_outer == DroppableData.outer_default_text
            assert actual_text_inner == DroppableData.success_text

        @allure.story("Revert — элемент возвращается обратно после drop")
        def test_revert_after_drop(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_revert_draggable_tab()
            before_position = droppable_page.get_position_revert_box()
            droppable_page.drop_will_revert()

            actual_text_revert_box = droppable_page.droppable_revert_text()
            after_position = droppable_page.get_position_revert_box()

            assert actual_text_revert_box == DroppableData.success_text
            assert before_position == after_position

        @allure.story("Revert — Not Revert остаётся на новой позиции")
        def test_not_revert_after_drop(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_revert_draggable_tab()
            droppable_page.drop_not_revert()
            position_after_move = droppable_page.get_position_not_revert_box()
            actual_text_not_revert_box = droppable_page.droppable_revert_text()

            assert position_after_move == DroppableData.position_after_move
            assert actual_text_not_revert_box == DroppableData.success_text
