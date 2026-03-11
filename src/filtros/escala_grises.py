def escala_grises(doc):
    pixeles_salida = doc.procesada.copy().load()

    for x in range(doc.ancho):
        for y in range(doc.alto):
            pixel = doc.pixeles[x, y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            g = (r + g + b) // 3
            pixeles_salida[x, y] = (g, g, g)

    return [pixeles_salida, "Escala de grises"]
