#import os
import math
from selenium import webdriver
import time
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.implicitly_wait(5)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser.get(link)
    text = browser.find_element_by_id("price")
    test = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    if test:
        button = browser.find_element_by_css_selector('button.btn.btn-primary')
        button.click()

        x_element = browser.find_element_by_css_selector('span[id=input_value]')
        x = x_element.text
        y = calc(x)

        pole = browser.find_element_by_css_selector('input[id=answer]')
        pole.send_keys(y)

        button = browser.find_element_by_id('solve')
        button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    #pass