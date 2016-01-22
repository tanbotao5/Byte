#!/usr/bin/env python
#!coding:utf-8
import serial
import string
import shelve
import time
import sql

try:
   stt = sql.get_uartrack()
   i=int(0)
   ser = 'ser'
   uart = []
   set = ['123','1','456']
   for key in stt:
       i=i+1
       uart.append(ser+str(i))
       print ser+str(i),key.uart,int(key.speed),key.databit,key.checkbit,key.stopbit,'\r'
       uart[i-1]= serial.Serial('/dev/'+key.uart,int(key.speed),int(key.databit),key.checkbit,int(key.stopbit))
   print uart
except:
     pass

#ser1 = serial.Serial('/dev/ttyUSB1',19200,7,'E',1,timeout = 1)
#ser = serial.Serial('/dev/ttyUSB2',19200,8,'E',1,timeout = 1)
#ser3 = serial.Serial('/dev/ttyUSB3',19200,7,'E',1,timeout = 1)
#ser1.flush()
#ser.flush()
#ser3.flush()
####################
#云台状态列表 字典
###################
pan_list = {  'up=1':',WU1', 'up=2':',WU2', 'up=3':',WU3', 'up=4':',WU4', 'up=5':',WU5',
              'down=1':',WD1', 'down=2':',WD2', 'down=3':',WD3', 'down=4':',WD4', 'down=5':',WD5',
              'left=1':',WL1', 'left=2':',WL2', 'left=3':',WL3', 'left=4':',WL4', 'left=5':',WL5',
              'right=1':',WR1', 'right=2':',WR2', 'right=3':',WR3', 'right=4':',WR4', 'right=5':',WR5',
              'focus=1':',WI1', 'focus=2':',WI2', 'focus=3':',WI3', 'focus=4':',WI4', 'focus=5':',WI5',
              'focus=-1':',WO1', 'focus=-2':',WO2', 'focus=-3':',WO3', 'focus=-44':',WO4', 'focus=-5':',WO5',
              'hfocus1':',WN1', 'hfocus2':',WN2', 'hfocus3':',WN3', 'hfocus4':',WN4', 'hfocus5':',WN5',
               'zero':',WH1'
           }
####################
#云台初始命令           
###################
cmd1 = ['*','2','A','1',',WH1','A',chr(0x0D)] 
####################
#切换命令初始命令           
###################
cmd2 = ['*','2','V','1',',','1',chr(0x0D)]
####################
#设置预值位初始命令
###################
SET =  ['*','2','A','1',',','W','s','1','A',',','W','1',chr(0x20),'A',chr(0x0D)] 
####################
#调用预值位初始命令           
###################
VIEW = ['*','2','A','1',',','W','v','1','A',',','W','1',chr(0x20),'A',chr(0x0D)] 

CAMt = '1'    #摄像头 监视器初始值
MONt = '1'
camera_value = '1'
camera_id = '1'
flag = int(0)
flag2 = int(0)
flag3 = int(0)
####################
#云台类           
###################
class conf_uart:
        
     def conf(self,uart,data_speed,databit,check_bit,stop_bit,timeout):       
     #ser = serial.Serial('/dev/usbmon0',baudrate=19200,bytesize='EIGHTBITS',parity='PARITY_NONE',stopbits='STOPBITS_ONE',timeout=1)
         ser = serial.Serial('/dev/'+uart,data_speed,databit,check_bit,stop_bit,timeout)
      #x = ser.read(10)
     #s = ser.readline(eol = '\n')
         t = ['FF','23','0A']
         i = 0
         #while True:
         for i in range(0,3):
         #s =ser.writelines(t)
             s = ser.write(t[i].decode('hex'))
         #print "%x" % (string.atoi(t[i],16))
         #if(i == 100 ):
         #break          
         ser.close()
