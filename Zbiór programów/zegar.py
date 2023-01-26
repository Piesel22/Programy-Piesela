import time
import PySimpleGUI as sg
import datetime

stoperVar = [0, 0, 0]

def getTime():
    return datetime.datetime.now()
def stoper(funkcja):
    if funkcja == 'ret1':
        return stoperVar[0]
    if funkcja == 'ret2':
        return stoperVar[1]
    if funkcja == 'ret3':
        return stoperVar[2]
    if funkcja == 'upd':
        stoperVar[2] = stoperVar[2] + 1
        if stoperVar[2] == 60:
            stoperVar[2] = 0
            stoperVar[1] = stoperVar[1] + 1
        if stoperVar[1] == 60:
            stoperVar[1] == 0
            stoperVar[0] == stoperVar[0] + 1
def run():
    layout = [[sg.Text('', key='_time_')]]
    window = sg.Window('Zegar', layout)
    while True:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED:
            break
        window.find_element('_time_').Update(getTime())
    window.close()
def run2():
    stoperW = False
    layout = [[sg.Text('', key='_stoper_')], [sg.Button("Start"), sg.Button("Stop")]]
    window = sg.Window("Stoper", layout)
    while True:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED:
            break
        if event == "Start":
            stoperW = True
        if event == "Stop":
            stoperW = False
        if stoperW == True:
            stoper('upd')
        window.find_element('_stoper_').Update(f"{stoper('ret1')}:{stoper('ret2')}:{stoper('ret3')}")
        time.sleep(1)
    window.close()