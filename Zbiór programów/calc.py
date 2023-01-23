import PySimpleGUI as sg
import math

def run():
    layout = [[sg.Text("Podaj pierwszą liczbę"), sg.InputText()],[sg.Text("Podaj drugą liczbę"), sg.InputText()], [sg.Button("+"), sg.Button("-"), sg.Button("*"), sg.Button("/"), sg.Button("^")], [sg.Button("Zaokrąglenie"), sg.Button("sin"), sg.Button("cos"), sg.Button("Exp")]]
    window = sg.Window("Kalkulator", layout)

    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED:
        break
      if event == "+":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(values[0]) + float(values[1]))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "-":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(values[0]) - float(values[1]))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "*":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(values[0]) * float(values[1]))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "/":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(values[0]) / float(values[1]))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "^":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(values[0])**float(values[1]))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "Zaokrąglenie":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(round(float(values[0])))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "sin":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(math.sin(float(values[0]))))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "cos":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(math.sin(float(values[0]))))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
      if event == "Exp":
        layout2 = [[sg.Text("Wynik działania:")], [sg.Text(float(math.exp(float(values[0]))))]]
        window2 = sg.Window("Wynik", layout2)
        window2.read()
    window.close()