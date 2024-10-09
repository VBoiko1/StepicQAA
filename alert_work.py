from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link  = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, '[class*="btn"]')
    button.click()

    alert_confirm = browser.switch_to.alert
    alert_confirm.accept()

    num =browser.find_element(By.CSS_SELECTOR, '#input_value')
    x =num.text

    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, "[class*='btn']").click()

    print(browser.switch_to.alert.text)


   





    time.sleep(10)
finally:

    browser.quit()