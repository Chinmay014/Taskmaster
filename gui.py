import PySimpleGUI
import functions

# create a (filled) text box and input box
label = PySimpleGUI.Text("Type in a to-do: ")
input_box = PySimpleGUI.InputText(tooltip="write tasks here", key="todo")
add_button = PySimpleGUI.Button("Add")

list_box = PySimpleGUI.Listbox( values = functions.read_file(),key='tasks',
                                enable_events = True, size = [45,10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")

exit_button = PySimpleGUI.Button("Exit")
# creates a window
wdw = PySimpleGUI.Window('My To-do App',
                         layout=[[label],[input_box,add_button],[list_box,edit_button,complete_button],[exit_button]], 
                         font = ('Helvetica',20))
while True:
    tasks = functions.read_file()
    event,values = wdw.read()
    print(event)
    print(values)
    match event:
        case "Add":
            new_task = values["todo"]+"\n"
            tasks.append(new_task)
            functions.write_to_file(tasks)
            wdw['tasks'].update(values=tasks)
        case PySimpleGUI.WIN_CLOSED:
            break
        case "Edit":
            selected_task = values['tasks'][0] # the item the user has selected in list Box
            user_input = values['todo'] # this is what user wrote in text box
            index = tasks.index(selected_task)
            tasks[index]=user_input+"\n"
            functions.write_to_file(tasks)
            wdw['tasks'].update(values=tasks)
        case 'tasks':
            wdw['todo'].update(value=values['tasks'][0])
        case "Complete":
            completed_task = values['tasks'][0]
            tasks.remove(completed_task)
            functions.write_to_file(tasks)
            wdw['tasks'].update(values=tasks)
            wdw['todo'].update(value="")
        case "Exit":
            break