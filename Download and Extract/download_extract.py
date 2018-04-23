import urllib2
import os

#sorry just testing pull requests on git. Good work.
'''Download'''

print("Downloading...")

destDir="data"
os.mkdir(destDir)

fileName="my_file.zip"
filePath=os.path.join(destDir,fileName)

url = 'https://example.tar.gz'
f = urllib2.urlopen(url)

with open(filePath, "wb") as code:
    code.write(f.read())

'''Extraxt tar'''

print("Extracting...")
import tarfile
tar = tarfile.open(filePath)
tar.extractall(path=destDir)
tar.close()


'''Extract zip'''

print("Extracting...")
from zipfile import ZipFile
thefile=ZipFile(filePath)
thefile.extractall(destDir)
thefile.close()


