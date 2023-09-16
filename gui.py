import PySimpleGUI

# create a (filled) text box and input box
label = PySimpleGUI.Text("Type in a to-do: ")
input_box = PySimpleGUI.InputText(tooltip="write tasks here")
add_button = PySimpleGUI.Button("Add")

# creates a window
wdw = PySimpleGUI.Window('My To-do App',layout=[[label],[input_box,add_button]])
wdw.read()