#####################################
#云台控制
#cmd：前台传送命令
#
####################################
     def send_pan(self,cmd):         #发送切换  云台控制命令
           global flag
           global flag2
           global flag3
         #  cmd1 = ['*','1','A','1',',WH1','A',chr(0x0D)]
          # cmd2 = ['*','1','V','1',',','1',chr(0x0D)]
          # SET =  ['*','1','A','1',',','W','s','1','A',',','W','1',chr(0x20),'A',chr(0x0D)] #设置预值位初始值
          # VIEW = ['*','1','A','1',',','W','v','1','A',',','W','1',chr(0x20),'A',chr(0x0D)] #调用预值位初始值
           global  MONt
           global  CAMt
           global camera_value 
           global camera_id 
           if ('cam=' in cmd) or ('mon=' in cmd):
             if 'cam=' in cmd:
               flag3 = flag3 + 1
               CAMt = cmd[4:]
               if CAMt == '':
                  CAMt = '1'
               cmd2[5]=CAMt             #获取cameraID
              # for i in range(0,6):
               #   ser.write(cmd2[i])   #发送切换指令
             if 'mon=' in cmd:
               flag3 = flag3 +1
               MONt = cmd[4:]
               if MONt == '':
                  MONt = '1'
             if flag3 == 2:
               cmd2[3]= MONt             #获取监视器
               cmd2[5]= CAMt
           #    for i in range(0,7):
            #      ser.write(cmd2[i])    #发送切换指令
               self.send_message(cmd)
               print "%s" % cmd2
               flag3 = int(0)
           elif 'spre_' in cmd:
              print 'flag=',flag
              if 'spre_id' in cmd:
                  flag = flag + 1
                  camera_id = cmd[8:]
                  if camera_id == '':
                     camera_id = '1'    #获取设置预置位的摄像头ID
                  print 'flag=',flag          
              if 'spre_value' in cmd:
                  flag = flag +1
                  camera_value = cmd[11:]
                  if camera_value == '':
                     camera_value = '1' #获取预置位号
                  print 'flag=',flag
              if flag == 2:
                set_w = string.atoi(camera_value,10)
                c = string.atoi(CAMt,10)
                if c % 16 == 0:
                   SET[3] = str(c / 16)
                   SET[8] = 'P'
                   SET[13] = 'p'
                else:
                   SET[3] = str((c / 16)+1)
                   if c % 16 ==10:
                       SET[8] = 'J'
                       SET[13] ='J'
                   elif c % 16 == 11:
                       SET[8] = 'K'
                       SET[13] = 'K'
                   elif c % 16 == 12:
                       SET[8] = 'L'
                       SET[13]= 'L'
                   elif c % 16 == 13:
                       SET[8] = 'M'
                       SET[13] = 'M'
                   elif c % 16 == 14:
                       SET[8] = 'N'
                       SET[13] ='N'
                   elif c % 16 == 15:
                       SET[8] = 'O'
                       SET[13] = 'O'
                   else:
                       SET[8] = chr(ord(str(c % 16))+16)
                       SET[13] = chr(ord(str(c % 16))+16)
                c2 = set_w
                if c2 >=16 and c2 <=255:
                   c3 = hex(c2)
                   c4 = str(c3)
                   SET[7] = c4[2]
                   SET[11] = c4[3]
                elif c2>=1 and c2 <=15:
                   c3 = hex(c2)
                   c4 = str(c3)
                   SET[7] = '0'
                   SET[11] = c4[2]
                else:
                   print 'error!!!!'
                print 'flag=',flag
              #  for i in range(0,15):
               #        ser.write(SET[i])
                self.send_message(cmd)   
                print '%s' % SET 
                flag = int(0)
                       
           elif 'vpre_' in cmd:
              print 'flag2=',flag2
              if 'vpre_id' in cmd:
                    flag2 = flag2 +1
                    camera_id = cmd[8:]
                    if camera_id == '':
                       camera_id = '1'    #获取调用预置位的摄像头ID
              if 'vpre_value' in cmd:
                    flag2 = flag2 +1
                    camera_value = cmd[11:]
                    if camera_value == '':
                       camera_value = '1' #获取调用预置位号
              if flag2 == 2:
                view_w = string.atoi(camera_value,10)
                c = string.atoi(CAMt,10)
                if c % 16 == 0:
                  VIEW[3] = str(c / 16)
                  VIEW[8] = 'P'
                  VIEW[13] = 'P'
                else:
                  VIEW[3] = str((c / 16)+1)
                  if c % 16 ==10:
                     VIEW[8] = 'J'
                     VIEW[13] ='J'
                  elif c % 16 == 11:
                     VIEW[8] = 'K'
                     VIEW[13] = 'K'
                  elif c % 16 == 12:
                     VIEW[8] = 'L'
                     VIEW[13]= 'L'
                  elif c % 16 == 13:
                     VIEW[8] = 'M'
                     VIEW[13] = 'M'
                  elif c % 16 == 14:
                     VIEW[8] = 'N'
                     VIEW[13] ='N'
                  elif c % 16 == 15:
                     VIEW[8] = 'O'
                     VIEW[13] = 'O'
                  else:
                     VIEW[8] = chr(ord(str(c % 16))+16)
                     VIEW[13] = chr(ord(str(c % 16))+16)
                 
                c2 = view_w
                if c2 >=16 and c2 <=255:
                   c3 = hex(c2)
                   c4 = str(c3)
                   VIEW[7] = c4[2]
                   VIEW[11] = c4[3]
                elif c2>=1 and c2 <=15:
                   c3 = hex(c2)
                   c4 = str(c3)
                   VIEW[7] = '0'
                   VIEW[11] = c4[2]
                else:
                   print 'error!!!!'
               # for i in range(0,15):
                #   ser.write(VIEW[i])
                self.send_message(cmd)   
                print '%s' % VIEW      
                flag2 =int(0)
   
           else:
               pan = pan_list.get(cmd,',WH1')   #获取云台控制命令字
               cmd1[4] = pan 
               c = string.atoi(CAMt,10)
               if c % 16 == 0:
                  cmd1[3] = str(c / 16)            #确定控制那个RS485口的摄像头
                  cmd1[5] = 'P'                    #确定摄像头ID  A～～～P 
               else:
                  cmd1[3] = str((c / 16)+1)        #同理
                  if c % 16 ==10:
                      cmd1[5] = 'J'
                  elif c % 16 == 11:
                      cmd1[5] = 'K'
                  elif c % 16 == 12:
                      cmd1[5] = 'L'
                  elif c % 16 == 13:
                      cmd1[5] = 'M'
                  elif c % 16 == 14:
                      cmd1[5] = 'N'
                  elif c % 16 == 15:
                      cmd1[5] = 'O'
                  else:
                     cmd1[5] = chr(ord(str(c % 16))+16)
              # for i in range(0,7):
               #     ser.write(cmd1[i])          #发送云台命令
               self.send_message(cmd)   
               print "%s" % cmd1
     def lun(self):                          #轮巡
         yy = ['*2V','1',',','1','\r']
         db = shelve.open('tantt','c')
         yy[1] = db['MON']         
         while True:
              for key in db.keys():
                if key != 'MON':
                  print 'key=',key
                  yy[3] = key                 
                  #ser.write(yy)
                  print yy
                  time.sleep(string.atoi(db[key],10))
     def ztog(self,cmd):         #新组合方式控制  组合切换 
         if "MON" in cmd:
             #print 'tanbotao',cmd
             db = shelve.open('tantt','c')
             db.clear()            
             db['MON'] = cmd[4:cmd.index(':')]
             cmd = cmd[cmd.index(':')+1 :]
             cmd = cmd.split(';')
             print cmd
             for key in cmd:
                 print key
                 if '=' in key:
                     db[str(key[ :key.index('=')])] = key[key.index('=')+1 : ]                  
             db.close()
             self.lun()            
         if "Tpre" in cmd:   #轮巡
             cmd = cmd.split(',')
             for key in cmd:
                if 'Tpre=' in key:
                    pre = key[key.index('=')+1 :] 
                if 'Tpre_id=' in key:
                    pre_id = key[key.index('=')+1 :]
                if 'Tcam_id=' in key:
                    cam_id = key[key.index('=')+1 :]
                if 'Tmon_id=' in key:
                    mon_id = key[key.index('=')+1 :]
             print pre,pre_id,cam_id,mon_id
             #conn = sql.insert_pre(pre.encode('utf8'),pre_id,cam_id,mon_id)
           #  print conn
             self.set_pre(cam_id,pre_id)
     def pre_view(self,cmd):         #新组合方式控制  组合切换
         cmd = cmd.split(';')
         for keyy in cmd:
             keyy = keyy.split(',')
             for key in keyy:
                if 'Tpre=' in key:
                    pre = key[key.index('=')+1 :]
                if 'Tpre_id=' in key:
                    pre_id = key[key.index('=')+1 :]
                if 'Tcam_id=' in key:
                    cam_id = key[key.index('=')+1 :]
                if 'Tmon_id=' in key:
                    mon_id = key[key.index('=')+1 :]
             print pre,pre_id,cam_id,mon_id
             self.view_pre(cam_id,pre_id)       
                             
