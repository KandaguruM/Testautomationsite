from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from test_utilities import test_dynamicparameter

# autobrowser = webdriver.Chrome(ChromeDriverManager.install())
service = Service('C:/Users/ADMIN/Downloads/chromedriver_win3/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

act = ActionChains(driver)


def test_double():
    doubleelement = driver.find_element(By.XPATH, "(//input[@id='field1'])[1]")
    doubleelement.clear()
    doubleelement.send_keys("Hi guys")

    copytext = driver.find_element(By.XPATH, "(//button[normalize-space()='Copy Text'])[1]")

    act.double_click(copytext).perform()
    time.sleep(2)


# test_double()


def test_draganddrop():
    sour = driver.find_element(By.XPATH, "(//p[normalize-space()='Drag me to my target'])[1]")
    target = driver.find_element(By.XPATH, "(//div[@id='droppable'])[1]")

    act.drag_and_drop(sour, target).perform()
    time.sleep(2)


# test_draganddrop()


def test_slider():
    s = driver.find_element(By.XPATH, "(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
    size = s.size['width']
    print(size)
    offset = size + 50
    print(offset)
    act.click_and_hold(s).move_by_offset(offset, 0).release().perform()
    time.sleep(2)


test_slider()






