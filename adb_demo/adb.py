#!d:\cccc2020\TOOL\python-3.9.1-embed-amd64\python.exe
from ppadb.client import Client as AdbClient

def dump_logcat(connect):
    file_obj = connect.socket.makefile()
    for index in range(0, 10):
        print("Line {}: {}".format(index, file_obj.readline().strip()))

def progress(file_name, total_size, sent_size):
    print(f'{file_name}-{total_size}-{sent_size}')

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

for device in devices:
    print(device)
    device.shell("logcat", handler=dump_logcat)



    device.push("screen.png", "/sdcard/Download/aaa.png", progress=progress)

    device.shell("screencap -p /sdcard/screen.png")
    device.pull("/sdcard/screen.png", "screen2.png")

    result = device.get_battery_level()
    print(result)
    result = device.cpu_times()
    print(result)
    percent = device.cpu_percent(interval=1)
    print(percent)
    result = device.cpu_count()
    print(result)

    result = device.reboot()
    print('reboot ok!')

    device.shell('/system/bin/reboot recovery')

    print('recovery ok!')

    device.shell('/system/bin/reboot fastboot')