#####################################
#设置摄像头预值位类
#cam:摄像头编号
#camera_value:预值位编号
####################################
     def set_pre(self,cam,camera_value):
                set_w = string.atoi(camera_value,10)
                c = string.atoi(cam,10)
                if c % 16 == 0:
                   SET[3] = str(c / 16)
                   SET[8] = 'P'
                   SET[13] = 'p'
                else:
                   SET[3] = str((c / 16)+1)
                   if c % 16 ==10:
                       SET[8] = 'J'
                       SET[13] ='J'
                   elif c % 16 == 11:
                       SET[8] = 'K'
                       SET[13] = 'K'
                   elif c % 16 == 12:
                       SET[8] = 'L'
                       SET[13]= 'L'
                   elif c % 16 == 13:
                       SET[8] = 'M'
                       SET[13] = 'M'
                   elif c % 16 == 14:
                       SET[8] = 'N'
                       SET[13] ='N'
                   elif c % 16 == 15:
                       SET[8] = 'O'
                       SET[13] = 'O'
                   else:
                       SET[8] = chr(ord(str(c % 16))+16)
                       SET[13] = chr(ord(str(c % 16))+16)
                c2 = set_w
                if c2 >=16 and c2 <=255:
                   c3 = hex(c2)
                   c4 = str(c3)
                   SET[7] = c4[2]
                   SET[11] = c4[3]
                elif c2>=1 and c2 <=15:
                   c3 = hex(c2)
                   c4 = str(c3)
                   SET[7] = '0'
                   SET[11] = c4[2]
                else:
                   print 'error!!!!'
                print 'flag=',flag
                self.send_message(SET)
              #  for i in range(0,15):
               #        ser.write(SET[i])
                print '%s' % SET
     def send_message(self,cmd):
         global uart
         for i in range(0,len(cmd)):
             for j in range(len(uart)):
                 uart[j].write(cmd[i])
