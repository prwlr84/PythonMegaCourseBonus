import PySimpleGUI as pysg
from decmprss import *

pysg.theme('LightYellow')

label1 = pysg.Text('Select file:')
input1 = pysg.Input()
choose_button1 = pysg.FileBrowse('Choose...', key='file')
label2 = pysg.Text('Select destination folder:')
input2 = pysg.Input()
choose_button2 = pysg.FolderBrowse('Choose...', key='dest')

cmprss_button = pysg.Button('Unzip')
label_success = pysg.Text(key='label_success', text_color='green')


layout = [[label1, input1, choose_button1],
          [label2, input2, choose_button2],
          [cmprss_button, label_success]]

window = pysg.Window('File Unzippr', layout=layout)

while True:
    event, value = window.read()
    print(event, value)
    path = value['file']
    dest = value['dest']
    print(event)
    if event == pysg.WINDOW_CLOSED:
        break
    if event is not None and (not path or not dest):
        pysg.popup('Something is missing...')
        continue
    unzip_archive(path, dest)
    window['label_success'].update(value='Unzippd')
    window['file'].update(value='')
    window['dest'].update(value='')


window.close()
