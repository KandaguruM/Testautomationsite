from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from test_utilities import test_dynamicparameter
from test_utilities import Write_data

# autobrowser = webdriver.Chrome(ChromeDriverManager.install())
service = Service('C:/Users/ADMIN/Downloads/chromedriver_win3/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(4)

Filename = 'C:/Users/ADMIN/Downloads/EssList.xlsx'
sheetname = "Sheet1"

column = 2


def test_status():
    # How many status is enabled and disable employee in the table
    r = 1

    noofcells = len(driver.find_elements(By.XPATH, "(//div[@class='oxd-table-body'])//div[@class='oxd-table-card']"))
    TotalEnableemployee = 0
    TotalDisableemployee = 0

    for c in range(1, noofcells + 1):

        status = driver.find_element(By.XPATH,
                                     "(//div[@class='oxd-table-card'])[" + str(c) + "]//div[@role='cell'][5]").text
        if status == "Enabled":
            employeename = driver.find_element(By.XPATH, "(//div[@class='oxd-table-card'])[" + str(c) + "]//div["
                                                                                                        "@role='cell'][2]").text
            TotalEnableemployee += 1
        else:
            employeename = driver.find_element(By.XPATH, "(//div[@class='oxd-table-card'])[" + str(c) + "]//div["
                                                                                                        "@role='cell'][2]").text
            print("Disable employee", employeename)
            TotalDisableemployee += 1

    print("Total no of Enableemployee = ", TotalEnableemployee)
    print("Total no of Disableemployee = ", TotalDisableemployee)


def test_userrole():
    # To find the username whose role is ESS
    noofrows = len(driver.find_elements(By.XPATH, "(//div[@class='oxd-table-body'])//div[@class='oxd-table-card']"))

    Ess_employee = 0
    row = 2
    for c in range(1, noofrows + 1):
        role = driver.find_element(By.XPATH,
                                   "(//div[@class='oxd-table-card'])[" + str(c) + "]//div[@role='cell'][3]").text
        if role == "ESS":
            username = driver.find_element(By.XPATH, "(//div[@class='oxd-table-card'])[" + str(c) + "]//div["
                                                                                                    "@role='cell'][2]").text
            print("Essemployeename = ", username)
            Ess_employee += 1
            Write_data(Filename, sheetname, row, column, username)
            row += 1

    print("Total EssRole employee", Ess_employee)
    Write_data(Filename, sheetname, 1, 5, "Total EssRole employee")
    Write_data(Filename, sheetname, 1, 5, Ess_employee)


test_userrole()
