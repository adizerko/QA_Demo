import random
import time

import allure

from curl import SORTABLE_URL, SELECTABLE_URL, RESIZABLE_URL, DROPPABLE_URL
from generation import Generation
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators

    @allure.step("Открыть страницу Sortable")
    def open_sortable_page(self):
        self.open(SORTABLE_URL)

    @allure.step("Переключиться на вкладку Grid")
    def click_tab_grid(self):
        self.click(self.locators.GRID)

    @allure.step("Получить текст элементов для проверки порядка")
    def get_tab_items_text(self, elements_locator):
        tab_elements = self.get_elements(elements_locator)
        after_sort = []

        for tab in tab_elements:
            after_sort.append(tab.text)

        return after_sort

    @allure.step("Перетащить элементы в обратном порядке")
    def reverse_sorting(self, items_texts, target):
        for item in items_texts:
            self.drag_and_drop_elements(item, target)

    @allure.step("Перетащить элемент '{first_locator}' → '{second_locator}'")
    def drag_and_drop_elements(self, first_locator, second_locator):
        self.drag_and_drop(first_locator, second_locator)


class SelectablePage(BasePage):
    locators = SelectablePageLocators

    @allure.step("Открываем страницу Selectable")
    def open_selectable_page(self):
        self.open(SELECTABLE_URL)

    @allure.step("Переходим на вкладку Grid")
    def click_tab_grid(self):
        self.click(self.locators.GRID)

    @allure.step("Выбираем случайные элементы списка/сетки")
    def select_random_items(self, items_list):
        items_to_select = Generation.selecting_random_elements(self.get_elements(items_list))
        selected_items = []

        for el in items_to_select:
            el.click()
            selected_items.append(el.text)

        allure.attach(", ".join(selected_items), "Выбранные элементы")
        return set(selected_items)

    @allure.step("Получаем текст выбранных элементов")
    def get_selected_items_text(self, selectable_items_list):
        selectable_elements = self.get_elements(selectable_items_list)
        selected_items = [item.text for item in selectable_elements]
        allure.attach(", ".join(selected_items), "Фактические выбранные элементы")
        return set(selected_items)


class ResizablePage(BasePage):
    locators = ResizablePageLocators

    @allure.step("Открываем страницу 'Resizable'")
    def open_resizable_page(self):
        self.open(RESIZABLE_URL)

    @allure.step("Изменяем размеры элемента до ширины {target_width}px и высоты {target_height}px")
    def resize_box(self, target_width: int, target_height: int):
        current_width, current_height = self.get_box_size()

        delta_x = target_width - current_width
        delta_y = target_height - current_height

        handle  = self.wait_for_element(self.locators.RESIZABLE_RESTRICTION_BOX_HANDLE)
        self.action_drag_and_drop_by_offset(handle, delta_x, delta_y)

    @allure.step("Получаем текущие размеры элемента")
    def get_box_size(self):
        attribute = self.get_attribute(self.locators.RESIZABLE_RESTRICTION_BOX, "style")
        width = int(attribute.split("th: ")[1].split("px")[0])
        height = int(attribute.split("ht: ")[1].split("px")[0])
        return width, height


class DroppablePage(BasePage):
    locators = DroppablePageLocators

    @allure.step("Открываем страницу Droppable")
    def open_droppable_page(self):
        self.open(DROPPABLE_URL)

    @allure.step("Переходим на вкладку Accept")
    def click_accept_tab(self):
        self.click(self.locators.TAB_ACCEPT)

    @allure.step("Переходим на вкладку Prevent Propagation")
    def click_prevent_propogation_tab(self):
        self.click(self.locators.TAB_PREVENT_PROPOGATION)

    @allure.step("Переходим на вкладку Revert Draggable")
    def click_revert_draggable_tab(self):
        self.click(self.locators.TAB_REVERT_DRAGGABLE)

    @allure.step("Перетаскиваем элемент в Simple box")
    def drop_draggable_to_simple_box(self):
        self.drag_and_drop(self.locators.DRAGGABLE, self.locators.DROPPABLE)

    @allure.step("Перетаскиваем Acceptable в Accept box")
    def drop_acceptable_to_accept_box(self):
        self.drag_and_drop(self.locators.ACCEPTABLE, self.locators.ACCEPT_DROPPABLE)

    @allure.step("Перетаскиваем Not Acceptable в Accept box")
    def drop_not_acceptable_to_accept_box(self):
        self.drag_and_drop(self.locators.NOT_ACCEPTABLE, self.locators.ACCEPT_DROPPABLE)

    @allure.step("Перетаскиваем элемент внутрь Not Greedy box")
    def drop_on_inner_not_greedy_box(self):
        self.drag_and_drop(self.locators.DRAG_ME, self.locators.INNER_DROPPABLE)

    @allure.step("Перетаскиваем элемент внутрь Greedy box")
    def drop_on_inner_greedy_box(self):
        self.drag_and_drop(self.locators.DRAG_ME, self.locators.GREEDY_DROP_BOX_INNER)

    @allure.step("Перетаскиваем Will Revert и ждём возврата")
    def drop_will_revert(self):
        self.drag_and_drop(self.locators.REVERT_ABLE, self.locators.DROPPABLE_REVERT)
        time.sleep(0.5)

    @allure.step("Перетаскиваем Not Revert")
    def drop_not_revert(self):
        self.drag_and_drop(self.locators.NOT_REVERT_ABLE, self.locators.DROPPABLE_REVERT)

    @allure.step("Получаем текст в simple droppable")
    def get_text_drop_box(self):
        return self.get_text(self.locators.DROPPABLE_TEXT)

    @allure.step("Получаем текст Accept droppable")
    def drop_box_accept_text(self):
        return self.get_text(self.locators.ACCEPT_DROPPABLE)

    @allure.step("Получаем текст Outer droppable")
    def outer_text(self):
        return self.get_text(self.locators.OUTER_DROPPABLE_TEXT)

    @allure.step("Получаем текст Inner droppable")
    def inner_text(self):
        return self.get_text(self.locators.INNER_DROPPABLE_TEXT)

    @allure.step("Получаем текст Greedy Inner droppable")
    def greedy_inner_text(self):
        return self.get_text(self.locators.GREEDY_DROP_BOX_INNER_TEXT)

    @allure.step("Получаем текст Greedy Outer droppable")
    def greedy_outer_text(self):
        return self.get_text(self.locators.GREEDY_DROP_BOX_TEXT)

    @allure.step("Получаем текст для зоны Revert droppable")
    def droppable_revert_text(self):
        return self.get_text(self.locators.DROPPABLE_REVERT_TEXT)

    @allure.step("Получаем позицию Will Revert box")
    def get_position_revert_box(self):
        position = self.get_element_position(self.locators.REVERT_ABLE)
        return position

    @allure.step("Получаем позицию Not Revert box")
    def get_position_not_revert_box(self):
        position = self.get_element_position(self.locators.NOT_REVERT_ABLE)
        return position
