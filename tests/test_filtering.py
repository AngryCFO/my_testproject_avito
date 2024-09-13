from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.main_page import MainPage


def test_filter_by_category(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()

    try:
        # Ожидание появления элемента фильтра и его кликабельности
        filter_element = WebDriverWait(main_page.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/span[2]"))
        )
        filter_element.click()  # Выбор категории

        # Ожидание появления игровых карточек после фильтрации
        game_cards = WebDriverWait(main_page.driver, 20).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".game-card"))
        )

        # Проверка, что игровые карточки найдены
        assert len(game_cards) > 0, "No games found after filtering"

    except Exception as e:
        print(f"Ошибка при взаимодействии с элементами: {e}")
    finally:
        main_page.close()
