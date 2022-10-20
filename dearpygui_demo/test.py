#!d:\cccc2020\TOOL\python-3.9.1-embed-amd64\python.exe

import dearpygui.dearpygui as dpg
import ctypes

dll = ctypes.CDLL('shcore.dll')
if dll:
    dll.SetProcessDpiAwareness(2)
    
def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
