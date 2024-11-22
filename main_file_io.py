from locale import windows_locale
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests
from PyInstaller.loader.pyiboot01_bootstrap import entry
from Scripts.bottle import response


def upload():
    file_path = fd.askopenfilename()
    if file_path:
        files = {'file': open(file_path, 'rb')}
        response = requests.post('httrs://file.io', files = files)
        if response.status_code == 200:
            link = response.json()['link']
            entry.insert(0, link)


window = Tk()
window.title('Сохранение файла в облаке')
window.geometry('400x200')

button = ttk.Button('Загрузить файл', command = upload)
button.pack()

entry = ttk.Entry.pack()
