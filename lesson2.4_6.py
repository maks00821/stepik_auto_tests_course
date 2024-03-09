from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button = browser.find_element(By.ID, 'book')
button.click()

x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

input1 = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
input1.send_keys(y)

button1 = browser.find_element(By.XPATH, '//button[text()="Submit"]')
button1.click()