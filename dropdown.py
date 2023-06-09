from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# autobrowser = webdriver.Chrome(ChromeDriverManager.install())
service = Service('C:/Users/ADMIN/Downloads/chromedriver_win3/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

productList = driver.find_elements(By.XPATH, "//select[@id='speed']//option")
print(len(productList))

speedlist = ['Slower', 'Slow', 'Medium', 'Fast', 'Faster']
Filetype = ['TXT file', 'PDF file', 'DOC file', 'Other file']

# s = 1
# # # To check whether requirement list is display in the speedlist dropdown
# for list in productList:
#     speed = list.text
#     if speed in speedlist:
#         assert True
#         print(speed)
#     else:
#         assert False
#         print(speed)
#     try:
#         speedoption = Select(driver.find_element(By.XPATH, "//select[@id='speed']"))
#         speedoption.select_by_index(s)
#         s += 1
#         time.sleep(1)
#     except NoSuchElementException:
#         print()
#
# # To check whether user is able to his/her options
#
# speedoption = Select(driver.find_element(By.XPATH, "//select[@id='speed']"))
# speedoption.select_by_visible_text("Faster")
# time.sleep(3)
#
# # To check whether requirement list display in the file type
#
# fileformatlist = driver.find_elements(By.XPATH, "(//select[@id='files'])[1]//option")
#
# c = 1
# for fileformat in fileformatlist:
#     ff = fileformat.text
#     if ff in Filetype:
#         assert True
#         print(fileformat)
#     else:
#         assert False
#     try:
#         fflist = Select(driver.find_element(By.XPATH, "(//select[@id='files'])[1]"))
#         fflist.select_by_index(c)
#         c += 1;
#         time.sleep(2)
#     except NoSuchElementException:
#         print()

# To check the record dropdown
no = Select(driver.find_element(By.XPATH, "//select[@id='number']"))
no.select_by_index(3)

# To check whether user is able to select product
goproducts = driver.find_element(By.XPATH, "//select[@id='products']")
Selectanimals = driver.find_element(By.ID, "animals")


p = 1
while p < 4:
    s = Select(goproducts)
    s.select_by_index(p)
    a = Select(Selectanimals)
    a.select_by_index(p)
    p += 1
    time.sleep(2)

# To check whether user is able to copy text in the application

texts = driver.find_elements(By.XPATH, "(//div[@class='widget-content'])[4]//span")

for s in texts:
    atext = s.text
    print(atext)



