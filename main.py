from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest
import pandas as pd

def pytest_addoption(parser):
    parser.addoption("--index", action="store", type=int, help="El índice del elemento a seleccionar")

@pytest.fixture(scope='session')
def driver():
    service = Service("C:\\Drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://exclusivo.mitienda.mx/")
    time.sleep(3)

    locationButton = driver.find_element("xpath", "//div[@class='mitiendamx-store-selector-0-x-StoreSelector__CurrentSeller_content']")
    locationButton.click()
    time.sleep(3)
    pickGoButton = driver.find_element("xpath", "//*[contains(text(),'Recoge tu súper en la tienda que prefieras')]")
    pickGoButton.click()

    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="city"]')))

    def select_monterrey(driver):
        city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="city"]')))
        drop_city = Select(city)
        drop_city.select_by_visible_text("Monterrey")

    #llamada del método:
    select_monterrey(driver)

    #seleccionar la sucursal:
    miTiendaCabezadaButton = driver.find_element("xpath", "//h3[contains(text(),'MI TIENDA CABEZADA')]")
    miTiendaCabezadaButton.click()
    time.sleep(8)

    # Agregar validación con pytest
    location_text = driver.find_element("xpath", "//div[@class='mitiendamx-store-selector-0-x-StoreSelector__CurrentSeller_content']")
    assert location_text.text == "MI TIENDA CABEZADA"
    # Imprimir mensaje en la consola
    print("Prueba exitosa")
    print(f"El texto leído es: {location_text.text}")

    yield driver

    driver.quit()


#Leer el archivo de Excel y obtener los datos de la columna sku:
data = pd.read_excel('skus.xlsx')
skus = data['sku'].tolist()

# Obtener el segundo elemento de la lista skus
#sku = skus[1]

#A continuacion pedimos al usuario que ingrese el índice del elemento
#index = int(input('Ingrese el índice del elemento que desea seleccionar: '))
#sku = skus[index]

#funcion para buscar un producto / sku en Buscar productos
def test_search_sku(driver, request):
    index = request.config.getoption('index')
    sku = skus[index]
    search = driver.find_element("xpath","//input[@placeholder='Buscar productos']")
    search.send_keys(sku)
    time.sleep(3)
    # Vuelve a buscar el elemento search antes de interactuar con él
    search = driver.find_element("xpath","//input[@placeholder='Buscar productos']")
    search.send_keys(Keys.ENTER)

    # Llamar al método search_sku para el elemento seleccionado
    #search_sku(driver, sku)
    time.sleep(2)


time.sleep(1)