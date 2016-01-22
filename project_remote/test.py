#!/usr/bin/env python
import sql
import serial
import time
import UART

data = UART.conf_uart()
set = ['123','23','456']
'''stt = sql.get_uartkey()
i=int(0)
ser = 'ser'
uart = []
set = ['123','1','456']
for key in stt:
    i=i+1
    uart.append(ser+str(i))
    print ser+str(i),key.uart,int(key.speed),key.databit,key.checkbit,key.stopbit,'\r'
    uart[i-1]= serial.Serial('/dev/'+key.uart,int(key.speed),int(key.databit),key.checkbit,int(key.stopbit))
print uart'''

data.send_message(set)
'''while True:
      for i in range(0,len(uart)):
          uart[i].write("1234")  
      time.sleep(1)'''
