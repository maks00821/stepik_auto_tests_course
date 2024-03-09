from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'https://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num = calc(browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text)

    field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    field.send_keys(num)

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()