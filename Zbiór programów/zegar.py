
import PySimpleGUI as sg
from datetime import datetime

def run():
    while True:
        window = sg.Window("Zegar", [[sg.Text(datetime.now())]])
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()