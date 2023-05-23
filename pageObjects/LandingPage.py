from selenium import webdriver
from selenium.webdriver.common.by import By

class PaginaInicio:
    URL = 'https://www.example.com'

    # Localizadores
    CAMPO_CORREO = (By.ID, 'email')
    CAMPO_CONTRASENA = (By.ID, 'password')
    BOTON_INICIAR_SESION = (By.ID, 'login')

    def __init__(self, driver):
        self.driver = driver

    def cargar(self):
        self.driver.get(self.URL)

    def iniciar_sesion(self, correo, contrasena):
        campo_correo = self.driver.find_element(*self.CAMPO_CORREO)
        campo_contrasena = self.driver.find_element(*self.CAMPO_CONTRASENA)
        boton_iniciar_sesion = self.driver.find_element(*self.BOTON_INICIAR_SESION)

        campo_correo.send_keys(correo)
        campo_contrasena.send_keys(contrasena)
        boton_iniciar_sesion.click()