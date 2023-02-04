import PySimpleGUI as sg
import math
from decimal import Decimal

maxdec = Decimal(99999999999999999999999999999)

def run():
    layout = [[sg.Text("Podaj pierwszą liczbę"), sg.InputText()],[sg.Text("Podaj drugą liczbę"), sg.InputText()], [sg.Button("+"), sg.Button("-"), sg.Button("*"), sg.Button("/"), sg.Button("^")], [sg.Button("Zaokrąglenie"), sg.Button("sin"), sg.Button("cos"), sg.Button("Exp")]]
    window = sg.Window("Kalkulator", layout)

    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED:
        break
      if event == "+":
        if Decimal(values[0]) + Decimal(values[1]) < maxdec:
            layout2 = [[sg.Text("Wynik działania:")], [sg.Text(Decimal(values[0]) + Decimal(values[1]))]]
        else:
            layout2 = [[sg.Text("Jedna z podanych liczb jest za duża.")]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "-":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(Decimal(values[0]) - Decimal(values[1]))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "*":
        if Decimal(values[0]) * Decimal(values[1]) < maxdec:
            layout2 = [[sg.Text("Wynik działania:")], [sg.Text(Decimal(values[0]) * Decimal(values[1]))]]
        else:
            layout2 = [[sg.Text("Jedna z podanych liczb jest za duża.")]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "/":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(Decimal(values[0]) / Decimal(values[1]))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "^":
        if Decimal(values[0]) ** Decimal(values[1]) < maxdec:
            layout2 = [[sg.Text("Wynik działania:")], [sg.Text(Decimal(values[0])**Decimal(values[1]))]]
        else:
            layout2 = [[sg.Text("Jedna z podanych liczb jest za duża.")]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "Zaokrąglenie":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(round(Decimal(values[0])))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "sin":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(math.sin(Decimal(values[0])))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "cos":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(math.cos(Decimal(values[0])))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "Exp":
        try:
            layout2 = [[sg.Text("Wynik działania:")], [sg.Text(math.exp(Decimal(values[0])))]]
        except OverflowError:
            layout2 = [[sg.Text("Podana liczba jest za duża.")]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
    window.close()
