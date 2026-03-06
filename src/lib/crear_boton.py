import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def crear_boton(axes, label):
    btn_axes = plt.axes(axes)
    btn = Button(btn_axes, label, color="lightblue", hovercolor="skyblue")
    return btn


# btn_suavizado3x3 = plt.axes([0.34, 0.96, 0.1, 0.04])
# btn_suavizado3x3 = Button(
#     btn_suavizado3x3, "Suavizado 3x3", color="lightblue", hovercolor="skyblue"
# )
# btn_suavizado3x3.on_clicked(lambda event: suavizado_3x3(event, editor))
