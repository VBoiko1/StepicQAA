# В этом задании в форме регистрации требуется загрузить текстовый файл.

# Напишите скрипт, который будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Viktor')

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Boiko")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.com")
    #time.sleep(10)
    
### ЗАГРУЗКА ФАЙЛА - 
    current_dir = os.path.abspath(os.path.dirname('zagruzka_file.py')) # Указать наименования файла из которого выполняется код
    file = 'file.xlsx'             # Важно чтобы загружаемый файл лежал в той же папке где и файл кода
    path = os.path.join(current_dir, file)


    button = browser.find_element(By.XPATH, "//input[@id='file']")
    button.send_keys(path)

    end = browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(10)

finally:
    browser.quit()    