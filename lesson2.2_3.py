from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap")
    num2 = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap")
    num3 = str(int(num1.text) + int(num2.text))

    drop = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown.custom-select"))
    drop.select_by_value(num3)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()