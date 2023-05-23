from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

#from main import driver


def test_open_estado1():
    service = Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://estadomx.com/")
    time.sleep(3)

    someButton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@class='all-over-thumb-link']")))
    someButton.click()
    time.sleep(2)
