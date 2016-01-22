#!/usr/bin/env python
#!coding:utf-8
import web

db = web.database(dbn='mysql',db='tan_test',user = 'root',pw = '')
def get_data():
    return db.select('tan_uart',order = 'id')
def new_data(uart,byte_speed,databit,stop_bit,check_bit):
    return db.insert('tan_uart',uart=uart,byte_speed=byte_speed,databit=databit,stop_bit=stop_bit,check_bit=check_bit)
def del_data(id):
    db.delete('tan_uart',where="id=$id",vars=locals())
def get_cam_con():
    return db.select('cam_con',order = 'id')
def new_data(dev_type,dev_code,dev_desc,rack,uart_nu,uart_seat,longitude,latitude):
    return db.insert('cam_con',dev_type=dev_type,dev_code=dev_code,dv_desc=dev_desc,rack=rack,uart_nu=uart_nu,uart_seat=uart_seat,longitude=longitude,latitude=latitude)
def del_data(id):
    db.delete('cam_con',where="id=$id",vars=locals())


#和camera数据表相关类，关联配置表
def get_camera_data():
    return db.select('camera',order = 'id')
def get_camera_id():
    return db.select('camera',what='rack_id',order = 'id')
def save_camera(id,matrix_in,matrix_out,camera_id):    
    db.update('camera',where = 'id=$id',matrix_in=matrix_in,matrix_out=matrix_out,camera_id=camera_id,vars=locals())    

def new_camera_data(rack_id,video_in_id,video_out_id,matrix_in,matrix_out,camera_desc):
    return db.insert('camera',rack_id=rack_id,video_in_id=video_in_id,video_out_id=video_out_id,matrix_in=matrix_in,matrix_out=matrix_out,camera_desc=camera_desc)
def del_camera_data(id):
    db.delete('camera',where= "rack_id=$id",vars=locals())
def update_camera_data(id):
     db.update('camera',where ='id=$id',matrix_in=int(0),matrix_out=int(0),camera_id=int(0),vars=locals())  
def del_camera(id):
    db.delete('camera',where='id=$id',vars=locals())
def insert_camera_data(arg1, arg2, arg3):
    count = len(arg1)
    k = 0
    t = 0
    y = 0
    for i in range(0,count):
         for j in range(0,int(arg2[i])):
              k = k+1
              t = t+1
              if t == 17:
                 t = 1 
              if j < int(arg3[i]):
                 y = y+1
                 db.insert('camera',rack_id=arg1[i],video_in_id = k,video_out_id=y,camera_id = t)
              else:
                 db.insert('camera',rack_id =arg1[i],video_in_id= k,camera_id = t)

#和base_con数据表相关类，基本配置表
def get_base_con_data():
    return db.select('base_con',order = 'id')

def get_base_con_data():
    return db.select('base_con',order = 'id')
def insert_base_con_data(rack_id,video_in_id,video_out_id,uart_nu,byte_speed,databit,stop_bit,check_bit):
    return db.insert('base_con',rack_id=rack_id,video_in_id=video_in_id,video_out_id=video_out_id,uart_nu=uart_nu,byte_speed=byte_speed,databit=databit,stop_bit=stop_bit,check_bit=check_bit)
def del_base_con_data(id):
    db.delete('base_con',where="rack_id=$id",vars=locals())
def update_base_con_data(id,rack_id,video_in_id,video_out_id,uart_nu,byte_speed,databit,stop_bit,check_bit):
    db.update('base_con',where="id=$id",rack_id=rack_id,video_in_id=video_in_id,video_out_id=video_out_id,uart_nu=uart_nu,byte_speed=byte_speed,databit=databit,stop_bit=stop_bit,check_bit=check_bit)
#和pre_con相关类
#插入预值表
def insert_pre(pre,pre_id,pcam_id,pmon_id):
    return db.insert('pre_con',Tpre=pre,Tpre_id=pre_id,Tcam_id=pcam_id,Tmon_id=pmon_id)
#查询
def get_pre(pre):
    return db.select('pre_con',where="Tpre=$pre",vars=locals())
####################
##remote相关类
####################
def get_remote():
    return db.select('remote',order = 'id')
def update_remote(id,content):
    db.update('remote',where="abs_addr=$id",content=content,vars=locals())
def insert_remote(phy_id,abs_id,content):
    db.insert('remote',phy_addr = phy_id,abs_addr=abs_id,content=content)
##################
#uart相关类
###############
def get_uart():
    return db.select('uart',order = 'id')
def get_uartkey():
    return db.select('uart',where="type='键盘'",limit=3,vars=locals())
def get_uartrack():
    return db.select('uart',where="type='矩阵'",vars=locals())

def insert_uart(type,uart,bytespeed,databit,stopbit,check_bit):
    return db.insert('uart',type=type,uart=uart,speed=bytespeed,databit=databit,stopbit=stopbit,checkbit=check_bit)
def del_uart(id):
    db.delete('uart',where="id=$id",vars=locals())
def update_uart(id,type,uart,bytespeed,databit,stopbit,checkbit):
    db.update('uart',where="id=$id",type=type,uart=uart,speed=bytespeed,databit=databit,stopbit=stopbit,checkbit=checkbit,vars=locals())
def u_change(cmd):
    if 'type' in cmd: 
       cmd = cmd.split(',')
       for key in cmd:
           if 'type=' in key:
               type = key[key.index('=')+1 :]
           if 'uart=' in key:
               uart = key[key.index('=')+1 :]
           if 'speed=' in key:
               speed = key[key.index('=')+1 :]
           if 'databit=' in key:
               databit = key[key.index('=')+1 :]
           if 'stopbit=' in key:
               stopbit = key[key.index('=')+1 :]
           if 'checkbit=' in key:
               checkbit = key[key.index('=')+1 :]
       print type,uart,speed,databit,stopbit,checkbit
       insert_uart(type,uart,speed,databit,stopbit,checkbit)
    if 'ID' in cmd:
        id = cmd[cmd.index('=')+1 :]
        print id
        id = int(id)
        del_uart(id)
    if 'Type' in cmd: 
       cmd = cmd.split(',')
       print cmd
       for key in cmd:
            if 'Type=' in key:
                type = key[key.index('=')+1 :]
            if 'uart=' in key:
                uart = key[key.index('=')+1 :]
            if 'speed=' in key:
                speed = key[key.index('=')+1 :]
            if 'databit=' in key:
                databit = key[key.index('=')+1 :]
            if 'stopbit=' in key:
                stopbit = key[key.index('=')+1 :]
            if 'checkbit=' in key:
                checkbit = key[key.index('=')+1 :]
            if 'id=' in key:
                ID = key[key.index('=')+1 :]
                ID = int(ID)
                print 'ID=%d' % ID
       print type,uart,speed,databit,stopbit,checkbit,ID
       update_uart(ID,type,uart,speed,databit,stopbit,checkbit)



