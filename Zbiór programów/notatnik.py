import PySimpleGUI as sg

def run():
    niezapis = False
    layout = [[sg.Button("Wyjdź")], [sg.Multiline(key="tekst", size=(70,25))], [sg.Text("Nazwa pliku (z rozszerzeniem)"), sg.InputText(key="name")], [sg.Button("Zapisz"), sg.Button("Otwórz")]]
    window = sg.Window("Notatnik", layout)
    while True:
        event, values = window.read()
        if event == "Wyjdź":
            layout2 = [[sg.Text("Czy chcesz zapisać plik?")], [sg.Button("Anuluj i powróć do pliku"), sg.Button("Nie zapisuj")]]
            window2 = sg.Window("Czy chcesz zapisać plik?", layout2)
            while True:
                event2, values2 = window2.read()
                if event2 == "Anuluj i powróć do pliku":
                    break
                if event2 == "Nie zapisuj":
                    niezapis = True
                    break
            window2.close()
        if event == "Zapisz":
            with open("C:/ProgPies Dokumenty/" + values["name"], "w") as file:
                file.write(values["tekst"])
            window3 = sg.Window("Zapisano", [[sg.Text(f"Zapisano plik w C:/ProgPies Dokumenty/")]])
            window3.read()
            break
        if event == "Otwórz":
            with open("C:/ProgPies Dokumenty/" + values["name"], "r") as file:
                window.find_element("tekst").Update(file.read())
        if niezapis == True:
            break
    window.close()