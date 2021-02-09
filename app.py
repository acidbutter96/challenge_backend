from app.request.request_from_site import RequestFromSite
from app.config.scrapping import ProcessPandas

#request content from web and save into a json file
r = RequestFromSite()
r.get('http://dados.susep.gov.br/olinda-ide/servico/produtos/versao/v1/odata/DadosProdutos?$format=json')
r.save()

#json saved directory
jf = r.newdir+'/'+r.filename

#json into a dataframe
p = ProcessPandas(jf)