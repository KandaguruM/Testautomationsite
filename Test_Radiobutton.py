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


def test_radiobutton():
    driver.switch_to.frame("frame-one1434677811")

    radio_button = driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_0']")

    r = radio_button.is_selected()
    time.sleep(1)
    print(r)
    radio_button1 = driver.find_element(By.XPATH, "//label[@for='RESULT_RadioButton-7_1']")
    r1 = radio_button1.is_selected()
    time.sleep(1)
    print(r1)

    radio_button.click()
    time.sleep(3)
    male = radio_button.is_selected()
    time.sleep(1)
    print("Male Radio button is selected", male)

    radio_button1.click()
    time.sleep(3)
    Female = radio_button1.is_selected()
    time.sleep(1)
    print("Female radio button is selected", Female)

    # if radio_button.is_selected():
    #     print("The radio button is already selected.")
    # else:
    #     # Select the radio button if it's not already selected
    #     print("The radio button has been selected.")


# test_radiobutton()

def test_checkbox():
    driver.switch_to.frame("frame-one1434677811")
    value = 0
    while True:
        if value <= 6:
            week = driver.find_element(By.XPATH, "//label[@for='RESULT_CheckBox-8_" + str(value) + "']")
            week.click()
            time.sleep(1)
            value += 1
            print(week.is_selected())
        else:
            break


# test_checkbox()

def test_besttimecontent():
    driver.switch_to.frame("frame-one1434677811")

    btc = driver.find_elements(By.XPATH, "//select[@id='RESULT_RadioButton-9']//option")
    print(len(btc))
    sdime = ['Morning', 'Afternoon', 'Evening']
    for t in sdime:
        if t in sdime:
            print("True")
        else:
            print("False")

    c = Select(driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-9']"))
    c.select_by_visible_text('Morning')
    time.sleep(3)


def test_link():
    driver.switch_to.frame("frame-one1434677811")
    test = driver.find_element(By.XPATH, "//a[normalize-space()='Software Testing Tutorials']").is_enabled()
    link2 = driver.find_element(By.XPATH, "//a[normalize-space()='Software Testing Tools Training']").is_enabled()
    print(test, link2)

    driver.find_element(By.XPATH, "//a[@target='_top']").click()
    time.sleep(3)
    print(driver.title)
    driver.back()
    time.sleep(2)

    #   report abuse link
    driver.switch_to.frame("frame-one1434677811")
    report = driver.find_element(By.XPATH, '//a[normalize-space()="Report abuse"]')
    report.is_enabled()
    report.click()
    time.sleep(2)

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    tiles = driver.title
    if "Report Abuse" == tiles:
        assert True
    else:
        assert False

    driver.close()
    time.sleep(2)

    driver.switch_to.window(tabs[0])

    driver.switch_to.frame("frame-one1434677811")

    submit = driver.find_element(By.XPATH, "//input[@id='FSsubmit']").click()
    time.sleep(3)

    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "//div[@id='blog-pager']//a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//a[normalize-space()='Posts (Atom)'])[1]").click()
    time.sleep(3)


test_link()


