from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(10)
browser.get("https://ru.wikipedia.org/wiki/Selenium")

# Добавляем автоматизированный скриншотинг
browser.save_screenshot("dom.png")      # в скобках в ковычках указываем имя файла скриншота, имена должны быть разные
time.sleep(10)

# Добавляем автоматизированный скриншотинг для другой страницы
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png") # обрати внимание что скриншоты легли в папку проекта
time.sleep(3)

#. Добавляем перезагрузку страницы:
browser.refresh()







driver.quit()