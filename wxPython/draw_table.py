# coding: utf-8
"""
wxPythonのサンプルコード
テーブルを描画する
"""

import wx
import wx.grid


class MainFrame(wx.Frame):

    header = ["品名", "カロリー", "価格"]
    food_table = [
        ["ハンバーガー", 250, 200],
        ["チーズバーガー", 300, 250],
        ["チキンバーガー", 250, 200],
        ["フライドポテト", 380, 300],
        ["チキンナゲット", 300, 250],
        ["コーラ", 180, 150],
    ]

    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(400, 300))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        self.draw_table(panel, self.header, self.food_table)

    def draw_table(self, panel: wx.Panel, header: list[str], table: list[list[str]]):
        """テーブルを描画する"""
        grid = wx.grid.Grid(panel)
        grid.CreateGrid(len(table), len(table[0]))

        # ヘッダーを追加
        for i, column in enumerate(header):
            grid.SetColLabelValue(i, column)

        # セルに値を追加
        for i, row in enumerate(table):
            for j, value in enumerate(row):
                grid.SetCellValue(i, j, str(value))

        # "カロリー", "価格"を右寄せにする
        grid.SetColFormatNumber(1)
        grid.SetColFormatFloat(2, 2)

        sizer = panel.GetSizer()
        sizer.Add(grid, 1, wx.EXPAND)
        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None, "お品書き")
    frame.Show()
    app.MainLoop()
