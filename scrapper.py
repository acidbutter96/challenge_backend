import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'normal'

p = os.getcwd()

driver = webdriver.Chrome(p+'\\chrome_driver\\chromedriver.exe',options=options)
driver.get('https://www2.susep.gov.br/safe/menumercado/REP2/Produto.aspx/Consultar')

driver.find_element_by_class_name('botaoPesquisar')
driver.find_element(By.ID('numeroProcesso'))
