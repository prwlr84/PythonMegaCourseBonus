import PySimpleGUI as pysg
from cmprss import *

label1 = pysg.Text('Select files:')
input1 = pysg.Input()
choose_button1 = pysg.FilesBrowse('Choose...', key='files')
label2 = pysg.Text('Select destination folder:')
input2 = pysg.Input()
choose_button2 = pysg.FolderBrowse('Choose...', key='dest')

cmprss_button = pysg.Button('Compress')
label_success = pysg.Text(key='label_success', text_color='green')


layout = [[label1, input1, choose_button1],
          [label2, input2, choose_button2],
          [cmprss_button, label_success]]

window = pysg.Window('File Compressor', layout=layout)

while True:
    event, value = window.read()
    paths = value['files'].split(';')
    dest = value['dest']
    make_archive(paths, dest)
    window['label_success'].update(value='Zip created')

window.close()
