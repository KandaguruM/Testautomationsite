import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# autobrowser = webdriver.Chrome(ChromeDriverManager.install())
service = Service('C:/Users/ADMIN/Downloads/chromedriver_win3/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

def test_windowsalert():
    driver.find_element(By.XPATH, "(//button[normalize-space()='Click Me'])[1]").click()
    driver.switch_to.alert.accept()
    time.sleep(2)
    alerttext = driver.find_element(By.XPATH, "(//div[@class='widget-content'])[1]//p").text
    if alerttext == "You pressed OK!":
        assert True
    else:
        assert False

    driver.find_element(By.XPATH, "(//button[normalize-space()='Click Me'])[1]").click()
    driver.switch_to.alert.dismiss()
    time.sleep(2)
    alerttext1 = driver.find_element(By.XPATH, "(//div[@class='widget-content'])[1]//p").text
    if alerttext1 == "You pressed Cancel!":
        assert True
    else:
        assert False


test_windowsalert()