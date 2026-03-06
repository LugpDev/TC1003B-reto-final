import matplotlib.pyplot as plt


class MatplotlibViewer:
    def __init__(self):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 6))
        plt.subplots_adjust(wspace=0.2)

    def mostrar_original(self, imagen):
        self.ax1.clear()
        self.ax1.imshow(imagen)
        self.ax1.set_title("Imagen Original")
        self.fig.canvas.draw_idle()

    def mostrar_procesada(self, imagen, titulo):
        self.ax2.clear()
        self.ax2.imshow(imagen)
        self.ax2.set_title(titulo)
        self.fig.canvas.draw_idle()
