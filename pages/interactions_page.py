import random

import allure

from curl import SORTABLE_URL, SELECTABLE_URL, RESIZABLE_URL
from generation import Generation
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
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
