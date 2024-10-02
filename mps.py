import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 15 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(10)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://survey-service-trunk.rts-tender.ru/")
time.sleep(10)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. 
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать

# Ищем поле "Организация" для ввода текста
textarea = driver.find_element(By.XPATH, "//input[@class='p-element ng-tns-c45-3 p-autocomplete-input p-inputtext p-component rts-control-l ng-star-inserted']")

# Напишем текст ответа в найденное поле "Организация"
textarea.send_keys("9723098918")
time.sleep(10)

# Выбор организации из выподающего списка
submit_button = driver.find_element(By.CSS_SELECTOR, "div.ng-star-inserted")
submit_button.click()
time.sleep(10)

# Ищем поле "Заполнил" для ввода текста
textarea = driver.find_element(By.XPATH, "//input[@placeholder='ФИО сотрудника']")
textarea.send_keys("Иванов Иван Иванович")
time.sleep(10)

# Найти галлочку выпадающего списка поля "Место заполнения анкеты"
submit_button = driver.find_element(By.XPATH, "//span[@class='p-dropdown-trigger-icon pi pi-chevron-down']")

# Нажать на галочку
submit_button.click()
time.sleep(10)

# Выбор "Места заполнения анкеты" по платформе из списка
submit_button = driver.find_element(By.XPATH, "//li[@aria-label='ЛК 44']")

# Нажать на выбранную организацию
submit_button.click()
time.sleep(10)

# Поиск кнопки "Добавить товар"
textarea = driver.find_element(By.XPATH, "//rts-icon > svg-icon > svg[@width='24']")
textarea.click()
time.sleep(10)



# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
