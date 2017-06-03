import os, sys
import os.path as P
import shutil

path = os.getcwd()
app = path + '/app'


def errorStr(typeError):
    print('\033[1;31;40m')
    print(typeError)
    print(' _____   _____    _____    _____   _____ ')
    print("| ____| |  _  \  |  _  \  /  _  \ |  _  \ ")
    print('| |__   | |_| |  | |_| |  | | | | | |_| |')
    print('|  __|  |  _  /  |  _  /  | | | | |  _  /')
    print('| |___  | | \ \  | | \ \  | |_| | | | \ \ ')
    print('|_____| |_|  \_\ |_|  \_\ \_____/ |_|  \_\ ')


def createFile(name, auth):
    os.open(name, auth)
    os.close(0)


def createFolder(name):
    os.mkdir(name)

if not (P.exists(path + '/app')):
    createFolder('app')
    os.chdir(app)
    createFolder('img-content')
    createFolder('img-layout')
    createFolder('js')
    createFolder('css')
    os.chdir(path + '/app')
    createFile('index.html', os.O_RDWR|os.O_CREAT)
    os.chdir(path + '/app/css')
    createFile('styles.css', os.O_RDWR|os.O_CREAT)
    os.chdir(path + '/app/js')
    createFile('app.js', os.O_RDWR | os.O_CREAT)
else:
    errorStr('Folders already exist')
    removeFolder = str(input('You want to remove this folder ? (0/1)'))
    if removeFolder == '0':
        shutil.rmtree(app)
        print('Folder removed successfuly')
    else:
        print('Error')