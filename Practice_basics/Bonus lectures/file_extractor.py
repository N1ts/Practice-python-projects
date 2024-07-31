import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("black")
source = sg.Text('Select archive', key="archive")
source_input = sg.InputText(key='filepath')
button1 = sg.FilesBrowse('choose', key='filepath_name')
destination = sg.Text('Select destination', key="folder")
destination_input = sg.InputText(key='folderpath')
button2 = sg.FolderBrowse('choose', key="folder_name")
extract_button = sg.Button('Extract', key="extract")
output_message = sg.Text(key="message", text_color="yellow")

window = sg.Window('File Extractor', layout=[
                                                  [source, source_input,button1],
                                                  [destination, destination_input,button2],
                                                  [extract_button, output_message],
                                                  ])

while True:
    event, values = window.read()
    file_path = values["filepath_name"]
    folder_path = values["folder_name"]
    extract_archive(file_path,folder_path)
    window['message'].update(value="Extraction completed!")
    if (event == sg.WIN_CLOSED):
        break
window.close()