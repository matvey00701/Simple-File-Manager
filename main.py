import PySimpleGUI as gui
import os
import shutil

gui.theme('TanBlue')

from_l = [[gui.Text("From folder")],
          [gui.In(size=(30, 1), enable_events=True, key="-FOLDER-"), gui.FolderBrowse("Browse ")],
          [gui.Button("Copy"), gui.Button("Move"), gui.Button("Duplicate")],
          [gui.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")]]

to_l = [[gui.Text("To folder")],
        [gui.In(size=(30, 1), enable_events=True, key="-FOLDER0-"), gui.FolderBrowse("Browse ")],
        [gui.Checkbox("Dark Theme", key="dark", enable_events=True)],
        [gui.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST0-")]]

layout = [[gui.Column(from_l), gui.Column(to_l)]]


window = gui.Window("File Manager", layout)

filename = ""
folder = ""
folder0 = ""

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        # refresh "from" folder
        folder = values["-FOLDER-"]
        fromFileList = os.listdir(folder)
        fromFileNames = [f for f in fromFileList if os.path.isfile(os.path.join(folder, f))]
        window["-FILE LIST-"].update(fromFileNames)

    elif event == "-FILE LIST-":
        # generating chosen file path
        filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])

    if event == "-FOLDER0-":
        # refresh "to" folder
        folder0 = values["-FOLDER0-"]
        fromFileList = os.listdir(folder0)
        fromFileNames0 = [f for f in fromFileList if os.path.isfile(os.path.join(folder0, f))]
        window["-FILE LIST0-"].update(fromFileNames0)

    if event == "Copy":
        # copy file
        shutil.copy2(filename, folder0)

        # refresh "to" folder
        folder0 = values["-FOLDER0-"]
        fromFileList = os.listdir(folder0)
        fromFileNames0 = [f for f in fromFileList if os.path.isfile(os.path.join(folder0, f))]
        window["-FILE LIST0-"].update(fromFileNames0)

    if event == "Move":

        # move file
        shutil.move(filename, folder0)

        # refresh "to" folder
        folder0 = values["-FOLDER0-"]
        fromFileList = os.listdir(folder0)
        fromFileNames0 = [f for f in fromFileList if os.path.isfile(os.path.join(folder0, f))]
        window["-FILE LIST0-"].update(fromFileNames0)

        # refresh "from" folder
        folder = values["-FOLDER-"]
        fromFileList = os.listdir(folder)
        fromFileNames = [f for f in fromFileList if os.path.isfile(os.path.join(folder, f))]
        window["-FILE LIST-"].update(fromFileNames)

    if event == "Duplicate":
        dup_path = filename.split(".")
        shutil.copy(str(filename), str(dup_path[0]) + "(copy)" + "." + str(dup_path[1]))

        # refresh "from" folder
        folder = values["-FOLDER-"]
        fromFileList = os.listdir(folder)
        fromFileNames = [f for f in fromFileList if os.path.isfile(os.path.join(folder, f))]
        window["-FILE LIST-"].update(fromFileNames)


window.close()