
import PySimpleGUI as sg
from datetime import datetime

def run():
    now = datetime.now()
    window = sg.Window("Zegar", [[sg.Text(now)]])
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        now = datetime.now()
        window.update("Zegar", [[sg.Text(now)]])
        window.refresh()
    window.close()