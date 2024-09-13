from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from pages import MainPage


def test_back_to_main():
    driver_path = r"chromedriver.exe"
    site_url = r"https://makarovartem.github.io/frontend-avito-tech-test-assignment"
    main_page = MainPage(driver_path, site_url)
    main_page.go_to_site()

    try:
        # Ожидаем, пока элемент фильтра станет доступным
        category_filter = WebDriverWait(main_page.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "span.ant-select-selection-item[title='mmorpg']"))
        )

        # Взаимодействуем с элементом фильтра
        category_filter.click()  # Кликаем на элемент фильтра

    except Exception as e:
        print(f"Ошибка при взаимодействии с фильтром: {e}")

    try:
        # Ожидаем, пока игровые карточки станут доступными
        game_cards = WebDriverWait(main_page.driver, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".game-card"))
        )

        if game_cards:
            # Взаимодействие с первым элементом
            game_cards[0].click()
        else:
            print("Игровые карточки не найдены.")

    except Exception as e:
        print(f"Ошибка при взаимодействии с игровыми карточками: {e}")

    finally:
        main_page.close()
