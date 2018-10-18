# from pathlib import Path
import os
# from getinp import Getinp
# x=Getinp(r'C:\Users\Ahmed\Desktop\py\Codeforces rateDetector')
# x.writeinp()
# s=x.readinp()
# print(s)
# print('str',s)
# pa = Path
# p=pa(s)
# print(p.is_dir(pa))
# print(p.is_file())
pa=os.getcwd()
from filehandles import *
x=FileHandler(pa)
x.core()

