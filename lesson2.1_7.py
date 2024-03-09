from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule.check-input')
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox.check-input')
    button2.click()
    button3 = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button3.click()
    print(x)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла