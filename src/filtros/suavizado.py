from lib.aplicar_mascara import aplicar_mascara


def suavizado_3x3(doc):
    mask = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    return aplicar_mascara(doc, mask, "Suavizado 3x3")


def suavizado_5x5(doc):
    mask = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    return aplicar_mascara(doc, mask, "Suavizado 5x5")


def suavizado_7x7(doc):
    mask = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    return aplicar_mascara(doc, mask, "Suavizado 7x7")
