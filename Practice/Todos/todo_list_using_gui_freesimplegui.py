import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_text = sg.InputText(tooltip="Enter todo")
button = sg.Button("Add")

window = sg.Window('My Todo App', layout=[[label], [input_text,button]])
window.read()
window.close()