#!/usr/bin/env python
import PySimpleGUI as sg
import ctypes

dll = ctypes.CDLL('shcore.dll')
if dll:
    dll.SetProcessDpiAwareness(2)
    
for i in range(1, 1000):
  sg.one_line_progress_meter(
    '进度条',
    i + 1,
    1000,
    '该进度条key',
    '这是一个进度条',
    orientation='h',
    bar_color=('#F47264', '#FFFFFF')
  )