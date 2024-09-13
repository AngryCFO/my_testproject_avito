from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.main_page import MainPage


def test_pagination(browser):
    driver_path = r"chromedriver.exe"
    site_url = r"https://makarovartem.github.io/frontend-avito-tech-test-assignment"
    main_page = MainPage(browser)
    main_page.go_to_site()

    try:
        # Ожидаем, пока игровые карточки станут доступными
        game_cards = WebDriverWait(main_page.driver, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".game-card"))
        )

        if game_cards:
            # Взаимодействие с элементами
            for card in game_cards:
                card.click()  # Или другое взаимодействие
        else:
            print("Игровые карточки не найдены.")

        # Ожидаем, пока элемент фильтра станет доступным
        filter_element = WebDriverWait(main_page.driver, 10).until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/span[2]"))
        )

        if filter_element:
            filter_element.click()  # Взаимодействие с элементом фильтра
        else:
            print("Элемент фильтра не найден.")

    except Exception as e:
        print(f"Ошибка при взаимодействии с игровыми карточками или фильтром: {e}")
