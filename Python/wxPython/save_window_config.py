# coding: utf-8

"""
ウインドウ位置とサイズをiniファイルに保存するサンプル
"""

import wx

from config_manager import ConfigManager


class MainFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent, title="ウインドウの位置とサイズを保存")

        self.config = ConfigManager(__file__)
        
        # 画面領域からウインドウ座標の最小値を取得
        min_point: tuple[int, int] = wx.Display().GetClientArea().GetPosition()  
        self.config.position.min_point = min_point
        
        self.SetPosition(self.config.position.point)
        self.SetSize(*self.config.size.size)

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.Bind(wx.EVT_MOVE, self.on_move)
        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.panel = wx.Panel(self)

        # self.box = wx.BoxSizer(wx.VERTICAL)
        # self.console_log = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        # self.box.Add(self.console_log, 1, wx.EXPAND | wx.ALL, 10)
        self.display_status()
        self.Show()

    def on_move(self, event):
        self.config.position.x = self.GetPosition().x
        self.config.position.y = self.GetPosition().y
        self.display_status()
        event.Skip()

    def on_resize(self, event):
        self.config.size.width = self.GetSize().width
        self.config.size.height = self.GetSize().height
        self.display_status()
        event.Skip()

    def on_close(self, event):
        print("ウインドウが閉じられました")
        self.config.save()
        self.Destroy()
        event.Skip()

    def display_status(self):
        """メインウインドウに文字列を表示"""
        label = (
            "X: "
            + str(self.GetPosition().x)
            + " "
            + "Y: "
            + str(self.GetPosition().y)
            + "\n"
            + "Width: "
            + str(self.GetSize().width)
            + " "
            + "Height: "
            + str(self.GetSize().height)
        )

        if not hasattr(self, "config_text"):
            self.config_text = wx.StaticText(self.panel, label=label)
            self.config_text.SetPosition((10, 10))
            self.config_text.SetFont(
                wx.Font(
                    18,
                    wx.FONTFAMILY_TELETYPE,
                    wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL,
                )
            )
        else:
            self.config_text.SetLabel(label)


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
