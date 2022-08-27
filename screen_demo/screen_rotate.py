import win32api as win32
import win32con

rotation_val = 0    #0 or 2
device = win32.EnumDisplayDevices(None, 0)
print(device.DeviceName)
dm = win32.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
dm.DisplayOrientation = rotation_val
win32.ChangeDisplaySettingsEx(device.DeviceName, dm)


