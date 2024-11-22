from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def upload():
    try:
        file_path = fd.askopenfilename()
        if file_path:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files = files)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END)
                entry.insert(0, link)
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка: {e}')


window = Tk()
window.title('Сохранение файлов в облаке')
window.geometry('400x200')

button = ttk.Button(text = 'Загрузить файл', command = upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop()
