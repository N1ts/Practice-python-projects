import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_text = sg.InputText(tooltip="Enter todo", key="todo")
button = sg.Button("Add")

window = sg.Window('My Todo App', layout=[[label], [input_text,button]], font=('Helvetica', 16))

while True:
    events, values = window.read()
    match events:
        case "Add":
            todos = functions.read_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)
        case sg.WIN_CLOSED:
            break

window.close()