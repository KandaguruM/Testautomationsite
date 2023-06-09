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

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# driver.execute_script('window.scrollBy(0, 400);')

def test_table():
    noofrows = len(driver.find_elements(By.XPATH, "(//table[@name='BookTable'])[1]//tr"))
    noofcolumns = len(driver.find_elements(By.XPATH, "(//table[@name='BookTable'])[1]//tr/th"))

    # To find book name using author

    for r in range(2, noofrows+1):
        authorname = driver.find_element(By.XPATH, "(//table[@name='BookTable'])[1]//tr["+str(r)+"]//td[2]").text
        if authorname == "Mukesh":
            Bookname = driver.find_element(By.XPATH, "(//table[@name='BookTable'])[1]//tr["+str(r)+"]//td[1]").text
            print(authorname,"    ", Bookname)

    # To find the author using book name

    for r in range(2, noofrows+1):
        BookName = driver.find_element(By.XPATH, "(//table[@name='BookTable'])[1]//tr["+str(r)+"]//td[1]").text
        if BookName == "Master In Selenium":
            AuthorName = driver.find_element(By.XPATH, "(//table[@name='BookTable'])[1]//tr["+str(r)+"]//td[2]").text
            price = driver.find_element(By.XPATH, "(//table[@name='BookTable'])[1]//tr["+str(r)+"]//td[4]").text

            # print(BookName, "    ", AuthorName, "   ", price)





test_table()






