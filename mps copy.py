import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(3)

driver.get("https://survey-service-trunk.rts-tender.ru/")
time.sleep(3)

textarea = driver.find_element(By.XPATH, "//input[@class='p-element ng-tns-c45-3 p-autocomplete-input p-inputtext p-component rts-control-l ng-star-inserted']")
textarea.send_keys("9723098918")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, "div.ng-star-inserted")
submit_button.click()
time.sleep(3)


butto_pot = driver.find_element(By.CSS_SELECTOR, '[class*="upload-r"] input') 
butto_pot.send_keys(r'C:\Users\Администратор!\Documents\StepicQAA\file.xlsx')
time.sleep(10)

# Загрузить список потребностей 
# Загрузить файл с потребностями //div[@class='survey-form__products-upload-requirements ng-tns-c128-1']//input[@type='file']
# Загрузка файла с ТРУ [class*="upload-t"] input
# Загрузить список товаров //rts-file-uploader[@formcontrolname='productsList']//input[@type='file]
driver.quit()




# current_dir = os.path.abspath(os.path.dirname('mps.py'))
# file = 'file1.txt' 
# path = os.path.join(current_dir, file)




