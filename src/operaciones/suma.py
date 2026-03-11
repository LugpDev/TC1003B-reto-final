def img_suma(event):
    global imagen_procesada
    pixeles_salida = imagen_procesada.load()

    for x in range(ancho):
        for y in range(alto):
            r1, g1, b1 = pixeles1[x, y]
            r2, g2, b2 = pixeles2[x, y]

            pixeles_salida[x, y] = (
                min(r1 + r2, 255),
                min(g1 + g2, 255),
                min(b1 + b2, 255),
            )
