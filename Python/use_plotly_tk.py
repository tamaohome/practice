# require:
#   pip install plotly, ipywidgets


import tkinter as tk
from plotly.graph_objs import FigureWidget
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("Plotly Graph in Tkinter")

# Plotlyのグラフを作成
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='lines'))

# FigureWidgetを使用してPlotlyのグラフをTkinterウィンドウ上に描画
plotly_fig = FigureWidget(fig)
# plotly_fig_tk = plotly_fig.to_tk()

# TkinterウィンドウにPlotlyのグラフを配置
# plotly_fig_tk.pack(expand=True, fill=tk.BOTH)

# Tkinterウィンドウを表示
root.mainloop()
