import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def crear_boton(axes, label):
    btn_axes = plt.axes(axes)
    btn = Button(btn_axes, label, color="lightblue", hovercolor="skyblue")
    return btn
