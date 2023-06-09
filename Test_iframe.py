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


def test_googlesearch():
    driver.find_element(By.XPATH, "(//input[@id='Wikipedia1_wikipedia-search-input'])[1]").send_keys('google')
    driver.find_element(By.XPATH, "(//input[@type='submit'])[1]").click()
    time.sleep(2)
    links = driver.find_elements(By.XPATH, "(//div[@id='Wikipedia1_wikipedia-search-results'])[1]//div//a")

    window = 0
    page = 1
    for element in links:
        element.click()
        time.sleep(2)
        # To switch the new tab
        # Get the handles
        windowshandles = driver.window_handles
        # Switch to new tab
        driver.switch_to.window(windowshandles[page])
        # page = page + 1
        print(driver.title)
        driver.close()
        # Switch to default position
        driver.switch_to.window(windowshandles[window])
        time.sleep(1)

test_googlesearch()

driver.find_element(By.XPATH, "(//a[normalize-space()='More »'])[1]").click()
time.sleep(3)
# Get the handles
windowshandles = driver.window_handles
# Switch to new tab
driver.switch_to.window(windowshandles[1])
print(driver.title)


