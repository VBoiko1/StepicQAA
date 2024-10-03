# # from selenium import webdriver
# # browser = webdriver.Chrome()
# # import time
# # browser.execute_script("document.title='Script executing';alert('Robots at work');")
# # #browser.execute_script("alert('Robots at work');")
# # time.sleep(10)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("window.scrollBy(0, 4000);")
# button.click()
# time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link  = ' https://SunInJuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # JavaScript для скрола страницы
    browser.execute_script("window.scrollBy(0, 100);")

 # считывает число с экрана и записывает его в переменную "х"
    x_num = browser.find_element(By.ID, 'input_value') 
    x = x_num.text
 # Вычисляем форму из функции def 
    y = calc(x)
# Ишем поле для ввода результата и вставляем его
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    # Ищем чек-бокс "I'm the robot" ставим галочу в чек-боксе
    chek = browser.find_element(By.ID, "robotCheckbox").click()

    
    
    
    # Переключить радиобатон "Robots rule"
    radio = browser.find_element(By.ID, "robotsRule").click()

    # Нажать кнопку Submit
    button = browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(10)


finally:

    browser.quit()





