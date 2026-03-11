from lib.aplicar_mascara import aplicar_mascara
from lib.img_suma import img_suma


def aplicar_bordes(doc, mask_horizontal, mask_vertical, nombre):
    [horizontal, _] = aplicar_mascara(doc, mask_horizontal, "Horizontal")
    [vertical, _] = aplicar_mascara(doc, mask_vertical, "Vertical")

    pixeles = img_suma(doc, horizontal, vertical)

    return [pixeles, nombre]


def prewritt(doc):
    mask_horizontal = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    mask_vertical = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
    return aplicar_bordes(doc, mask_horizontal, mask_vertical, "Prewitt")


def sobel(doc):
    mask_horizontal = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    mask_vertical = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    return aplicar_bordes(doc, mask_horizontal, mask_vertical, "Sobel")
