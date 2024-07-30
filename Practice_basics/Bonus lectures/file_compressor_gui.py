import FreeSimpleGUI as sg
from zip_compressor import make_archive

label1 = sg.Text("Select files to compress:")
input_text1 = sg.InputText()
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input_text2 = sg.InputText()
button2 = sg.FolderBrowse("Choose", key="folder")
compress = sg.Button("Compress")
output_text = sg.Text(key="output", text_color="green")

window = sg.Window('File Zipper', layout=[[label1, input_text1, button1], [label2, input_text2,button2],
                                          [compress, output_text]])
while True:
    event, values = window.read()
    print(event, values)
    filepath = values['files'].split(';')
    folder = values['folder']
    make_archive(filepath,folder)
    window['output'].update(value="Compression completed")

    if (event == sg.WIN_CLOSED):
        break

window.close()