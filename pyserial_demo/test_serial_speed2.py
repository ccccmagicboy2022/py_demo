#!/usr/bin/env python

import serial
import time
import queue

fifo00 = queue.Queue(0)

ser = serial.Serial("com11", 115200, timeout=0.5)
print(ser.port)

ser.close()
ser.open()
ser.set_buffer_size(rx_size = 1024 * 1000, tx_size = 1024)

packet00 = []
PACKET_BYTE_SIZE = 4096
passed_num = 0
quit = 0
while quit == 0:
    x = ser.read_all()

    if x != b'':
        for xx in x:
            fifo00.put(xx)

    #print(f'fifo: {fifo00.qsize()}')
    if fifo00.qsize() > (2 + PACKET_BYTE_SIZE):
        y = fifo00.get()
        if y == 0xAB:
            #print(y)
            y = fifo00.get()
            if y == 0xCD:
                #print(y)
                packet00 = []
                for yy in range(PACKET_BYTE_SIZE):
                    packet00.append(fifo00.get())
                #print(len(packet00))
                passed_num += 1
                print(f'pass: {passed_num} {fifo00.qsize()}')
                for kk in range(PACKET_BYTE_SIZE):
                    if packet00[kk] == kk % 0x100:
                        pass
                    else:
                        #print('error!')
                        print(f'{packet00[kk]} - {kk % 0x100} - {kk}')
                        #print(packet00)
                        quit = 1
