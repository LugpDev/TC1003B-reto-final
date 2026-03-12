from lib.aplicar_mascara import aplicar_mascara


def contraste(doc):
    pixeles_salida = doc.procesada.copy().load()
    factor = 1.5
    for x in range(doc.ancho):
        for y in range(doc.alto):
            pixel = doc.pixeles[x, y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            g = (r + g + b) // 3

            r = min(255, max(0, int((r - 128) * factor + 128)))
            g = min(255, max(0, int((g - 128) * factor + 128)))
            b = min(255, max(0, int((b - 128) * factor + 128)))

            pixeles_salida[x, y] = (r,g,b)

    return [pixeles_salida, "Contraste"]


from lib.aplicar_mascara import aplicar_mascara

def nitidez(doc):
    mask = [
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ]
    return aplicar_mascara(doc, mask, "Nitidez")
