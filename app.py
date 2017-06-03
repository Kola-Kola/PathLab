import os, sys
import os.path as P

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

if not (P.exists(path + '/app')):
    os.mkdir('app')
    os.chdir(app)
    os.mkdir('img-content')
    os.mkdir('img-layout')
    os.mkdir('js')
    os.mkdir('css')
    os.chdir(path + '/app')
    createFile('index.html', os.O_RDWR|os.O_CREAT)
    os.chdir(path + '/app/css')
    createFile('styles.css', os.O_RDWR|os.O_CREAT)
    os.chdir(path + '/app/js')
    createFile('app.js', os.O_RDWR | os.O_CREAT)
else:
    errorStr('Folders already exist')
    choice = input('You want remove folder ? (Y/N)')
    print(choice)
