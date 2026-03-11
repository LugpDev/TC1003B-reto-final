import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from core.editor import Editor
from filtros.escala_grises import escala_grises
from filtros.binarizado import binarizado_fijo, binarizado_dinamico
from filtros.inverso import inverso
from filtros.suavizado import suavizado_3x3, suavizado_5x5, suavizado_7x7
from filtros.bordes import prewritt, sobel, roberts, canny
from lib.crear_boton import crear_boton


Tk().withdraw()
archivo = askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.avif")])
if not archivo:
    exit()


editor = Editor(archivo)
editor.mostrar_imagenes()


btn_grises = crear_boton([0.0, 0.96, 0.08, 0.04], "Grises")
btn_grises.on_clicked(lambda event: editor.aplicar_filtro(escala_grises))

btn_binario_fijo = crear_boton([0.08, 0.96, 0.08, 0.04], "Binario fijo")
btn_binario_fijo.on_clicked(lambda event: editor.aplicar_filtro(binarizado_fijo))

btn_binario_dinamico = crear_boton([0.16, 0.96, 0.1, 0.04], "Binario dinámico")
btn_binario_dinamico.on_clicked(
    lambda event: editor.aplicar_filtro(binarizado_dinamico)
)

btn_inverso = crear_boton([0.26, 0.96, 0.08, 0.04], "Inverso")
btn_inverso.on_clicked(lambda event: editor.aplicar_filtro(inverso))

btn_suavizado3x3 = crear_boton([0.34, 0.96, 0.1, 0.04], "Suavizado 3x3")
btn_suavizado3x3.on_clicked(lambda event: editor.aplicar_filtro(suavizado_3x3))

btn_suavizado5x5 = crear_boton([0.44, 0.96, 0.1, 0.04], "Suavizado 5x5")
btn_suavizado5x5.on_clicked(lambda event: editor.aplicar_filtro(suavizado_5x5))

btn_suavizado7x7 = crear_boton([0.54, 0.96, 0.1, 0.04], "Suavizado 7x7")
btn_suavizado7x7.on_clicked(lambda event: editor.aplicar_filtro(suavizado_7x7))

btn_prewitt = crear_boton([0.64, 0.96, 0.07, 0.04], "Prewitt")
btn_prewitt.on_clicked(lambda event: editor.aplicar_filtro(prewritt))

btn_sobel = crear_boton([0.71, 0.96, 0.07, 0.04], "Sobel")
btn_sobel.on_clicked(lambda event: editor.aplicar_filtro(sobel))

btn_roberts = crear_boton([0.78, 0.96, 0.07, 0.04], "Roberts")
btn_roberts.on_clicked(lambda event: editor.aplicar_filtro(roberts))

btn_canny = crear_boton([0.85, 0.96, 0.07, 0.04], "Canny")
btn_canny.on_clicked(lambda event: editor.aplicar_filtro(canny))

btn_save = crear_boton([0.92, 0.96, 0.08, 0.04], "Guardar")
btn_save.on_clicked(lambda event: editor.guardar_imagen())


btn_copy = crear_boton([0.48, 0.48, 0.04, 0.04], "<-")
btn_copy.on_clicked(lambda event: editor.copiar_imagen())

plt.show()
