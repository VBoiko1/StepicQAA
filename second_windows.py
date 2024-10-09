from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link  = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button =browser.find_element(By.CSS_SELECTOR, '[class*="btn"]').click()
    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    num = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = num.text

    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    button_finally = browser.find_element(By.CSS_SELECTOR, '[class*="btn"]').click()



    time.sleep(10)


finally:
    browser.quit()