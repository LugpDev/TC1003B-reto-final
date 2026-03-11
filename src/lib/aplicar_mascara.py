def aplicar_mascara(doc, mask, nombre):
    pixeles_salida = doc.procesada.copy().load()

    for x in range(doc.ancho):
        for y in range(doc.alto):
            n = r = g = b = 0
            radio = len(mask) // 2
            for dx in range(-radio, radio + 1):
                for dy in range(-radio, radio + 1):
                    if 0 <= x + dx < doc.ancho and 0 <= y + dy < doc.alto:
                        pixel = doc.pixeles[x + dx, y + dy]
                        peso = mask[dx + radio][dy + radio]
                        r += pixel[0] * peso
                        g += pixel[1] * peso
                        b += pixel[2] * peso
                        n += peso
            if n == 0:
                n = 1
            r, g, b = r // n, g // n, b // n
            pixeles_salida[x, y] = (r, g, b)

    return [pixeles_salida, nombre]
