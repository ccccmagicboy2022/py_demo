import serial
import time

ser=serial.Serial("com11", 115200, timeout=0.5)
print(ser.port)

ser.close()
ser.open()
ser.set_buffer_size(rx_size = 1024 * 100, tx_size = 1024)

all = 0
start = time.time()
while True:
    x = ser.read_all()
    all += len(x)
    diff = time.time() - start
    
    if (diff != 0):
        speed = all / diff / 1000
        print(f"speed: {speed: .3f} KByte/s")