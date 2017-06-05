import os, sys
import os.path as P
import shutil
import subprocess

path = os.getcwd()
app = path + '/app'


def errorStr(typeError):
    print('\033[1;31;40m')
    print(typeError)
    print(' _____   _____    _____    _____   _____ ')
    print('| ____| |  _  \  |  _  \  /  _  \ |  _  \ ')
    print('| |__   | |_| |  | |_| |  | | | | | |_| |')
    print('|  __|  |  _  /  |  _  /  | | | | |  _  /')
    print('| |___  | | \ \  | | \ \  | |_| | | | \ \ ')
    print('|_____| |_|  \_\ |_|  \_\ \_____/ |_|  \_\ ')


def createFile(name, auth):
    os.open(name, auth)
    os.close(0)


def createFolder(name):
    os.mkdir(name)


def createFolderDefault():
    createFolder('img-content')
    createFolder('img-layout')
    createFolder('js')
    createFolder('styles')
    os.chdir(path + '/app/styles')
    createFile('styles.scss', os.O_WRONLY | os.O_CREAT)
    createFile('styles.css', os.O_RDWR | os.O_CREAT)

    sty = os.open('styles.css', os.O_RDWR | os.O_CREAT)
    os.write(sty,'@charset "UTF-8";')
    os.close(sty)

    os.chdir(path + '/app/js')
    createFile('app.js', os.O_RDWR | os.O_CREAT)
    os.chdir(path + '/app')
    createFile('index.html', os.O_RDWR | os.O_CREAT)

    idx = os.open('index.html', os.O_RDWR | os.O_CREAT)
    os.write(idx,'<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <link rel="stylesheet" href="styles/styles.css">\n    <title></title>\n  </head>\n  <body>\n\n\n  </body>\n</html>')
    os.close(idx)


print('\033[1;32;40m')
print('PathLab - Simply generator Files/Folders for a fast Workflow \n\n ' )
print('If you need to validate a step press 0, or if you want to exit press 1 \n\n')
print('Thanks you to use this script, its made by Jonathan IBOR student @HETIC \n\n')

start = str(input('Ready to start ? (0/1) : '))
sass = str(input('Want to launch SASS Watcher ? (0/1) : '))
if start == '0':
    if not (P.exists(path + '/app')):
        createFolder('app')
        os.chdir(app)
        createFolderDefault()
        if sass == '0' :
            os.chdir(path + '/app/styles')
            os.system('sass --watch styles.scss:styles.css')
        else:
            os.chdir(path + '/app/styles')
            os.remove('styles.scss')

    else:
        errorStr('Folders already exist')
        removeFolder = str(input('You want to remove this folder ? (0/1)'))
        if removeFolder == '0':
            shutil.rmtree(app)
            print('Folder removed successfuly')
        else:
            print("Error, can't remove this folder. Try again")
else:
    errorStr('Thanks you ! Next time maybe.')
