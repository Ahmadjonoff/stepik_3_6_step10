import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element(By.XPATH, "//button[contains(@class, 'add-to-basket')]")