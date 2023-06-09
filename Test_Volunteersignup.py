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


def Test_Fillform():
    driver.switch_to.frame("frame-one1434677811")
    fname = driver.find_element(By.ID, "RESULT_TextField-1")
    fname.send_keys("Guru")
    lname = driver.find_element(By.ID, "RESULT_TextField-2")
    lname.send_keys("M")
    pno = driver.find_element(By.ID, "RESULT_TextField-3")
    pno.send_keys("8825802313")
    country = driver.find_element(By.ID, "RESULT_TextField-4")
    country.send_keys("India")
    city = driver.find_element(By.ID, "RESULT_TextField-5")
    city.send_keys("Kumbakonam")
    email = driver.find_element(By.ID, "RESULT_TextField-6")
    email.send_keys("kandaguru102@gmail.com")

    # To check whether first,last name inputfield shouldn't allow to enter no and special characters
    fname.send_keys("a")
    lname.send_keys("a")
    pno.send_keys("1")
    time.sleep(2)
    country.send_keys('234%^&')
    city.send_keys("233#@!%&")

    firstname = fname.get_attribute('value')
    print(firstname)
    lastname = lname.get_attribute('value')
    print(lastname)
    phonenumber = pno.get_attribute('value')
    print(phonenumber)
    countryname = country.get_attribute('value')
    print(countryname)
    cityname = city.get_attribute('value')
    print(cityname)

    if any(char.isdigit() for char in firstname) or not any(char.isalpha() for char in firstname) or any(
            char.isdigit() for char in lastname) or not any(char.isalpha() for char in lastname) or any(char.isdigit()
        for char in countryname) or not any(char.isalpha() for char in countryname) or any(char.isdigit() for char in
        countryname) or not (char.isalpha() for char in cityname):
        print("First and lastname, county , city shouldn't digit and special character as per requirement")
    else:
        print("first,last name input field should accept only alphabets")

    if any(char.isalpha() for char in phonenumber):
        print("Phone number input field allow user to type alphabets and special characters")
    else:
        print("phone number input field contains digits")




# Test_Fillform()

def test_radiobutton():
    driver.switch_to.frame("frame-one1434677811")
    radio_button =driver.find_element(By.ID, "RESULT_RadioButton-7_0")
    radio_button.click()
    time.sleep(2)

    if radio_button.is_selected():
        print("The radio button is already selected.")
    else:
        # Select the radio button if it's not already selected
        print("The radio button has been selected.")

test_radiobutton()