from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage


class MainPage(BasePage):
    PLATFORM_FILTER = (By.CSS_SELECTOR, "select[aria-label='Filter by platform']")
    CATEGORY_FILTER = (By.CSS_SELECTOR, "select[aria-label='Filter by category']")
    SORT_FILTER = (By.CSS_SELECTOR, "select[aria-label='Sort by']")
    GAME_CARDS = (By.CSS_SELECTOR, ".game-card")
    PAGINATION = (By.CSS_SELECTOR, ".pagination")
    NEXT_PAGE = (By.CSS_SELECTOR, ".pagination .next")
    BACK_TO_MAIN = (By.LINK_TEXT, "Back to main")

    def select_platform(self, platform):
        select = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.PLATFORM_FILTER)
        )
        select.find_element(By.XPATH, f"//option[text()='{platform}']").click()

    def select_category(self, category):
        select = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.CATEGORY_FILTER)
        )
        select.find_element(By.XPATH, f"//option[text()='{category}']").click()

    def get_game_cards(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(self.GAME_CARDS)
        )
        return self.find_elements(self.GAME_CARDS)

    def go_to_next_page(self):
        next_page = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.NEXT_PAGE)
        )
        next_page.click()

    def go_back_to_main(self):
        back_to_main = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.BACK_TO_MAIN)
        )
        back_to_main.click()

    def close(self):
        pass
