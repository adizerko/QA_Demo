import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from data.interactions_data import SortableData, ResizableData, DroppableData
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite("Interactions")
class TestInteractions:

    @allure.feature("Sortable")
    class TestSortable:
        @allure.title("Сортировка списка — обратный порядок")
        def test_sortable_list(self, driver: WebDriver) -> None:
            sortable_page = SortablePage(driver)
            sortable_page.open_sortable_page()
            sortable_page.reverse_sorting(
                SortableData.ITEMS_LIST_TO_REVERSE, SortablePageLocators.ONE_LIST)
            after_sort = sortable_page.get_tab_items_text(
                SortablePageLocators.TAB_LISTS, )

            assert after_sort == SortableData.expected_sort_by_list, \
                f"Список отсортирован некорректно: {after_sort}"

        @allure.title("Сортировка сетки — обратный порядок")
        def test_sortable_grid(self, driver: WebDriver) -> None:
            sortable_page = SortablePage(driver)
            sortable_page.open_sortable_page()
            sortable_page.click_tab_grid()
            sortable_page.reverse_sorting(
                SortableData.ITEMS_GRID_TO_REVERSE, SortablePageLocators.ONE_GRID)
            after_sort = sortable_page.get_tab_items_text(
                SortablePageLocators.TAB_GRIDS)

            assert after_sort == SortableData.expected_sort_by_grid, \
                f"Сетка отсортирована неверно: {after_sort}"

    @allure.feature("Selectable")
    class TestSelectable:
        @allure.title("Проверка выбора случайных элементов в List")
        def test_selectable_list(self, driver: WebDriver) -> None:
            selectable_page = SelectablePage(driver)
            selectable_page.open_selectable_page()

            expected_selected_items = selectable_page.select_random_items(
                SelectablePageLocators.ITEMS_LIST)
            actual_selected_items = selectable_page.get_selected_items_text(
                SelectablePageLocators.SELECT_ITEMS_LIST)

            assert expected_selected_items == actual_selected_items, \
                (f"Ожидались выбранные элементы {expected_selected_items},"
                 f" но фактически {actual_selected_items}")

        @allure.title("Проверка выбора случайных элементов в Grid")
        def test_selectable_grid(self, driver: WebDriver) -> None:
            selectable_page = SelectablePage(driver)
            selectable_page.open_selectable_page()
            selectable_page.click_tab_grid()

            expected_selected_items = selectable_page.select_random_items(
                SelectablePageLocators.GRID_LIST)
            actual_selected_items = selectable_page.get_selected_items_text(
                SelectablePageLocators.GRID_SELECT_LIST)

            assert expected_selected_items == actual_selected_items, \
                (f"Ожидались выбранные элементы {expected_selected_items},"
                 f" получили {actual_selected_items}")

    @allure.feature("Resizable")
    class TestResizable:

        @allure.title("Изменение размера ограниченного resizable-бокса")
        @pytest.mark.parametrize("width, height",
                                 ResizableData.BOX_SIZES,
                                 ids=["min size", "max size", "random size"])
        def test_resizable_box(self, driver: WebDriver, width: int, height: int) -> None:
            resizable_page = ResizablePage(driver)
            resizable_page.open_resizable_page()
            resizable_page.resize_box(width, height)
            actual_width, actual_height = resizable_page.get_box_size()

            assert actual_width == width,\
                f"Ожидалось {width}px, получено {actual_width}px"
            assert actual_height == height,\
                f"Ожидалось {height}px, получено {actual_height}px"

    @allure.feature("Droppable")
    class TestDroppable:

        @allure.story("Simple droppable")
        def test_simple_drop(self, driver: WebDriver) -> None:
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.drop_draggable_to_simple_box()
            actual_text = droppable_page.get_text_drop_box()

            assert actual_text == DroppableData.success_text, \
                f"Ожидали '{DroppableData.success_text}', получили '{actual_text}'"

        @allure.story("Accept — box принимает только Acceptable")
        def test_accept_drop(self, driver: WebDriver) -> None:
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_accept_tab()
            droppable_page.drop_acceptable_to_accept_box()
            actual_text = droppable_page.drop_box_accept_text()

            assert actual_text == DroppableData.success_text, \
                f"Accept-box должен успешно принять элемент, получили '{actual_text}'"

        @allure.story("Accept — Not Acceptable не активирует зону")
        def test_not_accept(self, driver: WebDriver) -> None:
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_accept_tab()
            droppable_page.drop_not_acceptable_to_accept_box()
            actual_text = droppable_page.drop_box_accept_text()

            assert actual_text == DroppableData.expected_not_drop_text, \
                (f"Ожидали '{DroppableData.expected_not_drop_text}',"
                 f" получили '{actual_text}'")

        @allure.story("Prevent Propagation — Not Greedy обновляет оба бокса")
        def test_not_greedy_updates_both(self, driver: WebDriver) -> None:
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_prevent_propogation_tab()
            droppable_page.drop_on_inner_not_greedy_box()

            outer_after_drop = droppable_page.outer_text()
            inner_after_drop = droppable_page.inner_text()

            assert outer_after_drop == DroppableData.success_text, \
                f"Внешний бокс должен обновиться, получили '{outer_after_drop}'"

            assert inner_after_drop == DroppableData.success_text, \
                f"Внутренний бокс должен обновиться, получили '{inner_after_drop}'"

        @allure.story("Prevent Propagation — Greedy обновляется только внутренний бокс")
        def test_greedy_updates_only_inner(self, driver: WebDriver) -> None:
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_prevent_propogation_tab()
            droppable_page.drop_on_inner_greedy_box()

            actual_text_outer = droppable_page.greedy_outer_text()
            actual_text_inner = droppable_page.greedy_inner_text()

            assert actual_text_outer == DroppableData.outer_default_text, \
                f"Внешний бокс не должен обновляться, получили '{actual_text_outer}'"

            assert actual_text_inner == DroppableData.success_text, \
                f"Внутренний бокс должен обновиться, получили '{actual_text_inner}'"

        @allure.story("Revert — элемент возвращается обратно после drop")
        def test_revert_after_drop(self, driver: WebDriver) -> None:
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_revert_draggable_tab()
            before_position = droppable_page.get_position_revert_box()
            droppable_page.drop_will_revert()

            actual_text_revert_box = droppable_page.droppable_revert_text()
            after_position = droppable_page.get_position_revert_box()

            assert actual_text_revert_box == DroppableData.success_text, \
                (f"Ожидали '{DroppableData.success_text}',"
                 f" получили '{actual_text_revert_box}'")

            assert before_position == after_position, \
                (f"Элемент должен вернуться обратно: было {before_position},"
                 f" стало {after_position}")

        @allure.story("Revert — Not Revert остаётся на новой позиции")
        def test_not_revert_after_drop(self, driver: WebDriver) -> None:
            droppable_page = DroppablePage(driver)
            droppable_page.open_droppable_page()
            droppable_page.click_revert_draggable_tab()
            droppable_page.drop_not_revert()

            position_after_move = droppable_page.get_position_not_revert_box()
            actual_text_not_revert_box = droppable_page.droppable_revert_text()

            assert position_after_move == DroppableData.position_after_move, \
                (f"Ожидали позицию {DroppableData.position_after_move},"
                 f" получили {position_after_move}")

            assert actual_text_not_revert_box == DroppableData.success_text, \
                (f"Ожидали текст '{DroppableData.success_text}',"
                 f" получили '{actual_text_not_revert_box}'")

    @allure.feature("Draggable")
    class TestDraggable:
        @allure.title("Тест простого перетаскивания элемента Drag Me")
        def test_draggable_simple(self, driver: WebDriver) -> None:
            draggable_page = DraggablePage(driver)
            draggable_page.open_draggable_page()

            before_x, before_y = draggable_page.get_position_drag_me()
            offset_x, offset_y = draggable_page.move_random_position_drag_me()
            after_x, after_y = draggable_page.get_position_drag_me()

            assert after_x == before_x + offset_x, \
                f"Ожидали X={before_x + offset_x}, получили X={after_x}"

            assert after_y == before_y + offset_y, \
                f"Ожидали Y={before_y + offset_y}, получили Y={after_y}"

        @allure.title("Тест ограничения по оси X")
        def test_axis_restricted_only_x(self, driver: WebDriver) -> None:
            draggable_page = DraggablePage(driver)
            draggable_page.open_draggable_page()
            draggable_page.click_axis_restricted_tab()

            before_x = draggable_page.get_position_only_x()
            offset_x = draggable_page.move_random_only_x_element()
            after_x = draggable_page.get_position_only_x()

            assert after_x == before_x + offset_x, \
                f"Ожидали X={before_x + offset_x}, получили X={after_x}"

        @allure.title("Тест ограничения по оси Y")
        def test_axis_restricted_only_y(self, driver: WebDriver) -> None:
            draggable_page = DraggablePage(driver)
            draggable_page.open_draggable_page()
            draggable_page.click_axis_restricted_tab()

            before_y = draggable_page.get_position_only_y()
            offset_y = draggable_page.move_random_only_y_element()
            after_y = draggable_page.get_position_only_y()

            assert after_y == before_y + offset_y, \
                f"Ожидали Y={before_y + offset_y}, получили Y={after_y}"

        @allure.title("Тест ограниченного контейнера: элемент не выходит за пределы")
        def test_restricted_box_inside_container(self, driver: WebDriver) -> None:
            draggable_page = DraggablePage(driver)
            draggable_page.open_draggable_page()
            draggable_page.click_container_restricted_tab()

            draggable_page.move_random_position_restricted_box()
            inside = draggable_page.is_inside_container()

            assert inside, "Элемент вышел за пределы контейнера, а не должен"
