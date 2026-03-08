from PIL import Image


class ImageDocument:
    def __init__(self, archivo):
        self.original = Image.open(archivo)
        self.ancho, self.alto = self.original.size
        self.procesada = Image.new("RGB", (self.ancho, self.alto), color="white")
        self.pixeles = self.original.load()

    def borrar_procesada(self):
        self.procesada = Image.new("RGB", (self.ancho, self.alto), color="white")
