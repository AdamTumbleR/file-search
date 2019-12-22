import os

path = r'/home/pi'

extension=input('Extension: ')
# Function for filter by extension
def filterByExtension(fileName, extension):
    dottindex=0
    for idx, i in enumerate(fileName):
        if i== '.':
            dottindex=idx
    endExtension=fileName[dottindex+1:]
    return endExtension == extension

def listdir(dir):
    fileNames = os.listdir(dir)
    filteredFileNames = filter(lambda x: filterByExtension(x, extension),fileNames)
    for fileNames in filteredFileNames:
        print(fileNames)

listdir(path)