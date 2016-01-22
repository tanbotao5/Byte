#!/usr/bin/env python
#-*- coding: utf-8 -*-
import wx
import flash
class MyFrame(wx.Frame):   
    """
    This is the main frame of program
    """
    def __init__(self, parent, title):
       # wx.Frame.__init__(self, parent, -1, title, pos=(150, 150), size=(400, 250))
        self.charheight=64
        self.charwidth=64
        self.specwidth=0

       
        self.chrlist=[]
        self.chrpixellist=[]
        self.fontName="宋体"
        self.encode="ASCII"
        self.height=48
        self.weight=wx.NORMAL
         #wx.SWISS
        self.font=wx.Font(self.height,wx.SWISS, wx.NORMAL, self.weight, faceName=self.fontName)
       
        self.buffer = wx.EmptyBitmap(64,64) #320 240
        self.dc = wx.BufferedDC(None,self.buffer)#wx.Size(300,200))
        self.dc.SetPen(wx.Pen("WHITE", 1))
        self.dc.SetBackground(wx.Brush((0,0,0,255),wx.SOLID))
        self.dc.SetTextBackground((255,255,255,255))
        self.dc.SetTextForeground((255,255,255,255))
        self.dc.SetFont(self.font )
#--------------------------------------------------------------------  
    def getCharPixel(self ,chr,width,height):
        """get the pixels of a given char"""          
        self.dc.Clear()
#        print chr,
        self.dc.DrawText(chr,0,0)
        pixel=[]
        for i in range(0,height):
            Mask =0x80
            dot =int(0)
            for j in range(0,width) :
                clr=self.dc.GetPixel(i,j)
                if(clr[0]!=0):
                   dot = dot | Mask
                if ((7==(j & 0x07)) or (j==(height-1))):
                    pixel.append(dot)
                    #tan.kk.append(dot)                    
                    print dot
                    dot=0
                    k=7
                    Mask = 0x80
                    continue
                Mask = Mask >> 1
        return pixel
#----------------------------------------------------------   
class MyApp(wx.App):
    def get64(self,tt):
        frame = MyFrame(None, "Resource generator")
       # self.SetTopWindow(frame)
        str= []
        str = frame.getCharPixel(tt,64,64)
        return str
#app = MyApp(redirect=True)
app=MyApp(redirect=False)
app.get('A')
app.MainLoop()
