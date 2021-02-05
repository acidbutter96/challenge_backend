from app.request.request_from_site import RequestFromSite
from app.config.scrapping import ProcessPandas

#respective requests and saving json file
r = RequestFromSite()
r.get()
r.save()

#actual json file saved
jf = r.newdir+'/'+r.filename

p = ProcessPandas(jf)