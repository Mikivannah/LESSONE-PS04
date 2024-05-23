from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.google.com/')


browser = webdriver.Chrome()

#В кавычках указываем URL сайта, на который нам нужно зайти
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(5)
driver.quit()