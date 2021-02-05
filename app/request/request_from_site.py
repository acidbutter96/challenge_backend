import requests
import json
from app.config.config import CreateAndSave

class RequestFromSite(CreateAndSave):
    
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({'accept-encoding':'utf-8'})
        super().__init__()
    
    def get(self):
        self.r = self.s.get('http://dados.susep.gov.br/olinda-ide/servico/produtos/versao/v1/odata/DadosProdutos?$format=json')
        self.r.encoding = 'utf-8'

    def save(self):
        super().save_str_to_json('data',self.r.text,'result.json')
        
        #self.file = open('data/result.json','w',encoding='utf-8')
        #self.file.write(self.r.text)
