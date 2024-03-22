# coding: utf-8

import wx
from wx.adv import TaskBarIcon
from pathlib import Path

from Python.config_manager import WindowConfigManager


class MainWindow(wx.Frame):
    window_config = WindowConfigManager()
    
    def __init__(self):
        super().__init__(None, title="ウインドウ位置とサイズの保存", size=(300, 200))
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Bind(wx.EVT_MOVE, self.on_move)
        self.Show()

    def on_move(self, event):
        self.window_config.position.x = self.GetPosition().x
        self.window_config.position.y = self.GetPosition().y
        event.Skip()

    def on_resize(self, event):
        self.window_config.size.width = self.GetSize().width
        self.window_config.size.height = self.GetSize().height
        event.Skip()


if __name__ == "__main__":
    app = wx.App()
    window = MainWindow()
    app.MainLoop()
