import requests
import requests.exceptions as re
import json
from app.config.config import CreateAndSave

class RequestFromSite(CreateAndSave):
    
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({'accept-encoding':'utf-8'})
        super().__init__()
    
    def get(self,path):
        self.r = self.s.get(path)
        self.r.encoding = 'utf-8'

    def save(self):
        super().save_str_to_json('data',self.r.text,'result.json')
        
        #self.file = open('data/result.json','w',encoding='utf-8')
        #self.file.write(self.r.text)
        
    def download(self,link,path,name):
        try:
            _r = requests.get(link)
            _r.raise_for_status()
        except re.HTTPError as err:
            print('Error, HTTP: '+ err.response.text,err)
        except re.Timeout as err:
            print('Error, Timeout '+ err.response.text,err)
        except re.ConnectionError as err:
            print('Error, Connection '+ err.response.text,err)
        except re.RequestException as err:
            print('Error, Any '+ err.response.text,err)
        
        super().create_dir(path)
        open('./{}/{}.pdf'.format(path,name), 'wb').write(_r.content)
        
        
