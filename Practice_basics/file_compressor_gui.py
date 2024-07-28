import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input_text1 = sg.InputText()
button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input_text2 = sg.InputText()
button2 = sg.FolderBrowse("Choose")
compress = sg.Button("Compress")

window = sg.Window('File Zipper', layout=[[label1, input_text1, button1], [label2, input_text2,button2],
                                          [compress]])
window.read()
window.close()