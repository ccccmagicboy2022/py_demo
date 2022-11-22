#!/usr/bin/env python

import serial
import time
import queue
import asyncio
import threading

fifo00 = queue.Queue(0)
PACKET_BYTE_SIZE = 4096
passed_num = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        async_process()
        print ("退出线程：" + self.name)
        
async def read_command0(delay):
    global ser
    global fifo00
    global stop_thread_flag
    passed_num = 0

    while True:
        #print('this message is from send_command0 function')
        #print(f'fifo: {fifo00.qsize()}')
        if fifo00.qsize() > (1):
            y = fifo00.get()
            if y == 0xAB:
                #print(y)
                y = fifo00.get()
                if y == 0xCD:
                    #print(y)
                    for yy in range(PACKET_BYTE_SIZE):
                        if fifo00.get() == yy % 0x100:
                            pass
                        else:
                            stop_thread_flag = True
                            print(yy)
                    passed_num += 1
                    print(f'pass: {passed_num} {fifo00.qsize()}')

        if (stop_thread_flag == True):
            break        
        await asyncio.sleep(delay)  # 阻塞直到协程sleep返回结果

async def rev_command0(delay):
    global ser
    global fifo00
    global stop_thread_flag

    while True:
        #print('this message is from rev_command0 function')
        x = ser.read(1000000)
        if x != b'':
            for xx in x:
                fifo00.put(xx)    
        if (stop_thread_flag == True):
            break
        await asyncio.sleep(delay)  # 阻塞直到协程sleep返回结果

def init_uart():
    global ser
    ser=serial.Serial("com11", 500000, timeout=0.5)
    print(ser.port)

    ser.close()
    ser.open()
    ser.set_buffer_size(rx_size = 1024, tx_size = 1024)

def async_process():
    asyncio.run(main_co())

async def main_co():
    task1 = asyncio.create_task(read_command0(0.0001))   # unit: s
    task2 = asyncio.create_task(rev_command0(0.020))

    await task1
    await task2

def main():
    global ser
    global thread1
    global stop_thread_flag
    stop_thread_flag = False
    init_uart()

    try:
        thread1 = myThread(1, "Thread-1", 1)
        thread1.start()
    except KeyboardInterrupt:
        ser.close()
        print('Bye-Bye!!!')
        pass

if __name__ == '__main__':
    main()
    