import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from requests.exceptions import Timeout

from app.request.request_from_site import RequestFromSite
from app.config.scrapping import ProcessPandas

#request content from web and save into a json file
r = RequestFromSite()
r.get('http://dados.susep.gov.br/olinda-ide/servico/produtos/versao/v1/odata/DadosProdutos?$format=json')
r.save()

#json saved directory
jf = r.newdir+'/'+r.filename

p = ProcessPandas(jf)
p.serialize_to_df()


_p = os.getcwd()

driver = webdriver.Chrome(_p+'\\chrome_driver\\chromedriver.exe')
driver.get('https://www2.susep.gov.br/safe/menumercado/REP2/Produto.aspx/Consultar')
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'numeroProcesso'))
    )
finally:
    driver.find_element_by_class_name('botaoPesquisar')
    driver.find_element(By.ID,'numeroProcesso').send_keys("15414.004053/2012-57" + Keys.ENTER)
    dl = driver.find_element(By.CLASS_NAME,'linkDownloadRelatorio').get_attribute('onclick').split('=')[1].split("'")[1]
    #driver.quit()


def dll():
    np = 'pdfs'
    l = 'https://www2.susep.gov.br'+dl
    print(l)
    r.download(l,np,'name1.df')