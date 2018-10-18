import os
class FileHandler:
    def __init__(self,path):
        self.path = path
        self.validextentios = ['.mp3','.mp4']
        self.foldername = 'mediaFolder'

    def checkPath(self,path):
        return os.path.isdir(path)

    def getsong(self,path):
        for fi in os.listdir():
            for ext in self.validextentios:
                if fi.endswith(ext):
                    return getsong
        else:
            raise Exception "no file not found"
    def createFoder(self):
        os.mkdir(self.folderpath)

    def openfolder(self):
        os.system(f'explorer {self.folderpath}')

    def core(self,add = False):
        self.folderpath = f'{self.path}\\{foldername}'
        fp=self.folderpath
        if self.checkPath(fp):
            if add:
                self.openfolder()
            return self.getsong()
        else:
            self.createFoder()
            self.core(add)









