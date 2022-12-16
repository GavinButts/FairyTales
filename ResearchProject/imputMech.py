import PySimpleGUI as sg

sg.theme('LightBrown11')

layout = [  [sg.Text('Please enter your story below.')],
            [sg.Text('Story:'), sg.Multiline(key="texto", size=(50, 20))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]


window = sg.Window('Fairy Tale Text', layout, size=(500, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values['texto'])

window.close()