import os


class CreateAndSave:
    def __init__(self):
        self.actualpath = os.getcwd()
    
    def create_dir(self,path):
        self.newdir = self.actualpath+'/'+path
        self.path = path
        print(self.path)
        try:
            os.mkdir(self.newdir)
        except OSError:
            print('The directory {} could not be created'.format(self.newdir))
        else:
            print('The directory {} has been created successfully'.format(self.newdir))

    def save_str_to_json(self,path,text,filename,encode='utf-8',mode='w'):
        self.create_dir(path)
        self.filename = filename
        self.file = open(self.path+'/'+filename,mode,encoding='{}'.format(encode))
        self.file.write(text)
        print('file has been saved successfully')
        
    def out_to_json(self):
        return 'u'