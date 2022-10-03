import PySimpleGUI as sg
import ctypes

dll = ctypes.CDLL('shcore.dll')
if dll:
    dll.SetProcessDpiAwareness(2)
"""
    This is a simple as it gets.  Calls the "main" function which is the PySimpleGUI Test Harness
    or Control Panel of sorts.   Use it to view themes, upgrade your PySimpleGUI to the GitHub version, etc.
"""

sg.main()

