import allure

from curl import SORTABLE_URL
from locators.interactions_page_locators import SortablePageLocators
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
