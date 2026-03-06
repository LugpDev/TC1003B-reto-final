import matplotlib.pyplot as plt
from PIL import Image


class Editor:
    def __init__(self, archivo):
        # Setup de la imagen
        imagen_original = Image.open(archivo)
        self.imagen = imagen_original
        ancho, alto = imagen_original.size
        self.imagen_procesada = Image.new("RGB", (ancho, alto), color="white")
        self.ancho = ancho
        self.alto = alto
        self.pixeles = imagen_original.load()
