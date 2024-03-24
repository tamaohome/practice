# coding: utf-8

import wx


class MainFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent, title="テキストファイルを開く")

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.file_picker = wx.FilePickerCtrl(self.panel, style=wx.FLP_DEFAULT_STYLE)
        vbox.Add(self.file_picker, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        button = wx.Button(self.panel, label="Open")
        button.Bind(wx.EVT_BUTTON, self.on_open)
        vbox.Add(button, proportion=0, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        self.panel.SetSizer(vbox)

        self.Bind(wx.EVT_KEY_DOWN, self.on_key_press)
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_open(self, event):
        path = self.file_picker.GetPath()
        if path:
            print("Selected file:", path)
        else:
            print("No file selected.")

    def on_close(self, event):
        self.Destroy()

    def on_key_press(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.Close()


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
