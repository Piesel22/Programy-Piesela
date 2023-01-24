import PySimpleGUI as sg

def run():
    layout = [[sg.Multiline(key="tekst", size=(70,25))], [sg.Text("Nazwa pliku (z rozszerzeniem)"), sg.InputText(key="name")], [sg.Button("Zapisz")]]
    window = sg.Window("Notatnik", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Zapisz":
            with open("C:/ProgPies Dokumenty/" + values["name"], "w") as file:
                file.write(values["tekst"])
            window3 = sg.Window("Zapisano", [[sg.Text(f"Zapisano plik w C:/ProgPies Dokumenty/")]])
            window3.read()
            break
        window.close()