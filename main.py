import wx
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"czfnice", pos=wx.Point(-1, -1), size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(500, 300), wx.Size(500, 300))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer2.SetMinSize(wx.Size(500, 300))
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"czfnice", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer2 = wx.GridSizer(2, 2, 0, 0)

        gSizer2.SetMinSize(wx.Size(-1, 60))
        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Github.com官网", wx.DefaultPosition, wx.Size(-1, 60), 0)
        gSizer2.Add(self.m_button6, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"gitee.com官网", wx.DefaultPosition, wx.Size(-1, 60), 0)
        gSizer2.Add(self.m_button7, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2.Add(gSizer2, 1, wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"关于", wx.DefaultPosition, wx.Size(300, 60), 0)
        bSizer2.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"获取本页面源码", wx.DefaultPosition, wx.Size(300, 60), 0)
        bSizer2.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"BY. 陈泽锋", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer2.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button6.Bind(wx.EVT_BUTTON, self.github)
        self.m_button7.Bind(wx.EVT_BUTTON, self.gitee)
        self.m_button4.Bind(wx.EVT_BUTTON, self.about)
        self.m_button5.Bind(wx.EVT_BUTTON, self.more)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def github(self, event):
        event.Skip()

    def gitee(self, event):
        event.Skip()

    def about(self, event):
        event.Skip()

    def more(self, event):
        event.Skip()


import webbrowser
import os

class CalcFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
    def github( self, event ):
        webbrowser.open('https://github.com/czfnice')
    def gitee( self, event ):
        webbrowser.open('https://gitee.com/czfnice')
    def about( self, event ):
        os.popen('.\\about_main\\about_main.exe')
    def more( self, event ):
        webbrowser.open('https://github.com/czfnice/czfnice')
def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == '__main__':
    main()