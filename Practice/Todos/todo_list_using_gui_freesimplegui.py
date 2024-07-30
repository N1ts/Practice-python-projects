import functions
import FreeSimpleGUI as sg

# UI elements
label = sg.Text("Type in a to-do")
input_text = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
text_area = sg.Listbox(size=(40,10), values=functions.read_file(), key="todos",
                       enable_events=True)
edit_button = sg.Button("Edit")

#display window with UI elements
window = sg.Window('My Todo App', layout=[[label],
                    [input_text,add_button],
                    [text_area, edit_button]],
                   font=('Helvetica', 16))

# while loop to keep showing the window until we close manually
while True:
    events, values = window.read()
    print(events)
    print(values)
    # print(values['todos'])
    match events:
        case "Add":
            todos = functions.read_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_file(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.read_file()
            index = todos.index(todo_to_edit)
            print(index)
            todos[index] = new_todo
            print(todos[index])
            print(todos)
            functions.write_file(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()