from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# Instanciar el WebDriver de Chrome
driver = webdriver.Chrome()

# Navegar a www.google.com
driver.get("https://www.amazon.es/")

# Encontrar el elemento usando el nombre "accept"
accept_button = driver.find_element(By.NAME, "accept")

# Hacer clic en el botón
accept_button.click()

# Encontrar el elemento con id "twotabsearchtextbox"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enviar las teclas "Vinilo" al cuadro de búsqueda
search_box.send_keys("Vinilo")

sleep(10)

# Cerrar el navegador
driver.quit()