import PySimpleGUI as sg

import calc
import zegar
import themes

themes.update()

while True:
    program = input("Podaj polecenie: ")
    if program == "calc":
        calc.run()
    if program == "zegar":
        zegar.run()
    if program == "wygląd":
        themes.theme = input("Podaj wygląd: ")
        themes.update()
    if program == "pod_wyg":
        sg.theme_previewer()
        