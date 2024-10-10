from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = ' http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    
    browser = webdriver.Chrome()
    browser.get(link) 
    browser.maximize_window()

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'),"100")
    )
    button = browser.find_element(By.CSS_SELECTOR, '#book').click()

     # JavaScript для скрола страницы
    browser.execute_script("window.scrollBy(0, 300);")

    num = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = num.text
    y = calc(x)

    button1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, '#solve').click()
    
    # Запись текста из алерта

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

   


finally:
    time.sleep(10)

    browser.quit()