from lib.aplicar_mascara import aplicar_mascara


def prewritt(doc):
    mask_horizontal = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    mask_vertical = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
    horizontal = aplicar_mascara(doc, mask_horizontal, "Prewitt Horizontal")
    vertical = aplicar_mascara(doc, mask_vertical, "Prewitt Vertical")

    print(horizontal, vertical)
