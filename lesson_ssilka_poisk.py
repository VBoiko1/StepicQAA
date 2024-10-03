import math

from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/find_link_text")
time.sleep(5)

# link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
# link.click()
# time.sleep(10)

link = driver.find_element(By.LINK_TEXT,'224592') # Поиск текста с гипер-ссылкой
link.click()
time.sleep(10)

driver.quit()
