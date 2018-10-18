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
            print(f'file {filepath}')
            # filepath = self.parseline()
            if not len(filepath):
                return print('file is empty')
            return filepath
        except Exception as xe:
            print('ex',xe)
            return None

    def writeinp(self):
        '''get the song file and write it to the settings.txt file'''
        os.chdir(self.pkpath)
        fi = open('settings.txt','w')
        # filepath = self.getsong(input('Enter the path to this song: '))
        filepath = input('Enter the path to this song: ')
        print(filepath)
        print('The program will terminat now, run it again this time with the contest ID (and the handle is optional)')
        fi.close()
        return filepath

    def getsong(self,path):
        for dir in os.listdir(path):
            if '.mp3' or '.mp4' in dir:
                print(path+'\\'+dir)
                return path+'\\'+dir
        return None
