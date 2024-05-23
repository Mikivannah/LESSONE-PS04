# Напишите программу,  на языке Python с помощью которой можно искать информацию
# на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.
#"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Если хотите видеть браузер, закомментируйте эту строку
    driver = webdriver.Chrome(options=options)
    return driver

def search_wikipedia(query, driver):
    driver.get('https://www.wikipedia.org/')
    search_box = driver.find_element(By.NAME, 'search')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Даем время на загрузку страницы

def print_paragraphs(driver):
    paragraphs = driver.find_elements(By.CSS_SELECTOR, 'p')
    for index, paragraph in enumerate(paragraphs):
        print(f"Paragraph {index + 1}:\n{paragraph.text}\n")

def list_internal_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, 'div#bodyContent a')
    internal_links = [link for link in links if link.get_attribute('href') and '/wiki/' in link.get_attribute('href') and ':' not in link.get_attribute('href')]
    for index, link in enumerate(internal_links):
        print(f"{index + 1}: {link.text} - {link.get_attribute('href')}")
    return internal_links

def main():
    driver = get_driver()
    try:
        query = input("Введите запрос для поиска на Википедии: ")
        search_wikipedia(query, driver)

        while True:
            print("Выберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            choice = input("Ваш выбор: ")

            if choice == '1':
                print_paragraphs(driver)
            elif choice == '2':
                internal_links = list_internal_links(driver)
                link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
                if 0 <= link_choice < len(internal_links):
                    driver.get(internal_links[link_choice].get_attribute('href'))
                    time.sleep(2)  # Даем время на загрузку страницы
                else:
                    print("Неверный выбор ссылки.")
            elif choice == '3':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()