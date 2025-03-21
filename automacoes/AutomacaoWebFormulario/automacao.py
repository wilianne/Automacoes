from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

servico = Service(r"C:\Users\willi\OneDrive\Desktop\automacoes\AutomacaoWebFormulario\chromedriver.exe")

navegador = webdriver.Chrome(service=servico)

navegador.get(r"C:\Users\willi\OneDrive\Desktop\automacoes\AutomacaoWebFormulario\formulario.html")
time.sleep(2)
navegador.find_element('xpath','//*[@id="nome"]').send_keys("Wilianne Paixao")
time.sleep(2)
navegador.find_element('xpath','//*[@id="email"]').send_keys("williannequaresmapaixao@gmail.com")
time.sleep(2)
navegador.find_element('xpath','/html/body/form/input[3]').click()
time.sleep(5)
