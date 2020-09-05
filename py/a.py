import os 
import shutil
spath=input("enter the name of source directory-")
dpath=input("enter the name of destination directory -")
spath=spath+'/'
dpath=dpath+'/'
listOfFiles=os.listdir(spath)
for file in listOfFiles:
    shutil.copy((spath+file),dpath)
    name,ext=os.path.splitext(file)
    