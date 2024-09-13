from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class MainPage:
    def __init__(self, dr_path, s_url):
        # Настройка опций для Chrome, если это необходимо
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (опционально)

        # Инициализация WebDriver с указанным путём к драйверу
        self.driver = webdriver.Chrome(service=Service(dr_path), options=chrome_options)
        self.url = s_url  # Присваивание URL

    def go_to_site(self):
        try:
            self.driver.get(self.url)
        except Exception as ex:
            print(f"Ошибка при переходе на сайт: {ex}")

    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Ошибка при закрытии драйвера: {e}")


# Пример использования
if __name__ == "__main__":
    # Путь к драйверу и URL сайта
    driver_path = r"chromedriver.exe"
    site_url = r"https://makarovartem.github.io/frontend-avito-tech-test-assignment"

    main_page = None
    try:
        # Передача параметров в конструктор MainPage
        main_page = MainPage(driver_path, site_url)
        main_page.go_to_site()
    except Exception as exc:
        print(f"Произошла ошибка: {exc}")
    finally:
        if main_page:
            main_page.close()
