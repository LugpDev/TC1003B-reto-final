from lib.aplicar_mascara import aplicar_mascara


def bordes_horizontales(doc):
    mask = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    return aplicar_mascara(doc, mask, "Bordes horizontales")


def bordes_verticales(doc):
    mask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    return aplicar_mascara(doc, mask, "Bordes verticales")
