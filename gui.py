import PySimpleGUI
import functions

# create a (filled) text box and input box
label = PySimpleGUI.Text("Type in a to-do: ")
input_box = PySimpleGUI.InputText(tooltip="write tasks here", key="todo")
add_button = PySimpleGUI.Button("Add")

# creates a window
wdw = PySimpleGUI.Window('My To-do App',
                         layout=[[label],[input_box,add_button]], 
                         font = ('Helvetica',20))
while True:
    tasks = functions.read_file()
    print(tasks)
    event,values = wdw.read()
    print(event)
    print(values)
    match event:
        case "Add":
            new_task = values["todo"]+"\n"
            tasks.append(new_task)
            functions.write_to_file(tasks)
        case PySimpleGUI.WIN_CLOSED:
            break
