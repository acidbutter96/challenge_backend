import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests

options = Options()
options.page_load_strategy = 'normal'

p = os.getcwd()

driver = webdriver.Chrome(p+'\\chrome_driver\\chromedriver.exe',options=options)
driver.get('https://www2.susep.gov.br/safe/menumercado/REP2/Produto.aspx/Consultar')

driver.find_element_by_class_name('botaoPesquisar')
driver.find_element(By.ID,'numeroProcesso').send_keys("15414.004053/2012-57" + Keys.ENTER)

dl = driver.find_element(By.CLASS_NAME,'linkDownloadRelatorio').get_attribute('onclick').split('=')[1].split("'")[1]

r = requests.get('https://www2.susep.gov.br'+dl)
open('test.pdf', 'wb').write(r.content)