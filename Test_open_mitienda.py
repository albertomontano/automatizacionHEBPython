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

def test_open_mitienda1():
    service = Service("C:\Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://exclusivo.mitienda.mx/")
    time.sleep(3)

    locationButton = driver.find_element("xpath","//div[@class='mitiendamx-store-selector-0-x-StoreSelector__CurrentSeller_content']")
    locationButton.click()
    time.sleep(2)
    pickGoButton = driver.find_element("xpath", "//*[contains(text(),'Recoge tu súper en la tienda que prefieras')]")
    pickGoButton.click()

    time.sleep(1)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="city"]')))

    def select_monterrey(driver):
        city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="city"]')))
        drop_city = Select(city)
        drop_city.select_by_visible_text("Monterrey")

    # llamada del método:
    select_monterrey(driver)

    # seleccionar la sucursal:
    miTiendaCabezadaButton = driver.find_element("xpath", "//h3[contains(text(),'MI TIENDA CABEZADA')]")
    miTiendaCabezadaButton.click()
    time.sleep(8)

    # funcion para buscar un producto / sku en Buscar productos

    def search_sku(driver, sku):
        search = driver.find_element("xpath", "//input[@placeholder='Buscar productos']")
        search.send_keys(sku)
        time.sleep(2)
        search.send_keys(Keys.ENTER)

    # llamar el método anterior:
    search_sku(driver, "leche")

    time.sleep(2)


