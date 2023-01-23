
import PySimpleGUI as sg
import datetime

def getTime():
    return datetime.datetime.now()

def run():
    layout = [[sg.Text('', key='_time_')]]
    window = sg.Window('Zegar', layout)
    while True:
        event, values = window.Read(timeout=10)
        if event == sg.WIN_CLOSED:
            break
        window.find_element('_time_').Update(getTime())
    window.close()