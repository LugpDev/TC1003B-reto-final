from datetime import datetime
from pathlib import Path
from core.image_document import ImageDocument
from core.matplotlib_viewer import MatplotlibViewer


class Editor:
    def __init__(self, archivo):
        self.doc = ImageDocument(archivo)
        self.viewer = MatplotlibViewer()

    def mostrar_imagenes(self):
        self.viewer.mostrar_original(self.doc.original)
        self.viewer.mostrar_procesada(self.doc.procesada, "Imagen Procesada")

    def aplicar_filtro(self, func):
        [pixeles_salida, nombre] = func(self.doc)
        self.doc.actualizar_procesada(pixeles_salida)
        self.viewer.mostrar_procesada(self.doc.procesada, f"Filtro aplicado: {nombre}")

    def guardar_imagen(self):
        output_dir = Path.cwd() / "outputs"
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = output_dir / f"imagen_procesada_{timestamp}.png"

        self.doc.procesada.save(nombre_archivo)

    def copiar_imagen(self):
        imagen = self.doc.procesada.copy()
        self.doc.original = imagen
        self.doc.pixeles = imagen.load()
        self.doc.borrar_procesada()
        self.mostrar_imagenes()
