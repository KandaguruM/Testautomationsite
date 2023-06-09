from selenium.webdriver.chrome.service import Service
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# autobrowser = webdriver.Chrome(ChromeDriverManager.install())
service = Service('C:/Users/ADMIN/Downloads/chromedriver_win3/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.find_element(By.XPATH, "(//input[@id='datepicker'])[1]").click()
time.sleep(2)

Monthyear = "September 2022"

while True:
    MonYear = driver.find_element(By.XPATH, "(//div[@class='ui-datepicker-title'])[1]").text

    if MonYear == Monthyear:
        driver.find_element(By.XPATH, "//a[normalize-space()='1']").click()
        break
        time.sleep(3)
    else:
        driver.find_element(By.XPATH, "(//a[@title='Prev'])[1]").click()


