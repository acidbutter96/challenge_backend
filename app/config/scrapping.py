import json
import pandas as pd
from pandas import json_normalize
from selenium import webdriver
from BeautifulSoup import BeautifulSoup

class ProcessPandas:
    def __init__(self,path,product='PLANO DE PREVIDÊNCIA'):
        self.path = path
        self.product = product

    def serialize_to_df(self):
        with open(self.path,'rb') as f:
            self.d = json.load(f)
            
        self.df = json_normalize(self.d['value'])
        self.dff=self.df[self.df['tipoproduto']==self.product]
        
class Scrapper(ProcessPandas):
    def __init__(self,path,product='PLANO DE PREVIDÊNCIA'):
        self.driver = webdriver.Chrome('./chrome_driver')