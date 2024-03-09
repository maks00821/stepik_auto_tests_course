from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    browser.switch_to.alert.accept()

    num = calc(browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text)

    field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    field.send_keys(num)

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()