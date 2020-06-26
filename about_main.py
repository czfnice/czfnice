# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1200, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"about"), wx.VERTICAL)

        sbSizer2.SetMinSize(wx.Size(1200, 700))
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"只是个学生而已，嗯，你好。", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        sbSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"可以通过以下二维码捐助我，我很穷的，但我的梦想是世界首富！", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        sbSizer2.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer1 = wx.GridSizer(2, 2, 0, 0)

        self.m_bitmap3 = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"1.ico", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(-1, -1), 0)
        gSizer1.Add(self.m_bitmap3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.m_bitmap4 = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"2.ico", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_bitmap4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"邮箱：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"czfnice@foxmail.com", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText4.Wrap(-1)
        gSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        sbSizer2.Add(gSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class CalcFrame(MyFrame2):
    def __init__(self, parent):
        MyFrame2.__init__(self, parent)
def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == '__main__':
    main()