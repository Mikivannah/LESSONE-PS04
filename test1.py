import time
from selenium import webdriver
browser = webdriver.Chrome
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(10)
browser.get("https://en.wikipedia.org/wiki/HTML")
time.sleep(10)
browser.quit()