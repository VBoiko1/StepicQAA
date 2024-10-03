from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
       return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)

    x_element = browser.find_element(By.XPATH, "//*[@id='treasure']")
    x = x_element.get_attribute("valuex") # Записывает значение атрибута из консоли (В данном примере атрибут - "valuex")
    #x = x_element.text # Копирует и записывает значение 

    y = calc(x)

    input = browser.find_element(By.XPATH, "//input[@id='answer']")
    input.send_keys(y)
    time.sleep(2)

    input1 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    input1.click()

    input2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    input2.click()
    time.sleep(2)

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()

    time.sleep(15)




finally:
    browser.quit()
