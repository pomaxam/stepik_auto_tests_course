from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)

    button1 = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()