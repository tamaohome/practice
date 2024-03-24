# -*- coding: utf-8 -*-

"""
ホットキーを検出してウインドウを閉じるサンプル

このコードではウインドウが非アクティブの状態でもホットキーを受け付ける

参考URL: https://python-minutes.blogspot.com/2017/06/wxpython_28.html
"""
import wx


class MainFrame(wx.Frame):
    def __init__(self, parent: wx.Window | None, id: int, title: str):
        wx.Frame.__init__(self, parent, id, title, size=(400, 300))

        # キーの設定
        if wx.Platform == '__WXMSW__':
            self.RegisterHotKey(0, wx.MOD_CONTROL, ord("q"))  # Windows用
        elif wx.Platform == '__WXMAC__':
            self.RegisterHotKey(0, wx.MOD_CMD, ord('q'))  # Mac用

        # ホットキーイベントハンドラ
        self.Bind(wx.EVT_HOTKEY, self.callhotkey)

        p = wx.Panel(self, wx.ID_ANY)
        l = wx.StaticText(p, wx.ID_ANY, "ホットキーのテスト")
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(l, flag=wx.ALL, border=10)
        p.SetSizer(layout)

        self.Show()

    def callhotkey(self, event):
        """ホットキーイベント"""

        # ダイアログを表示
        dialog = wx.MessageDialog(self, "ウインドウを閉じますか？", "確認", wx.OK | wx.CANCEL)
        result = dialog.ShowModal()
        dialog.Destroy()

        # OKボタンが押された場合はウインドウを閉じる
        if result == wx.ID_OK:
            self.Close()


if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, wx.ID_ANY, "Ctrl+Q(Cmd+Q)でウインドウを閉じる")
    app.MainLoop()
