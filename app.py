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


def createFolderDefault(ext):
    createFolder('img-content')
    createFolder('img-layout')
    createFolder('js')
    createFolder('styles')
    os.chdir(path + '/app/styles')

    os.chdir(path + '/app/js')
    createFile('app.js', os.O_RDWR | os.O_CREAT)
    os.chdir(path + '/app')
    createFile('index.' + ext, os.O_RDWR | os.O_CREAT)

    idx = os.open('index.' + ext, os.O_RDWR | os.O_CREAT)
    os.write(idx, bytes(
        '<!DOCTYPE html>\n<html>\n  <head>\n '
        '<meta charset="utf-8">\n '
        '<link rel="stylesheet" href="styles/styles.css">\n '
        '<title></title>\n  </head>\n  <body>\n\n\n  </body>\n</html>'))
    os.close(idx)


def editStyle(text):
    css = os.open(text, os.O_RDWR | os.O_CREAT)
    os.write(css, bytes('@charset "UTF-8";\n\n\n'
                       '/*/////////////////////////////////////////////////////////////////////////////'
                       '\n'
                       '\n'
                       '                                    Commons \n'
                       '\n'
                       '\n'
                       '/////////////////////////////////////////////////////////////////////////////*/\n'
                       '\n'
                       ' *{\n '
                       'margin: 0;\n padding: 0;\n}\n*,*:before,*:after {\n   box-sizing:border-box\n}'))
    os.close(css)


print('\033[1;32;40m')
print('PathLab - Simply generator Files/Folders for a fast Workflow \n\n ' )
print('If you need to validate a step press 0, or if you want to exit press 1 \n\n')
print('Thanks you to use this script, its made by Jonathan IBOR student @HETIC \n\n')

start = str(raw_input('Ready to start ? (Yes/No) : '))
sass = str(raw_input('Want to launch SASS Watcher ? (Yes/No) : '))
extensionFile = str(raw_input('Choose your extension (php/html): '))

if start == 'yes'.lower():
    if not (P.exists(path + '/app')):
        createFolder('app')
        os.chdir(app)
        if extensionFile == 'php':
            createFolderDefault('php')
        elif extensionFile == 'html':
            createFolderDefault('html')
        else:
            exit()

        if sass == 'yes'.lower():
            os.chdir(path + '/app/styles')
            editStyle('styles.scss')
            os.system('sass --watch styles.scss:styles.css')

        else:
            os.chdir(path + '/app/styles')
            editStyle('styles.css')

    else:
        errorStr('Folders already exist')
        removeFolder = str(raw_input('You want to remove this folder ? (Yes/No)'))
        if removeFolder == 'yes'.lower():
            shutil.rmtree(app)
            print('Folder removed successfuly')
        else:
            print("Error, can't remove this folder. Try again")
else:
    errorStr('Thanks you ! Next time maybe.')
