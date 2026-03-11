def img_suma(doc, pixeles1, pixeles2):
    pixeles_salida = doc.procesada.copy().load()

    for x in range(doc.ancho):
        for y in range(doc.alto):
            r1, g1, b1 = pixeles1[x, y]
            r2, g2, b2 = pixeles2[x, y]

            pixeles_salida[x, y] = (
                min(r1 + r2, 255),
                min(g1 + g2, 255),
                min(b1 + b2, 255),
            )

    return pixeles_salida
