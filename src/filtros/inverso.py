def inverso(doc):
    pixeles_salida = doc.procesada.copy().load()

    for x in range(doc.ancho):
        for y in range(doc.alto):
            pixel = doc.pixeles[x, y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]

            pixeles_salida[x, y] = (255 - r, 255 - g, 255 - b)

    return [pixeles_salida, "Colores inversos"]
