#!/usr/bin/env python
#-*- coding: utf-8 -*-
import flash
import serial
import tan
import time
import sql
from  basein2 import*
ser = serial.Serial('/dev/ttyUSB3',9600,8,'N',2,timeout = 1)      #配置串口
task = flash.CON_FLASH()
tt = ['波','涛','示']
x = int(0)
y = int(1)
base_x = 0x0E  ###显示一个汉字的地址,地址需要叠加
base_y = 0x0F
tt2 = []
tt3 = []
temp = []
app=MyApp(redirect=False)
#########################
##接受前端数据处理主程序
##cmd:前端传过来字符
## id:摄像头的id号
#########################
def main(cmd,id):
  try:
    global x
    global y
    global base_x
    global base_y
    if '\r\n' in cmd:
       temp2 = cmd.split('\r\n')
       print "temp2=",temp2
       print "1=", cmd.index('\r')
       if(temp2[1] == '   '):           ###只显示一行处理
          tt2 = cmd[:-2]
          tt2=tt2.strip()
          print "strip=",tt2
          tt2 = tt2.lower() 
          print "lower=",tt2                
          for i in range(0,len(tt2)):
              if(tt2[i] =='k'):
                  x=x+2
                  y=y+2
              else:
                 flash.B[x] = base_x 
                 flash.B[y] = base_y
                 print "x=%s y=%s" % (base_x,base_y)
                 x=x+2
                 y=y+2
                 base_x = base_x+2
                 base_y = base_y+2
              #  time.sleep(0.2)
                 temp = app.get64(tt2[i])
                 for m in range(0,512):
                       flash.file_buffer.append(temp[m])
                       print "len_flash=",len(flash.file_buffer)
                 flash.file_length=flash.file_length+512
              
          print "flash.file_length=",flash.file_length
          print "x=%s y=%s" % (x,y)
          tt2 = tt2.replace('k',' ')
          print tt2
          sql.update_remote(id,tt2)
       else:                                             #显示两行处理
          tt2 = cmd.replace('k',' ')
          print tt2
          sql.update_remote(id,tt2)

          tt2 = cmd[:cmd.index('\r')]
          tt2=tt2.strip()
          print "strip=",tt2
          tt2 = tt2.lower()
          print "lower=",tt2
          print "len-tt2=",len(tt2)

          tt3 = cmd[cmd.index('\n')+1 : ]
          tt3=tt3.strip()
          print "strip=",tt3
          tt3 = tt3.lower()
          print "lower=",tt3
          print "len-tt3=",len(tt3)
          for i in range(0,len(tt2)):
              if(tt2[i] =='k'):
                  x=x+2
                  y=y+2
              else:
                 flash.B[x] = base_x
                 flash.B[y] = base_y
                 print "x=%s y=%s base_x=%s base_y=%s" % (x,y,base_x,base_y)
                 x=x+2
                 y=y+2
                 base_x = base_x+2
                 base_y = base_y+2
              #  time.sleep(0.2)
                 temp = app.get64(tt2[i])
                 for m in range(0,512):
                       flash.file_buffer.append(temp[m])
                       print "len_flash=",len(flash.file_buffer)

                 flash.file_length=flash.file_length+512
                 print "flash.file_length=",flash.file_length
          x = 32
          y = 33
          for i in range(0,len(tt3)):
              if(tt3[i] =='k'):
                  x=x+2
                  y=y+2
              else:
                 flash.B[x] = base_x
                 flash.B[y] = base_y
                 print "x=%s y=%s base_x=%s base_y=%s" % (x,y,base_x,base_y)
                 x=x+2
                 y=y+2
                 base_x = base_x+2
                 base_y = base_y+2
              #  time.sleep(0.2)
                 temp = app.get64(tt3[i])
                 for m in range(0,512):
                       flash.file_buffer.append(temp[m])
                       print "len_flash=",len(flash.file_buffer)

                 flash.file_length=flash.file_length+512
                 print "flash.file_length=",flash.file_length

         # print "x=%s y=%s" % (x,y)
       ################
       ###重置相关参数
       ################
       x=0
       y=1
       base_x=0x0E
       base_y=0x0F
       flash.id = id
       task.file_wr()
       time.sleep(2)
       task.save_end()
       time.sleep(2)
       task.reset()
  except:
        pass  #异常处理 忽略所有异常

