import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# https://plotly.com/python/3d-surface-plots/
# を2022/02/15に改変しました。
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Your existing code
sur = go.Surface(
    contours={
        "x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color": "white"},
        "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05},
    },
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    z=[
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
    ],
)

fig = go.Figure(sur)
fig.update_layout(
    scene={
        "xaxis": {"nticks": 20},
        "zaxis": {"nticks": 4},
        "camera_eye": {"x": 0, "y": -1, "z": 0.5},
        "aspectratio": {"x": 1, "y": 1, "z": 0.2},
    }
)

# Create a tkinter window
window = tk.Tk()
window.title("Graph")

# Create a matplotlib figure
figure = plt.figure(figsize=(6, 6))

# Create a FigureCanvasTkAgg object
canvas = FigureCanvasTkAgg(figure, master=window)

# Plot the graph on the canvas
canvas.draw()

# Add the canvas to the tkinter window
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
fig.show()

# Show the tkinter window
window.mainloop()