from lib.aplicar_mascara import aplicar_mascara
from lib.img_suma import img_suma


def prewritt(doc):
    mask_horizontal = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    mask_vertical = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
    [horizontal, _] = aplicar_mascara(doc, mask_horizontal, "Prewitt Horizontal")
    [vertical, _] = aplicar_mascara(doc, mask_vertical, "Prewitt Vertical")

    pixeles = img_suma(doc, horizontal, vertical)

    return [pixeles, "Prewitt"]
