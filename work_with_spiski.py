from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
link = "https://suninjuly.github.io/selects2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)


    num_1 = browser.find_element(By.ID, 'num1')
    x = num_1.text


    num_2 = browser.find_element(By.ID, "num2")
    y = num_2.text

    z = int(x) + int(y)
    z = str(z)

    button = Select(browser.find_element(By.TAG_NAME, 'select'))
    button.select_by_value(z)
    time.sleep(1)

    button2 = browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(10)


finally:

    
    browser.quit()

