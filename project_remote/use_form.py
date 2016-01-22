#!/usr/bin/env python
# -*- coding: utf-8 -*-                                  # created by tan
import web
import main_from
import time
import sql
#import serial
from web import form
import string
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
cmd = ''
render = web.template.render('/code/project_remote/templates/',base='') #框架模板文件引用
#data = conf_uart()
urls = (                                               #链接地址
        '/', 'base',
        '/test.*','test',
        '/update/(\d+)','update',
)
app = web.application(urls, globals())                #引用地址
class update:
      def POST(self,id):
          id = int(id)
          print 'id=',id
          dataget = web.input()
          print "dataget=",dataget
        #  cmd = dataget.requestContent
         # print "cmd=",cmd

class test:                                         ###接受前端数据处理类
      def POST(self):
          dataget = web.input()
          id=int(dataget.id)
          print "id=",id
          cmd = dataget.a
          print "cmd=",cmd
          print "cmd[0]=%s cmd[1]=%s" %(cmd[0],cmd[1])
          sql.update_remote(id,cmd)
          if cmd ==' ' or '\r\n' not in cmd:
             return render.error() 
          else:
           #    sql.update_remote(id,cmd)
              main_from.main(cmd,int(5))
          print "lencmd=",len(cmd)
          todos=sql.get_remote()
          return render.base_con(todos)
class base:                                          ####默认调用页面显示类
      def GET(self):
          todos=sql.get_remote()
          return  render.base_con(todos)
         # return render.base_con()
      def POST(self):
          dataget = web.input()
if __name__ == "__main__":                               #运行本程序时执行
   app.run()
