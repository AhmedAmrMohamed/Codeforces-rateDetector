import os
class Getinp:
    def __init__(self,path):
        self.pkpath = self.getpath(path)


    def getpath(self,path):
        '''remove the file name from the path to return the path to the whole package'''
        path = path.split('\\')
        path.pop()
        return '\\'.join(path)

    def parseline(self,line):
        '''remove the \\n after the line'''
        line = line.split('\\')
        line.pop()
        return ''.join(line)

    def readinp(self):
        '''read the settings file to get the song'''
        try:
            os.chdir(self.pkpath)
            fi = open('settings.txt' , 'r')
            filepath = fi.read()
            # filepath = self.parseline()
            if not len(filepath):
                return None
            return filepath
        except Exception:
            print('wrong')
            return None

    def writeinp(self):
        '''get the song file and write it to the settings.txt file'''
        os.chdir(self.pkpath)
        fi = open('settings.txt','w')
        filepath = input('Enter the path to this song: ')
        print('The program will terminat now, run it again this time with the contest ID (and the handle is optional)')
        print(filepath,file = fi)
        fi.close()
        return filepath