#####################################
#调用摄像头预值位类
#cam:摄像头编号
#camera_value:预值位编号
####################################
     def view_pre(self,cam,camera_value):              
                view_w = string.atoi(camera_value,10)
                c = string.atoi(cam,10)
                if c % 16 == 0:
                  VIEW[3] = str(c / 16)
                  VIEW[8] = 'P'
                  VIEW[13] = 'P'
                else:
                  VIEW[3] = str((c / 16)+1)
                  if c % 16 ==10:
                     VIEW[8] = 'J'
                     VIEW[13] ='J'
                  elif c % 16 == 11:
                     VIEW[8] = 'K'
                     VIEW[13] = 'K'
                  elif c % 16 == 12:
                     VIEW[8] = 'L'
                     VIEW[13]= 'L'
                  elif c % 16 == 13:
                     VIEW[8] = 'M'
                     VIEW[13] = 'M'
                  elif c % 16 == 14:
                     VIEW[8] = 'N'
                     VIEW[13] ='N'
                  elif c % 16 == 15:
                     VIEW[8] = 'O'
                     VIEW[13] = 'O'
                  else:
                     VIEW[8] = chr(ord(str(c % 16))+16)
                     VIEW[13] = chr(ord(str(c % 16))+16)
                  
                c2 = view_w
                if c2 >=16 and c2 <=255:
                   c3 = hex(c2)
                   c4 = str(c3)
                   VIEW[7] = c4[2]
                   VIEW[11] = c4[3]
                elif c2>=1 and c2 <=15:
                   c3 = hex(c2)
                   c4 = str(c3)
                   VIEW[7] = '0'
                   VIEW[11] = c4[2]
                else: 
                   print 'error!!!!'
                self.send_message(VIEW)

               # for i in range(0,15):
                #   ser.write(VIEW[i])
                print '%s' % VIEW   

             
       
      
