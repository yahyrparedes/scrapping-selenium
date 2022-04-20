from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # webdriver-manager

# configure ubuntu local
driver_path = '/opt/google/chrome/google-chrome'
# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service)

# configure using webdriver-manager
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)  # Chrome

# commons settings
driver.maximize_window()
time.sleep(1)

# start chrome
driver.get('https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp')

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#txtRuc'))).send_keys('10738840718')

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary'))).click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]')))

consulta_ruc = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]')
consulta_ruc = consulta_ruc.text

print(consulta_ruc)

time.sleep(10)

















# ip :147.182.210.26

# user: root
# pass: kgr8MS2XUpyAE7aH

# https://apps.trabajo.gob.pe/consultas-remype/app/index.html
# https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp
# http://www.osce.gob.pe/consultasenlinea/rnp/consultaruc.asp
# https://apps.osce.gob.pe/perfilprov-ui/
# https://apps.osce.gob.pe/perfilprov-ui/ficha/10097603036


# Si hacer el proyecto integrador usando web mvc (flask) primero un status

# Si el lenguaje y framework puede ser libre para el back nell

# Clase de refuerzo para el tema de integrar apis

# Grupos:

# 01
#


# 02
#


# 03
#


# 04
#






