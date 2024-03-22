# coding: utf-8

import wx


class MainFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="テキストファイルを開く")

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.file_picker = wx.FilePickerCtrl(self.panel, style=wx.FLP_DEFAULT_STYLE)
        vbox.Add(self.file_picker, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        button = wx.Button(self.panel, label="Open")
        button.Bind(wx.EVT_BUTTON, self.on_open)
        vbox.Add(button, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        self.panel.SetSizer(vbox)

    def on_open(self, event):
        path = self.file_picker.GetPath()
        if path:
            print("Selected file:", path)
        else:
            print("No file selected.")


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()
