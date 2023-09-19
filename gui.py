import PySimpleGUI 
import functions
import time
import os

# create the task file if it does not exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt",'w') as file:
        pass

# create a (filled) text box and input box
PySimpleGUI.theme("Black")
time_label = PySimpleGUI.Text(key="clock")
label = PySimpleGUI.Text("Type in a to-do: ")
input_box = PySimpleGUI.InputText(tooltip="write tasks here", key="todo")
add_button = PySimpleGUI.Button("Add")

list_box = PySimpleGUI.Listbox( values = functions.read_file(),key='tasks',
                                enable_events = True, size = [45,10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")

exit_button = PySimpleGUI.Button("Exit")
# creates a window
wdw = PySimpleGUI.Window('Taskmaster',
                         layout=[[time_label],
                                 [label],
                                 [input_box,add_button],
                                 [list_box,edit_button,complete_button],
                                 [exit_button]], 
                         font = ('Helvetica',20))
while True:
    tasks = functions.read_file()
    event,values = wdw.read(timeout=10)
    # print(event)
    # print(values)
    wdw["clock"].update(value=time.strftime("%b,%d,%Y %H:%M:%S"))
    match event:
        case "Add":
            new_task = values["todo"]+"\n"
            tasks.append(new_task)
            functions.write_to_file(tasks)
            wdw['tasks'].update(values=tasks)
        case PySimpleGUI.WIN_CLOSED:
            break
        case "Edit":
            try:
                selected_task = values['tasks'][0] # the item the user has selected in list Box
                user_input = values['todo'] # this is what user wrote in text box
                index = tasks.index(selected_task)
                tasks[index]=user_input+"\n"
                functions.write_to_file(tasks)
                wdw['tasks'].update(values=tasks)
            except IndexError:
                PySimpleGUI.popup("Please select an item first",title="Error!",font = ('Helvetica',20))
        case 'tasks':
            wdw['todo'].update(value=values['tasks'][0])
        case "Complete":
            try:
                completed_task = values['tasks'][0]
                tasks.remove(completed_task)
                functions.write_to_file(tasks)
                wdw['tasks'].update(values=tasks)
                wdw['todo'].update(value="")
            except IndexError:
                PySimpleGUI.popup("Please select an item first",title="Error!",font = ('Helvetica',20))
        case "Exit":
            break