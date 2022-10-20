#!d:\cccc2020\TOOL\python-3.9.1-embed-amd64\python.exe

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
