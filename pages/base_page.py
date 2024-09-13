from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment/"

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(
                ec.presence_of_element_located(locator),
                message=f"Не удалось найти элемент по локатору {locator}"
            )
        except TimeoutException:
            print(f"Элемент не найден: {locator}")
            return None  # Возвращаем None, если элемент не найден

    def find_elements(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(
                ec.presence_of_all_elements_located(locator),
                message=f"Не удалось найти элементы по локатору {locator}"
            )
        except TimeoutException:
            print(f"Элементы не найдены: {locator}")
            return []  # Возвращаем пустой список, если элементы не найдены

    def find_clickable_element(self, locator, time=10):
        """Находит элемент, который можно кликнуть."""
        try:
            return WebDriverWait(self.driver, time).until(
                ec.element_to_be_clickable(locator),
                message=f"Не удалось найти кликабельный элемент по локатору {locator}"
            )
        except TimeoutException:
            print(f"Кликабельный элемент не найден: {locator}")
            return None  # Возвращаем None, если элемент не найден

    def go_to_site(self):
        self.driver.get(self.base_url)  # Переход на базовый URL
