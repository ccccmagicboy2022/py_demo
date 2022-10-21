#!/usr/bin/env python

import PySimpleGUI as sg
import ctypes

dll = ctypes.CDLL('shcore.dll')
if dll:
    dll.SetProcessDpiAwareness(2)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text(size = (40, 3), text = 'Some text on Row 1', text_color='yellow')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('CH341调试工具', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


