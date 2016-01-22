#!/usr/bin/env python
#-*- coding: utf-8 -*-
import flash
import serial
import tan
import time
from  basein2 import*
ser = serial.Serial('/dev/ttyUSB3',9600,8,'N',2,timeout = 1)      #配置串口
#tan.kk.append(90)

task = flash.CON_FLASH()
tt = ['波','涛','示']

tt2 = []
app=MyApp(redirect=False)
#for i in range(0,3):
 #    print tt[i]    
 #   app=MyApp(redirect=False)

  #   app.get64(tt[i])
   #  time.sleep(0.2)
tt2 = app.get64(tt[1])
#app.get64(tt[2])
print "win!"
#print "len_tt2",len(tt2)

for i in range(0,512):
    flash.file_buffer.append(tt2[i])
print "len_flash=",len(flash.file_buffer)


print "flash=",len(flash.file_buffer)
print "len=",len(tan.kk)
flash.B[4]=0x12
flash.B[5]=0x13
flash.file_length=flash.file_length+512

task.file_wr()
time.sleep(2)
task.save_end()
time.sleep(2)
task.reset()


