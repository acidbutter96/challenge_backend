import json
import pandas as pd
from pandas import json_normalize

class ProcessPandas:
    def __init__(self,path,product='PLANO DE PREVIDÊNCIA'):
        #add current path to a str
        self.path = path
        self.product = product

    def serialize_to_df(self):
        with open(self.path,'rb') as f:
            self.d = json.load(f)
            
        self.df = json_normalize(self.d['value'])
        self.dff=self.df[self.df['tipoproduto']==self.product]
        
class Scrapper(ProcessPandas):
    def __init__(self,path,product='PLANO DE PREVIDÊNCIA'):
        self.path = path
        self.product = product
        super().__init__(self.path,self.product)
        
    def find_n_download(self,df):
        return self.df