def binarizado_fijo(doc):
    pixeles_salida = doc.procesada.load()

    umbral = 128

    for x in range(doc.ancho):
        for y in range(doc.alto):
            pixel = doc.pixeles[x, y]

            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            g = (r + g + b) // 3

            if g <= umbral:
                pixeles_salida[x, y] = (0, 0, 0)
            else:
                pixeles_salida[x, y] = (255, 255, 255)

    return "Binarizado fijo"


def binarizado_dinamico(doc):
    pixeles_salida = doc.procesada.load()

    datos = doc.original.getdata()
    suma = sum((r + g + b) // 3 for r, g, b in datos)
    umbral = suma / (doc.ancho * doc.alto)

    for x in range(doc.ancho):
        for y in range(doc.alto):
            pixel = doc.pixeles[x, y]

            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            g = (r + g + b) // 3

            if g <= umbral:
                pixeles_salida[x, y] = (0, 0, 0)
            else:
                pixeles_salida[x, y] = (255, 255, 255)

    return "Binarizado dinámico"
