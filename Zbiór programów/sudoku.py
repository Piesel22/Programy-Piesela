import PySimpleGUI as sg

def run():
    lista = [0,0,0,0,0,0,0,0,0]
    layout = [[sg.InputText(size=(2,1)),sg.InputText(size=(2,1)),sg.InputText(size=(2,1))],
              [sg.InputText(size=(2,1)),sg.InputText(size=(2,1)),sg.InputText(size=(2,1))],
              [sg.InputText(size=(2,1)),sg.InputText( size=(2,1)),sg.InputText(size=(2,1))], [sg.Text(key="Błąd")],
              [sg.Button("Sprawdź")]]
    window = sg.Window("Sudoku", layout)
    powtliczb = 0
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Sprawdź":
            for index, text in enumerate(values.values()):
                lista[index] = text
            index1 = 0
            for liczba1 in lista:
                index2 = 0
                for liczba2 in lista:
                    if liczba1 != '' or liczba2 != '':
                        if not index2 == index1:
                            if liczba1 == liczba2:
                                powtliczb = liczba2
                                window.find_element("Błąd").Update(f"Błąd - {powtliczb}")
                                break
                    index2 = index2 + 1
                index1 = index1 + 1
    window.Close()